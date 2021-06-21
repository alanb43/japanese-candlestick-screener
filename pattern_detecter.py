import talib
import yfinance as yf

'''

THIS FILE IS NOT NEEDED FOR THE REST OF THE WEB APPLICATION

'''
data = yf.download("SPY", start="2020-01-01", end="2021-06-20")

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])
moring_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

data['engulfing'] = engulfing
data['morning_star'] = moring_star

engulfing_days = data[data['engulfing'] != 0]
morning_star_days = data[data['morning_star'] != 0]

print(engulfing_days)
print(morning_star_days)