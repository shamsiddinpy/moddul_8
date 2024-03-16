# myapp/management/commands/send_product_notification.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import datetime


class Command(BaseCommand):
    help = '8:00 da barcha foydalanuvchilarga mahsulot haqida bildirishnoma yuboring'

    def handle(self, *args, **kwargs):
        now = datetime.now()
        if now.hour == 8 and now.minute == 0:
            users = User.objects.all()
            message = "Bugun biz yangi mahsulotlarni qo'shdik!"
            for user in users:
                send_mail('Yangi mahsulotlar haqida bildirishnoma', message, 'shamsiddinpython215@gmail.com',
                          [user.email])
