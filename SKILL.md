# Skill: lakehouse-insights

## Purpose
Given a natural-language analytics question and a metrics catalog, propose SQL. Never execute unless `--execute` is explicitly passed.

## Inputs
- Question string
- `metrics/catalog.yaml`

## Outputs
- Proposed SQL + matched metric id + rationale

## Guardrails
- Default is propose-only
- Sandbox CSV/DuckDB only when `--execute`
- No warehouse credentials in this repo
