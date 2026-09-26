# lakehouse-insights-skill

Skill + Python CLI: load `metrics/catalog.yaml` (JSON twin for zero-deps), **propose SQL** for a question, optionally run against sandbox CSV / DuckDB with `--execute`.

## What it is
- Governed metric catalog → SQL proposal
- Explicit execute flag (never auto-run)

## What it is not
- Not a text-to-SQL LLM service
- Not connected to production Databricks / Snowflake

## Architecture

```
  question --> catalog match --> proposed SQL
                                   |
                                   +-- (--execute) --> sandbox CSV/DuckDB
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m lakehouse_insights.cli "revenue by region"
python -m lakehouse_insights.cli "which pipelines failed" --execute
```

## Demo assets checklist
- [ ] `assets/demo.gif`
- [ ] `assets/architecture.png`
- [ ] `docs/DEMO.md`

## License
MIT
