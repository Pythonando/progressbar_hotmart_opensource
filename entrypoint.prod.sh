#!/usr/bin/env bash

python manage.py migrate --noinput &&
python manage.py collectstatic --noinput &
#!/bin/bash

# Verifica se o superusuário já existe
SUPERUSER_EXISTS=$(python3 manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).exists())")

if [ "$SUPERUSER_EXISTS" == "True" ]; then
    echo "Superusuário já existe."
else
    echo "Criando superusuário..."

    DJANGO_SUPERUSER_USERNAME="admin" \
    DJANGO_SUPERUSER_EMAIL="admin@example.com" \
    DJANGO_SUPERUSER_PASSWORD="admin123" \
    python3 manage.py createsuperuser --noinput

    echo "Superusuário criado com sucesso!"
fi

gunicorn core
