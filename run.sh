#!/usr/bin/env sh

# Применяем миграции
python manage.py migrate --noinput

# Загружаем данные из файла data.json
python manage.py loaddata data.json

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем сервер
python manage.py runserver --noreload 0.0.0.0:8000