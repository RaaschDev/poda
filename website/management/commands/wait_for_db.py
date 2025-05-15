import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import psycopg2
from django.conf import settings
import os

class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        max_retries = 30  # 30 segundos de timeout
        retry_count = 0

        while not db_conn and retry_count < max_retries:
            try:
                # Print connection parameters for debugging
                self.stdout.write(f"""
                Attempting to connect to database with:
                - Host: {settings.DATABASES['default']['HOST']}
                - Port: {settings.DATABASES['default']['PORT']}
                - Database: {settings.DATABASES['default']['NAME']}
                - User: {settings.DATABASES['default']['USER']}
                """)

                # Try to connect using psycopg2 directly
                conn = psycopg2.connect(
                    dbname=settings.DATABASES['default']['NAME'],
                    user=settings.DATABASES['default']['USER'],
                    password=settings.DATABASES['default']['PASSWORD'],
                    host=settings.DATABASES['default']['HOST'],
                    port=settings.DATABASES['default']['PORT']
                )
                conn.close()
                db_conn = connections['default']
                self.stdout.write(self.style.SUCCESS('Database available!'))
                return
            except (OperationalError, psycopg2.OperationalError) as e:
                retry_count += 1
                self.stdout.write(f'Database unavailable, waiting 1 second... (Attempt {retry_count}/{max_retries})')
                self.stdout.write(f'Error: {str(e)}')
                time.sleep(1)

        self.stdout.write(self.style.ERROR(f'Could not connect to database after {max_retries} attempts'))
        raise Exception('Database connection failed') 