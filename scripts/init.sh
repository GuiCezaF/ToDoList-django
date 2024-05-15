#!/bin/bash
echo "Iniciando... 😆"

source ./venv/bin/activate
pip install -r ./djangoapp/requirements.txt
docker compose up --build --force-recreate