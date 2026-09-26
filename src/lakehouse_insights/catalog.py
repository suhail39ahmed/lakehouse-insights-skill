from __future__ import annotations

import json
from pathlib import Path


def load_catalog(path: Path) -> dict:
    """Load metrics catalog. Prefer sibling .json for zero-dep offline runs."""
    json_twin = path.with_suffix(".json") if path.suffix.lower() in {".yaml", ".yml"} else path
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    if json_twin.exists():
        return json.loads(json_twin.read_text(encoding="utf-8"))
    try:
        import yaml  # type: ignore

        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except ImportError as exc:
        raise SystemExit(
            f"No JSON twin at {json_twin} and PyYAML not installed. "
            "Use metrics/catalog.json or pip install pyyaml."
        ) from exc
