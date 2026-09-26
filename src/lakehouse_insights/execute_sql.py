from __future__ import annotations

import csv
from pathlib import Path


def execute_sandbox(sql: str, sandbox_dir: Path) -> dict:
    """Minimal executor: only supports the two canned templates without DuckDB.

    If duckdb is installed, use it; else run a tiny CSV aggregation for known SQL shapes.
    """
    try:
        import duckdb  # type: ignore

        con = duckdb.connect(database=":memory:")
        for csv_path in sandbox_dir.glob("*.csv"):
            con.execute(
                f"CREATE TABLE {csv_path.stem} AS SELECT * FROM read_csv_auto('{csv_path.as_posix()}')"
            )
        rows = con.execute(sql).fetchall()
        cols = [d[0] for d in con.description]
        return {"engine": "duckdb", "columns": cols, "rows": [list(r) for r in rows]}
    except ImportError:
        return _csv_fallback(sql, sandbox_dir)


def _csv_fallback(sql: str, sandbox_dir: Path) -> dict:
    low = sql.lower()
    if "daily_revenue" in low and "region" in low:
        path = sandbox_dir / "daily_revenue.csv"
        with path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            agg: dict[str, list[float]] = {}
            for row in reader:
                region = row["region"]
                agg.setdefault(region, [0.0, 0.0])
                agg[region][0] += float(row["revenue_usd"])
                agg[region][1] += float(row["orders"])
        rows = sorted(([r, v[0], int(v[1])] for r, v in agg.items()), key=lambda x: x[1], reverse=True)
        return {"engine": "csv-fallback", "columns": ["region", "revenue_usd", "orders"], "rows": rows}
    if "pipeline_runs" in low and "failed" in low:
        path = sandbox_dir / "pipeline_runs.csv"
        with path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            stats: dict[str, list[float]] = {}
            for row in reader:
                if row["status"] != "failed":
                    continue
                name = row["pipeline_name"]
                stats.setdefault(name, [0.0, 0.0])
                stats[name][0] += 1
                stats[name][1] += float(row["duration_sec"])
        rows = []
        for name, (cnt, dur) in stats.items():
            rows.append([name, int(cnt), dur / cnt if cnt else 0])
        rows.sort(key=lambda x: x[1], reverse=True)
        return {
            "engine": "csv-fallback",
            "columns": ["pipeline_name", "failures", "avg_duration_sec"],
            "rows": rows,
        }
    return {"engine": "csv-fallback", "error": "SQL shape not supported without duckdb", "rows": []}
