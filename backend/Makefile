rev:
	poetry run alembic revision --autogenerate

mig:
	poetry run alembic upgrade head

mig_down:
	poetry run alembic downgrade -1

dev:
	poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000

deploy:
	docker-compose -f docker/docker-compose.yml --env-file .env --project-directory . up --build -d

down:
	docker-compose -f docker/docker-compose.yml --env-file .env --project-directory . down

kill:
	taskkill /f /im python.exe