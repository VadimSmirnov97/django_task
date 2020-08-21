import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_task.settings')

app = Celery('django_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
