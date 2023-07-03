SERVER = uvicorn

PORT=8000


# ##########################################################################
# common commands

init:
	python init_project.py

run:
	python main.py

install:
	pip install -r requirements.txt

first-init-db:
	aerich init -t config.db.DB_CONFIG

init-db:
	aerich init-db

migrate:
	aerich migrate

upgrade:
	aerich upgrade

