# Candlestick Pattern Scanner

This python web-app accesses price data from the start of the year up to present day for companies in the S&P 500 to find and display Japanese candlestick patterns from [this book](https://www.amazon.com/Japanese-Candlestick-Charting-Techniques-Second/dp/0735201811) in a web browser. Choose from 60+ patterns, and all companies who've exhibited this pattern in their price data in the last available day in the data will populate the screen.

![](https://i.imgur.com/ngoXfeM.gif)


To use: 

1. Install requirements
```console
$ pip3 install -r requirements.txt
```
2. Create sub-directory "datasets"
3. Run the flask app
```console 
$ flask run
```
4. Use the tool and find tomorrow's plays!
