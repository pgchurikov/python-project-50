install:
	poetry install

gendiff:
	poetry run build_diff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 gendiff
