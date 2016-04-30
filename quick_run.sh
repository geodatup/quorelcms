source ~/myvenv/bin/activate
cd ~/Projects/quorelcms/
export DJANGO_SETTINGS_MODULE=quorelcms.settings.local
python manage.py runserver 0.0.0.0:8080
