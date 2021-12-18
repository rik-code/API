import os
import requests
from requests.exceptions import HTTPError


def translate(query: str, language: str) -> str or None:
    """
    Translates text passed through parameters from english into another language.
    :param query:  text to translate
    :param language: target language of translation
    :return: translated text
    """
    url = "https://google-translate20.p.rapidapi.com/translate"

    payload = f"text={query}&tl={language}&sl=en"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "google-translate20.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('API_KEY')
    }
    try:
        response = requests.request("POST", url, data=payload, headers=headers)
        json_response = response.json()
        return json_response['data']['translation']
    except HTTPError as http_err:
        print(f'HTTP Error occurred: {http_err}')
        return None
    except Exception as e:
        print(f'Other error occurred: {e}')
        return None