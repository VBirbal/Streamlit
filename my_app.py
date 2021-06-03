import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Pfizer!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'PFE'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-6-02')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

"""### Dividends"""
tickerData.actions

"""### Recommendations"""
tickerData.recommendations

""" IS IN :""" 
tickerData.isin

import plotly.graph_objects as go
old = tickerDf.reset_index()
for i in ['Open', 'High', 'Close', 'Low']: 
      old[i]  =  old[i].astype('float64')
fig = go.Figure(data=[go.Candlestick(x=old['Date'],
                                   open=old['Open'],
high=tickerDf['High'],
low=tickerDf['Low'],
close=tickerDf['Close'])])
#fig.show()

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(fig.show())