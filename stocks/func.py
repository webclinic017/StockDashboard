import pandas as pd
from .models import Stock

def saveSP500():
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    df.to_csv('SP500.csv')

def loadSP500():
    df = pd.read_csv('SP500.csv')
    ticker = df['Symbol'].tolist()
    company = df['Security'].tolist()
    return ticker,company