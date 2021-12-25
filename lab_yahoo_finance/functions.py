import os
import json
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from datetime import datetime

KEY = os.environ.get('f652c1f2c284e4708669d034b02f30999cbc83d0')
HOST = os.environ.get('API_HOST')

symbol_string = ''
data = {}


def fetchStockData(symbol: str, region: str, api_key: str, api_host: str) -> dict or None:
    """
    Function connects to the API and fetch data through the query string,
    and receives data for building a chart
    :param symbol: Company index on the stock exchange (AAPL, YH, TSLA)
    :param region: Stock region US|BR|AU|DE|ES|GB
    :param api_key: Private api key (yours)
    :param api_host: API host name from rapidapi.com
    :return: body of the response in JSON format
    """
    url = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts'
    querystring = {
        'symbol': symbol.upper(),
        'interval': '5m',
        'range': '5d',
        'region': region.upper()
    }
    headers = {
        'x-rapidapi-host': api_host,
        'x-rapidapi-key': api_key
    }
    response = requests.get(url, headers=headers, params=querystring)
    json_r = json.loads(response.text)

    if response.status_code == 200:
        return json_r
    else:
        return None


def parseTimestamp(data: dict) -> list:
    """
    API returns a lot of daata for a stock symbol. All of it's formatted
    as a separate series of opening and closing, high and low figures of the stock
    during each day.
    :param data: json response
    :return: list of dates
    """
    timestamp_list = []
    timestamp_list.extend(data['chart']['result'][0]['timestamp'])
    timestamp_list.extend(data['chart']['result'][0]['timestamp'])
    calendar_time = []
    for ts in timestamp_list:
        dt = datetime.fromtimestamp(ts)
        calendar_time.append(dt.strftime('%d/%m/%Y'))
    return calendar_time


def parseValues(data: dict) -> list:
    """
    Extracting open and close values
    :param data: json response
    :return: list of values
    """
    valuesList = []
    valuesList.extend(data['chart']['result'][0]['indicators']['quote'][0]['open'])
    valuesList.extend(data['chart']['result'][0]['indicators']['quote'][0]['close'])

    return valuesList


def attachEvent(data: dict) -> list:
    """
    Defining open and close events in a list
    :param data: json response
    :return: list of open and close values
    """
    eventList = []

    for i in range(len(data['chart']['result'][0]['timestamp'])):
        eventList.append('open')
    for i in range(len(data['chart']['result'][0]['timestamp'])):
        eventList.append('close')

    return eventList


with open('yahoo.json', 'r') as j:
    o = j.read()
    o = json.loads(o)
    data['Timestamp'] = parseTimestamp(o)
    data['Values'] = parseValues(o)
    data['Events'] = attachEvent(o)
    df = pd.DataFrame(data)

    # диаграмма
    sns.set(style='darkgrid')
    rcParams['figure.figsize'] = 20, 10
    rcParams['figure.subplot.bottom'] = 0.5

    ax = sns.lineplot(x='Timestamp', y='Values', hue='Events',
                      dashes=False, markers=True, data=df, sort=False)
    ax.set_title('Symbol' + 'TSLA')
    plt.xticks(rotation=45,
               horizontalalignment='right',
               fontweight='light',
               fontsize='xx-small')
    plt.show()

#fetch = fetchStockData('TSLA', 'US', KEY, HOST)
#with open('yahoo.json', 'w') as f:
#    f.write(json.dumps(fetch, indent=4))

