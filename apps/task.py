# tasks.py

from celery import shared_task
from django.core.management import call_command
from celery.schedules import crontab


@shared_task
def send_product_notification():
    call_command('send_product_notification')


CELERY_BEAT_SCHEDULE = {
    'send-product-notification': {
        'task': 'apps.message',
        'schedule': crontab(hour=8, minute=0),
    },
}
