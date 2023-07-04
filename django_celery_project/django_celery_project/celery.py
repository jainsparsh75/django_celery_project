from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

# to disable Universal time
app.conf.enable_utc = False

# to set indian time
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
# celery beat to schedule static tasks
# static scheduling of tasks
app.conf.beat_schedule = {
    # 'send-mail-every-day': {
    #     'task': 'mainapp.tasks.send_mail_func',
    #     'schedule': crontab(hour=14, minute=37),
    # }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
