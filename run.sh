#!/bin/bash
source env/bin/activate

python /srv/manage.py makemigrations
python /srv/manage.py migrate
python /srv/manage.py loaddata db.json
python /srv/manage.py runserver 0.0.0.0:8000