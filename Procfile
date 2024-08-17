release: python manage.py migrate
web: python manage.py collectstatic && gunicorn faproscraper.wsgi