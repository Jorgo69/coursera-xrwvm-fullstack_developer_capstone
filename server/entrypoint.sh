#!/bin/sh

# Effectuer les migrations et migrer la base de données
echo "Making migrations and migrating the database..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Exécuter la commande passée en argument (par exemple, gunicorn)
exec "$@"