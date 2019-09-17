import os
import sys

sys.path.append('/home/ubuntu/chatbot')
sys.path.append('/home/ubuntu/chatbot/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot.settings')

application = get_wsgi_application()
