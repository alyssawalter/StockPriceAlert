from config import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, FROM_PHONE_NUMBER, TO_PHONE_NUMBER
from twilio.rest import Client


def send_alert(stock_symbol, price_change_with_sym, articles):
    if not (TWILIO_AUTH_TOKEN and TWILIO_ACCOUNT_SID):
        raise ValueError("TWILIO_AUTH_TOKEN or TWILIO_ACCOUNT_SID is not set")

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']

        message = client.messages.create(
            body=f"\n{stock_symbol}: {price_change_with_sym} \n"
                 f"Title: {title}"
                 f"Description: {description} \n"
                 f"{url}",
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER,
        )

