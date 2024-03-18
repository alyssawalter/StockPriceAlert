import requests
from datetime import datetime, timedelta
from config import ALPHAVANTAGE_API_KEY, NEWS_API_KEY


def get_date_range():
    today = datetime.now().date()

    # If today is Monday, retrieve data for the most recent trading day (Friday)
    if today.weekday() == 0:  # Monday
        yesterday = str(today - timedelta(days=3))  # Subtract 3 days to get data for Friday
        day_before_yesterday = str(today - timedelta(days=4))
    else:
        yesterday = str(today - timedelta(days=1))
        day_before_yesterday = str(today - timedelta(days=2))

    return today, yesterday, day_before_yesterday


def get_stock_data(stock_symbol):
    if not ALPHAVANTAGE_API_KEY:
        raise ValueError("ALPHAVANTAGE_API_KEY is not set")

    today, yesterday, day_before_yesterday = get_date_range()

    alphavantage_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "outputsize": "compact",  # contains last 100 days, starting with yesterday
        "datatype": "json",
        "apikey": ALPHAVANTAGE_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=alphavantage_parameters)
    sp_data = response.json()

    # Check if the required keys exist before accessing them
    if 'Time Series (Daily)' in sp_data and yesterday in sp_data['Time Series (Daily)']:
        yesterday_price = float(sp_data['Time Series (Daily)'][yesterday]['4. close'])
    else:
        yesterday_price = None

    if 'Time Series (Daily)' in sp_data and day_before_yesterday in sp_data['Time Series (Daily)']:
        day_before_yesterday_price = float(sp_data['Time Series (Daily)'][day_before_yesterday]['4. close'])
    else:
        day_before_yesterday_price = None

    price_change = (yesterday_price - 100) / yesterday_price

    return price_change


def get_news(company_name):
    today, _, day_before_yesterday = get_date_range()

    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": company_name,
        "from": day_before_yesterday,
        "to": str(today),
        "language": "en",
        "sortBy": "popularity",
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = response.json()
    articles = news_data['articles'][:3]

    return articles
