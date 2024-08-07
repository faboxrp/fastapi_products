#!/bin/sh

# Ejecuta las migraciones de Alembic
alembic upgrade head

# Ejecuta el servidor Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 9101
