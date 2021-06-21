from flask import Flask, render_template
from patterns import patterns
import yfinance as yf
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('index.html', patterns=patterns)

@app.route("/snap")
def snapshot():
  with open('datasets/companies.csv') as f:
    companies = f.read().splitlines()
    for company in companies:
      today = date.today()
      symbol = company.split(',')[0]
      data = yf.download(symbol, start="2021-01-01", end=today)
  return "symbol"