import os
import django
from django.conf import settings

# CONFIG TO DJANTO TESTS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')


def pytest_configure():
    settings.DEBUG = False
    django.setup()