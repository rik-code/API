import os
import requests
from requests.exceptions import HTTPError


def fetch_horoscope(sign: str, day: str) -> str or None:
    """
    Connects to the AZTRO API and fetches the horoscope data, then
    returns it to the user
    :param sign: horoscope sign
    :param day: day of horoscope
    :return: the prediction for a sign on a specific day
    """
    url = 'https://sameer-kumar-aztro-v1.p.rapidapi.com/'

    headers = {
        'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_KEY')
    }
    signs = {
        'овен': 'aries',
        'телец': 'taurus',
        'близнецы': 'gemini',
        'рак': 'cancer',
        'лев': 'leo',
        'дева': 'virgo',
        'весы': 'libra',
        'скорпион': 'scorpio',
        'стрелец': 'sagittarius',
        'козерог': 'capricorn',
        'водолей': 'aquarius',
        'рыбы': 'pisces',
    }
    days = {
        'вчера': 'yesterday',
        'сегодня': 'today',
        'завтра': 'tomorrow',
    }

    try:
        s = signs[sign]
        d = days[day]

        query = {'sign': s, 'day': d}
        response = requests.post(url, headers=headers, params=query)
        json_response = response.json()
        horo = json_response['description']

        return horo
    except KeyError:
        print('Вы ввели неправильный день/знак зодиака')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
