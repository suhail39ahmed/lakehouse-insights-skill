.PHONY: help install demo test clean

help:
	@echo "Targets: install | demo | clean"

install:
	pip install -e .

demo:
	python -m lakehouse_insights "revenue by region" >/tmp/lh-propose.json
	python -m lakehouse_insights "which pipelines failed" --execute >/tmp/lh-exec.json
	@grep -q sql /tmp/lh-propose.json
	@echo "✓ lakehouse-insights-skill demo OK — propose + sandbox execute" 

clean:
	rm -rf .venv dist build *.egg-info reports labs out audit.log __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
