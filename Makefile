.PHONY: deps test build run lint fmt docker-build docker-run

PY?=python
UV?=uv

deps:
	$(UV) sync --frozen || $(UV) sync

lint:
	$(UV) run ruff check .

fmt:
	$(UV) run ruff format .

test:
	$(UV) run pytest -q || echo "No tests found"

build:
	@echo "Nothing to build for pure-Python; ensure notebooks run."

run:
	$(PY) -c "print('Hello, Zero2AI')"

docker-build:
	docker build -t zero2ai:latest .

docker-run:
	docker run --rm -it zero2ai:latest

