import os

TOKEN = os.environ.get('TOKEN', '')
if not TOKEN:
    raise ValueError('TOKEN is not set')

DB_NAME = os.environ.get('DB_NAME', '')
if not DB_NAME:
    raise ValueError('DB_NAME is not set')

DB_USER = os.environ.get('DB_USER', '')
if not DB_USER:
    raise ValueError('DB_USER is not set')

DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
if not DB_PASSWORD:
    raise ValueError('DB_PASSWORD is not set')

DB_HOST = os.environ.get('DB_HOST', '')
if not DB_HOST:
    raise ValueError('DB_HOST is not set')

DB_PORT = os.environ.get('DB_PORT', '')
if not DB_PORT:
    raise ValueError('DB_PORT is not set')

SETTINGS_ADMINS_ID = [int(i) for i in os.environ.get(
    'SETTINGS_ADMINS_ID', "").split(",")]

SETTINGS_BOT_USERNAME = os.environ.get('SETTINGS_BOT_USERNAME', '')
if not SETTINGS_BOT_USERNAME:
    raise ValueError('SETTINGS_BOT_USERNAME is not set')
