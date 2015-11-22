import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dd3.dd3.settings')
from datetime import datetime

import django

print(django.get_version())

from dd3.visitor.models import Apache

import pytz

def add_apache_logs():
	apache = Apache()
	apache.date = datetime.now().replace(tzinfo=pytz.utc)
	apache.visit = 44
	apache.save()

add_apache_logs()	
