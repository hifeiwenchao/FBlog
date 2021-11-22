from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.conf import settings
import pymysql


UserModel = get_user_model()


class Command(BaseCommand):
    help = 'init fblog database'

    def handle(self, *args, **options):
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        port = settings.DATABASES['default']['PORT']
        name = settings.DATABASES['default']['NAME']
        conn = pymysql.connect(user=user, password=password, host=host, port=int(port))
        try:
            cursor = conn.cursor()

            if settings.DEBUG:
                clean = input(f'Clean the database {name}? [y/N]:') or 'N'
                if clean.upper() == 'Y':
                    cursor.execute(f'DROP DATABASE IF EXISTS {name}')
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {name}  DEFAULT CHARSET utf8mb4')
            conn.commit()
        finally:
            conn.close()
        call_command('migrate')
        call_command('createsuperuser')
        self.stdout.write(self.style.SUCCESS('init Successfully'))
