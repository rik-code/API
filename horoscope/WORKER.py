import json
from functions.gapi import translate
from functions.aztro_api import fetch_horoscope

lang = input('На каком языке вам нужен гороскоп? (es|fr|en|de|am|it|ru|zh)').lower()  # привожу в нижний регистр
sign = input('Введите свой знак зодиака: ').lower()  # привожу в нижний регистр
day = input('На какой день нужен гороскоп? (вчера|сегодня|завтра)').lower()

horo = fetch_horoscope(sign, day)
translation = translate(horo, lang)

if __name__ == '__main__':
    with open('results/res_it.json', 'w') as f:
        f.write(json.dumps(translation, ensure_ascii=False))
    print(translation)