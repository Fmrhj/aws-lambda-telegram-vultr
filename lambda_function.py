import datetime
import json
import os
from typing import Dict

import requests
from requests.structures import CaseInsensitiveDict

import constants

# Environmental variables
VULTR_API_KEY = os.environ.get('VULTR_API_KEY', '')
END_POINT = os.environ.get('END_POINT', '')
TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY', '')

for var in (TELEGRAM_API_KEY, END_POINT, VULTR_API_KEY):
    if len(var) == 0:
        raise ValueError('Environmental variables were not found')

TELEGRAM_URL = f'https://{constants.TELEGRAM_API_HOST}/bot{TELEGRAM_API_KEY}'


def get_account_details() -> Dict:
    """Gets information from VULTR API

    Returns:
        Dict: Account details
    """
    headers = CaseInsensitiveDict()
    headers['Accept'] = 'application/json'
    headers['Authorization'] = r'Bearer ' + VULTR_API_KEY
    response = requests.get(END_POINT, headers=headers)
    return response.json()


def get_charges(account_details: Dict) -> Dict:
    """Builds a response with account details Dict from Vultr

    Args:
        account_details (Dict): details from Vultr API

    Raises:
        KeyError: if a certain field can not be found

    Returns:
        Dict: charges, date and user
    """
    charges = CaseInsensitiveDict()
    now_ts = datetime.datetime.now()
    try:
        details = account_details[constants.ACCOUNT_KEY]
        charges = {
            'user': details[constants.EMAIL_KEY],
            'time': str(now_ts.strftime('%Y-%m-%d %H:%M:%S')),
            'charges': details[constants.PENDING_CHARGES_KEY],
            'balance': details[constants.BALANCE_KEY],
            'currency': 'EUR'
        }
    except:
        raise KeyError('Data could not be fetched from Vultr Costs API')

    return charges


def send_message(text: str, chat_id: int) -> None:
    """Main function to send messages to Telegram

    Args:
        text (str): Message to send
        chat_id (int): chat id from Telegram
    """
    url = f'{TELEGRAM_URL}/sendMessage?text={text}&chat_id={chat_id}&parse_mode=Markdown'
    requests.get(url)


def create_summary_message(charges: Dict) -> str:
    """Generates a summary message string"""
    return f'*Vultr* ☁ summary:\n️⏱ {charges["time"]}\n💰 {charges["charges"]} {charges["currency"]}\n🔋 {charges["balance"]}'


def lambda_handler(event, context):
    """Wrapper lambda

    Args:
        event (Dict): User input.
        context ([type]): AWS context.

    Returns:
        JSON: response with response code and headers
    """

    request_body = json.loads(event['body'])

    chat_id = request_body['message']['chat']['id']

    if 'text' not in request_body['message']:
        if 'sticker' in request_body['message']:
            send_message('😂 Lol, this is a sticker. Try again', chat_id)
        else:
            send_message('❌ This is not a text command. Try again ', chat_id)
        return json.dumps({'status_code': 200})

    command_arguments = request_body['message']['text'].split()
    command = command_arguments[0]
    arguments = command_arguments[1:]

    if command == '/costs':
        try:
            account_details = get_account_details()
            charges = get_charges(account_details)
            message = create_summary_message(charges)
            send_message(message, chat_id)
        except:
            send_message('🐛 Could not get latest charges...', chat_id)

    elif command == '/help':
        help_message = '💁🏾\n `/costs`: Gets costs from Vultr'
        send_message(help_message, chat_id)

    else:
        send_message('❌ Command is not supported ', chat_id)

    return json.dumps({'status_code': 200})
