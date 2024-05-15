#!/bin/bash

set -e
# Verifica se as variáveis POSTGRES_HOST e POSTGRES_PORT estão definidas
if [ -z "$POSTGRES_HOST" ] || [ -z "$POSTGRES_PORT" ]; then
  echo "❌ As variáveis POSTGRES_HOST e POSTGRES_PORT precisam estar definidas."
  exit 1
fi

# Loop até que o serviço no host e porta especificados esteja acessível
while [! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"]; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "🟢 Postgres Database Started Successfully $POSTGRES_HOST:$POSTGRES_PORT"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8080