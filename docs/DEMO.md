# Demo — lakehouse-insights-skill

Loom / screen recording script (**60–90 seconds**). Speak calmly; show the terminal, not slides.

## Setup (before record)

```bash
cd lakehouse-insights-skill
python -m venv .venv && source .venv/bin/activate
pip install -e .
# clear scrollback; font size ~16–18pt; dark theme
```

## Exact click / type script

1. Open terminal at repo root. Say: *"This is lakehouse-insights-skill — Governed metrics catalog → proposed SQL for analytics questions. Execute only wi…"*
2. Type `make demo` **or** walk the commands below one by one.
1. Run `python -m lakehouse_insights --help` — wait for JSON / output.
2. Run `python -m lakehouse_insights "revenue by region"` — wait for JSON / output.
3. Run `python -m lakehouse_insights "which pipelines failed" --execute` — wait for JSON / output.
3. Scroll the JSON briefly. Call out one concrete field (citation path, `human_approval_required`, findings, report path, etc.).
4. Close with: *"Offline fixtures only — clone it, `make demo`, adopt the pattern."* Link the GitHub repo in the Loom description.

## Talking points (pick 2)

- Who it's for: Data platform SAs who want agents constrained by a metrics catalog.
- What it is NOT: Not a hosted text-to-SQL LLM service
- Honest MVP: no fabricated production metrics

## Outro card (last 3s)

`github.com/suhail39ahmed/lakehouse-insights-skill`
