import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, user_input):
    headers = {'Authorization': f'Bearer {token}'}
    entered_url = {'long_url': user_input}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=entered_url)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def count_clicks(token, url_netloc, url_path):
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'unit': 'day',
        'units': '-1',
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url_netloc}{url_path}/clicks/summary',
        headers=headers,
        params=params,
    )
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(token, url_netloc, url_path):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url_netloc}{url_path}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.ok


def get_parser():
    parser = argparse.ArgumentParser(description='Сreate a bitlink or count the clicks on the bitlink.')
    parser.add_argument('url', help='enter the link')
    return parser


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLINK_TOKEN']
    parser = get_parser()
    args = parser.parse_args()
    splitted_url = urlparse(args.url)
    url_netloc = splitted_url.netloc
    url_path = splitted_url.path
    try:
        if is_bitlink(token, url_netloc, url_path):
            clicks_count = count_clicks(token, url_netloc, url_path)
            print(clicks_count)
        else:
            bitlink = shorten_link(token, args.url)
            print(bitlink)
    except requests.exceptions.HTTPError as error:
        print(f'Не правильно введен адрес, ошибка: {error}')
