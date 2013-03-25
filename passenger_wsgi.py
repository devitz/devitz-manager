import os
import sys

INTERP = os.path.join(os.environ['HOME'], '.virtualenvs', 'devitz_manager', 'bin', 'python')

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(1, os.getcwd())
sys.path.insert(1, os.path.join(os.getcwd(), 'devitz_manager'))


from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'devitz_manager.settings'

application = get_wsgi_application()