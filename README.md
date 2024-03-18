# StockPriceAlert

## Overview

StockPriceAlert is a Python application that monitors stock prices and sends alerts when significant price changes occur. It fetches real-time stock data using the AlphaVantage API and retrieves news articles related to specific companies using the News API. The application sends alerts via SMS using Twilio, providing users with timely information about stock price movements and relevant news articles.

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

