help:
	@echo "make"
	@echo "	install"
	@echo "		Install guardian."
	@echo "	test"
	@echo "		Runs test suite against tests/ directory."
	@echo "	formatter"
	@echo "		Runs black formatter on src/ and tests/ directories."

clean:
	rm -rf build/
	rm -rf .mypy_cache/
	rm -rf dist/

install:
	poetry run python -m pip install -U pip
	poetry install

test: clean
	poetry run pytest tests/

formatter:
	poetry run black src tests
