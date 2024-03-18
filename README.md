# StockPriceAlert

## Overview

StockPriceAlert is a Python application that monitors stock prices and sends alerts when significant price changes occur. It fetches real-time stock data using the AlphaVantage API and retrieves news articles related to specific companies using the News API. The application sends alerts via SMS using Twilio, providing users with timely information about stock price movements and relevant news articles.

## Features

- **Real-time Stock Price Monitoring:** Fetches real-time stock data using the AlphaVantage API to monitor price changes.
- **News Article Retrieval:** Retrieves news articles related to specific companies using the News API to provide additional context.
- **Alert Notifications:** Sends alert notifications via SMS using Twilio when significant price changes occur.
- **Customizable Settings:** Allows users to specify the stock symbol, company name, and threshold for price change alerts.

## Setup

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/alyssawalter/StockPriceAlert.git
```

2. **Install Dependencies:** Navigate to the project directory and install the required dependencies using pip:
```bash
cd StockPriceAlert
```
```bash
pip install -r requirements.txt
```

3. **Sign Up for APIs:**
- **AlphaVantage API:** Sign up for a free API key at [AlphaVantage](https://www.alphavantage.co/support/#api-key).
- **News API:** Obtain an API key by signing up at [News API](https://newsapi.org/register).
- **Twilio API:** Sign up for a Twilio account at [Twilio](https://www.twilio.com/try-twilio). Obtain your Account SID, Auth Token, and a Twilio phone number.

4. **Configure `config.py`:**
- Copy `config_template.py` to `config.py`.
- Replace the placeholder values in `config.py` with your API keys, Twilio credentials, and phone numbers.

5. **Run the Application:** Execute the `main.py` file to start the application:
```bash
python3 main.py
```
## File Structure

- **`main.py`:** Entry point of the application. Executes the main functionality and orchestrates the data handling and alert sending process.
- **`data_handler.py`:** Module responsible for fetching stock data from the AlphaVantage API and retrieving news articles using the News API.
- **`alert_handler.py`:** Module responsible for sending alert notifications via SMS using Twilio.
- **`config.py`:** Configuration file containing sensitive information such as API keys and phone numbers. Must be filled out with actual values before running the application.
- **`config_template.py`:** Template file for `config.py`. Contains placeholders for API keys and phone numbers.
  
## Config Template

The `config_template.py` file provides a template for storing sensitive information. Here's how to use it:

- **AlphaVantage API Key:** Replace `"YOUR_ALPHAVANTAGE_API_KEY_HERE"` with your AlphaVantage API key.
- **News API Key:** Replace `"YOUR_NEWS_API_KEY_HERE"` with your News API key.
- **Twilio Credentials:**
- **Twilio Account SID:** Replace `"YOUR_TWILIO_ACCOUNT_SID_HERE"` with your Twilio Account SID.
- **Twilio Auth Token:** Replace `"YOUR_TWILIO_AUTH_TOKEN_HERE"` with your Twilio Auth Token.
- **Twilio Phone Numbers:**
- **From Phone Number:** Replace `"YOUR_TWILIO_PHONE_NUMBER_HERE"` with your Twilio phone number.
- **To Phone Number:** Replace `"RECIPIENT_PHONE_NUMBER_HERE"` with the recipient's phone number.

## Running on PythonAnywhere

To run StockPriceAlert on PythonAnywhere and schedule it to run daily:

1. **Create a PythonAnywhere Account:** Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. **Upload Your Code:** Upload your StockPriceAlert project files to PythonAnywhere.
3. **Set Up a Scheduled Task:** Use the PythonAnywhere Dashboard to create a scheduled task that runs `main.py` daily. Ensure to set up a virtual environment and install dependencies as needed.

Now, StockPriceAlert will run automatically every day on PythonAnywhere, providing users with up-to-date stock price alerts and news.

## Contributions

Contributions are welcome!

## Licensing

This project is licensed under the [MIT License](LICENSE).
