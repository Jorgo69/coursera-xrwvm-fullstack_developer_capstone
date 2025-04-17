# Utiliser une image de base Python
FROM python:3.12.0-slim-bookworm

# Définir des variables d'environnement
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Changer le répertoire de travail
WORKDIR $APP

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt $APP
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . $APP

# Autoriser l'exécution du fichier entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Exposer le port 8000 pour l'application
EXPOSE 8000

# Définir le point d'entrée et la commande par défaut
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]