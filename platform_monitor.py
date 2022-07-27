import requests
from requests import exceptions as  req_exc

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import logging

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = "Current Time = " + current_time
    return data


format_string = '%(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename="platform_script.log", format=format_string)


def telegram_bot_sendtext(bot_message):

    bot_token = '<BOT TOKEN ID>'
    bot_chatID = '<BOT CHAT IP>'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

for url in ['https://google.com/', https://medium.com]:
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        # if response are successful , no exception is raised
    except req_exc.HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
        error_message = "Checked URL: {} has an issue: {}.".format(url, http_error)
        telegram_bot_sendtext(str(error_message))
        logging.error(str(error_message))

    except req_exc.ConnectionError as connection_error:
        print(f'Connection error occured: {connection_error}')
        error_message = "Checked URL: {} has an issue: {}.".format(url, connection_error)
        telegram_bot_sendtext(str(error_message))
        logging.error(str(error_message))

    else:
        print("Success!")
        #telegram_bot_sendtext("Link is UP and accessible..")
        logging.info("ALL link accessible")
