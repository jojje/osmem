.PHONY: test lint build publish publish-test init-env clean

test:
	poetry run pytest

lint:
	poetry run flake8 --max-line-length 120 --ignore=E302,E305,E231,E226
	poetry run mypy osmem

build:
	poetry build --format wheel

publish:
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	poetry publish

publish-test:
	@echo poetry publish -r test-pypi --username=__token__  --password=[api-token]

init-env:
	python -m pip install poetry
	poetry install

clean:
	rm -rf dist
