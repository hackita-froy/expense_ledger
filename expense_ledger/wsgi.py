"""
WSGI config for expense_ledger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/media/temp/python_projects/hackita/expense_ledger')
sys.path.append('/media/temp/python_projects/hackita/expense_ledger/expense_ledger')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense_ledger.settings")

application = get_wsgi_application()
