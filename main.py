from data_handler import get_stock_data, get_news
from alert_handler import send_alert


def main():
    # Company and Stock symbol selection
    company_name = input("Enter the name of the company you want to monitor: ")
    stock_symbol = input(f"Enter the stock symbol of {company_name}: ")

    # Fetch stock data
    price_change = get_stock_data(stock_symbol)

    # Check if price change exceeds threshold
    if price_change < -0.05 or price_change > 0.05:
        if price_change < -.05:
            sym = '🔻'
        else:
            sym = '🔺'

        percent_change = f"{price_change * 100:.2f}%"
        percent_change_with_sym = sym + percent_change

        # Get news articles about stock
        articles = get_news(company_name)

        # Send alerts
        send_alert(stock_symbol, percent_change_with_sym, articles)


if __name__ == "__main__":
    main()
