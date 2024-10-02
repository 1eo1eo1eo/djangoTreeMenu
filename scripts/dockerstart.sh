#!/bin/sh


cd djangoTreeMenu

poetry run python3 manage.py migrate

poetry run python3 manage.py loaddata fixtures/menu/menu.json

poetry run python3 manage.py loaddata fixtures/menu/menuItem.json

poetry run python3 manage.py loaddata fixtures/user/superuser.json

poetry run python3 manage.py runserver 0.0.0.0:8000