from re import search
from django.shortcuts import redirect, render
from matplotlib.pyplot import get
#import pdb; pdb.set_trace()

from listItems.models import Search, SearchField
from listItems.views import handleAdd

from stocks.func import loadSP500, validateInput

stock_limit = 10
# Create your views here.
def index(request):
    ticker,company = loadSP500()
    isValid = True
    searchResult = Search.objects.all()
    searchInfo = SearchField.objects.first()

    if request.method == 'POST':
        input = request.POST['searchBar']
        isValid,convertedTicker = validateInput(input,ticker,company)
        if isValid and searchInfo.count<stock_limit:
            new_item = Search(
                query = convertedTicker
            )
            new_item.save()
            searchInfo.validity = True
            searchInfo.count+=1
        else:
            searchInfo.validity = False
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
    s = Search.objects.get(id=pk)
    s.delete()

    searchInfo = SearchField.objects.first()
    searchInfo.count-=1
    searchInfo.validity = True
    searchInfo.save()

    return redirect('/')