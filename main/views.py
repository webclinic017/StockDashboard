from re import search
from django.shortcuts import redirect, render
from matplotlib.pyplot import get
#import pdb; pdb.set_trace()

from listItems.models import SearchField
from listItems.views import handleAdd

from stocks.models import Stock

from stocks.func import loadSP500, validateInput

stock_limit = 10
# Create your views here.
def index(request):
    ticker,company = loadSP500() # load list of ticker symbols and company names
    isValid = True
    searchResult = Stock.objects.all()
    curr_stocks = set(Stock.objects.values_list('ticker', flat=True)) # flat returned results are single values, rather than one-tuples
   
    searchInfo = SearchField.objects.first()

    if request.method == 'POST':
        input = request.POST['searchBar']
        isValid,convertedTicker,convertedCompany = validateInput(input,ticker,company)
        if isValid and searchInfo.count<stock_limit: # don't go over limit
            searchInfo.validity = True
            if convertedTicker not in curr_stocks: # no duplicate entered
                searchInfo.is_duplicate = False
                new_stock = Stock(
                    ticker = convertedTicker,
                    company = convertedCompany,
                )
                new_stock.save()
                
                searchInfo.count+=1
            else:
                searchInfo.is_duplicate = True
        else:
            searchInfo.validity = False # input not found
        searchInfo.save()

        return redirect('/') #homepage

    res = [i +' - '+j for i, j in zip(ticker, company)] #'TICKER - Company'

    context = {
        'to_add': searchResult,
        'res': res,
        'info': searchInfo,
    }

    return render(request, 'main/base.html', context)

def delete(request, pk):
    s = Stock.objects.get(id=pk)
    s.delete()

    searchInfo = SearchField.objects.first()
    searchInfo.count-=1
    searchInfo.validity = True
    searchInfo.is_duplicate = False
    searchInfo.save()

    return redirect('/')