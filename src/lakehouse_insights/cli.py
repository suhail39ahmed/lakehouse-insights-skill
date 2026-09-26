from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .catalog import load_catalog
from .execute_sql import execute_sandbox
from .propose import propose_sql


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="lakehouse-insights", description="Propose (and optionally run) lakehouse SQL")
    p.add_argument("question", help="Analytics question")
    p.add_argument("--catalog", type=Path, default=Path("metrics/catalog.yaml"))
    p.add_argument("--sandbox", type=Path, default=Path("sandbox"))
    p.add_argument("--execute", action="store_true", help="Actually run against sandbox (off by default)")
    args = p.parse_args(argv)

    catalog = load_catalog(args.catalog)
    proposal = propose_sql(args.question, catalog)
    if args.execute and proposal.get("sql"):
        proposal["execute"] = True
        proposal["result"] = execute_sandbox(proposal["sql"], args.sandbox)
    elif args.execute and not proposal.get("sql"):
        print("Nothing to execute — no SQL proposed.", file=sys.stderr)
        return 2
    print(json.dumps(proposal, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
