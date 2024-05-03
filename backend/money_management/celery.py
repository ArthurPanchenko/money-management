import os 

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'money_management.settings')

app = Celery('money_management')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': { 
        'task': 'money.tasks.recalculate_daily',
        'schedule': crontab(minute=0, hour=0),
    }
}
