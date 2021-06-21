from flask import Flask, render_template, request
from patterns import patterns
import yfinance as yf
from datetime import date
import talib
import pandas as pd
import os, csv

app = Flask(__name__)


DAILY_DATA_PATH = 'datasets/daily/'

@app.route("/")
def main():
  pattern = request.args.get('pattern', None)
  stocks = {}
  with open('datasets/companies.csv') as f:
    for row in csv.reader(f):
      stocks[row[0]] = {'company': row[1]}

  if pattern:
    data_files = os.listdir(DAILY_DATA_PATH)
    for dataset in data_files:
      symbol = dataset.split('.')[0]
      df = pd.read_csv(f'{DAILY_DATA_PATH}{dataset}')
      pattern_func = getattr(talib, pattern)
      result = pattern_func(df['Open'], df['High'], df['Low'], df['Close'])
      last = result.tail(1).values[0]
      if last > 0:
        stocks[symbol][pattern] = 'bullish'
      elif last < 0:
        stocks[symbol][pattern] = 'bearish'
      else:
        stocks[symbol][pattern] = None

  return render_template('index.html', patterns=patterns, stocks=stocks)

@app.route("/snap")
def capture_data():
  with open('datasets/companies.csv') as f:
    companies = f.read().splitlines()
    for company in companies:
      today = date.today()
      symbol = company.split(',')[0]
      data = yf.download(symbol, start="2021-01-01", end=today)
      if len(data.index) > 10: #incase symbol has been delisted
        data.to_csv(f'{DAILY_DATA_PATH}{symbol}.csv')
  return