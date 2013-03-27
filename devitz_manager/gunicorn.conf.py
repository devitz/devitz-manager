#!/usr/bin/python
import sys
import os
import multiprocessing

from django.conf import settings

try:
    import settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

bind = '127.0.0.1:9000'
workers = multiprocessing.cpu_count()
worker_connections = 2048
worker_class = 'egg:gunicorn#sync'
logfile = '/home/devitz/logs/gunicorn.log'