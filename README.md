# Template Py310-CA-CI-CD

Template Python 3.10

## Clean Architecture

- entities/
- use_cases/
- interfaces/
- framework_and_drivers/

## Tools

- Dependency Manager: Poetry
- Linter: Ruff
- Formatter: Ruff (Black)
- Type Checker: Pyright
- Test: Pytest
- Test Covorage: Pytest-cov
- Test Mutatation: Mutumt

## CI

poetry check
poetry lock
poetry

poerty run ruff
poerty run ruff --format

poetry run pyright

poetry run pytest
poetry run pytest-cov
