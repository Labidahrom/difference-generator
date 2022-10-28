install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 --ignore=C901 gendiff

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
