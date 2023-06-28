SERVER = uvicorn

PORT=8000


# ##########################################################################
# common commands

run:
	$(SERVER) main:app --host 127.0.0.1 --port $(PORT) --reload --lifespan on

install:
	pip install -r requirements.txt

migrate:
	aerich migrate

upgrade:
	aerich upgrade

