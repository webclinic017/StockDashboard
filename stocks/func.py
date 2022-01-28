import pandas as pd
from .models import Stock
from bisect import bisect_left
import yfinance as yf

def saveSP500():
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    df.to_csv('SP500.csv')

def loadSP500():
    df = pd.read_csv('SP500.csv')
    ticker = df['Symbol'].tolist()
    company = df['Security'].tolist()
    return ticker,company

def validateInput(input,ticker,company):
    #company list should be alphabetized, ticker not necessarily
    isValid = False
    convertedTicker = "N/A"
    convertedCompany = "N/A"

    if input.upper() in ticker:
        isValid = True
        convertedTicker = input.upper()
        convertedCompany = company[ticker.index(input.upper())]
    elif input.title() in company: #captalize first letter of each word
        isValid = True
        convertedCompany = input.title()
        convertedTicker = ticker[company.index(input.title())]
    
    return isValid, convertedTicker, convertedCompany 
    
def getYF_data(symbol):
    df = yf.download(symbol, period="1y", auto_adjust=True, prepost=True, threads=True, progress=False)
    low = df['Low'].min()
    high = df['High'].max()
    open = df['Open'][-1]
    close = df['Close'][-1]
    return low, high, open, close