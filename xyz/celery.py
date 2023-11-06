import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xyz.settings')

app = Celery('xyz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()