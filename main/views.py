from django.shortcuts import redirect, render
from matplotlib.pyplot import get
#import pdb; pdb.set_trace()

from listItems.models import Search
from listItems.views import handleAdd

from stocks.func import loadSP500

# Create your views here.
def index(request):
    searchResult = Search.objects.all()
    if request.method == 'POST':
        new_item = Search(
            query = request.POST['searchBar']
        )
        new_item.save()
        return redirect('/') #homepage

    ticker,company = loadSP500()
    res = [i +' - '+j for i, j in zip(ticker, company)]
    context = {
        'to_add': searchResult,
        'tickers': ticker,
        'companies': company,
        'res': res,
    }

    return render(request, 'main/base.html', context)

def delete(request, pk):
    s = Search.objects.get(id=pk)
    s.delete()
    return redirect('/')