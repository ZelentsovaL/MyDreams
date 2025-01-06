rev:
	alembic revision --autogenerate

mig:
	alembic upgrade head

mig_down:
	alembic downgrade -1

dev:
	poetry run uvicorn main:app --reload --host 0.0.0.0 --port 9000