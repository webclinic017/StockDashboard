from alpaca_trade_api.stream import Stream
from alpaca_trade_api.rest import REST,  TimeFrame
from decouple import config

API_KEY = config('APCA_API_KEY_ID')
API_SECRET = config('APCA_API_SECRET_KEY')
APCA_API_BASE_URL = config('APCA_API_BASE_URL')

api = REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2')
stream = Stream(API_KEY,
                API_SECRET,
                base_url=APCA_API_BASE_URL,
                data_feed='iex')

def getBars(symbol,start,end):
    bar_iter = api.get_bars_iter(symbol, TimeFrame.Hour, start, end, adjustment='raw')
    return bar_iter

def isOpen():
    return api.get_clock().is_open

def getQuote(symbol):
    return api.get_last_quote(symbol)

def getLastClose(symbol):
    bar = api.get_barset(symbol,limit=1,timeframe='minute')
    return bar[symbol][0].c