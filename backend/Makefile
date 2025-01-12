rev:
	poetry run alembic revision --autogenerate

mig:
	poetry run alembic upgrade head

mig_down:
	poetry run alembic downgrade -1

dev:
	poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000