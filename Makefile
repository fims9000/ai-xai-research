.PHONY: setup dev test lint docs

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

dev:
	pip install -e .

test:
	pytest -q

lint:
	black src tests && isort src tests

docs:
	mkdocs serve -a localhost:8000
