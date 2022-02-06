import os

import requests

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY', '')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')

set_webhook_url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/setWebHook?url={WEBHOOK_URL}"
try:
    requests.get(set_webhook_url)
except Exception as e:
    raise ValueError(f'Request was not successful. See {e}')
