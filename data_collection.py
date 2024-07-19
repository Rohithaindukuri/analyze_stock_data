import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_historical_data(ticker):
    data = yf.Ticker(ticker)
    historical_data = data.history(period="5y")
    return historical_data

def fetch_financial_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    financial_data = pd.read_html(str(tables[0]))[0]
    return financial_data

# Example usage:
ticker = 'AAPL'
historical_data = fetch_historical_data(ticker)
historical_data.to_csv('historical_data.csv')

url = 'https://finance.yahoo.com/quote/AAPL/financials'
financial_data = fetch_financial_data(url)
financial_data.to_csv('financial_data.csv')
