import yfinance as yf
import pandas as pd
import datetime

def get_daily_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def get_spy_daily_historical(start_date, end_date):
    data = get_daily_stock_data('SPY', start_date, end_date)
    return data

if __name__ == '__main__':
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)
    data = get_spy_daily_historical(start_date, end_date)
    print(data.head())
    print(data.tail())
    data.to_csv('spy_daily_historical.csv')