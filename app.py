from flask import Flask, render_template
from patterns import patterns
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('index.html', patterns=patterns)

@app.route("/snap")
def snapshot():
  return "SUCCESS"