.PHONY: test watch install

install:
	uv sync

test:
	uv run pytest

watch:
	uv run ptw . --now 
