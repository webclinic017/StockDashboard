from django.shortcuts import redirect, render
#import pdb; pdb.set_trace()

from listItems.models import Search
from listItems.views import handleAdd

# Create your views here.
def index(request):
    searchResult = Search.objects.all()
    
    handleAdd(request)

    context = {
        'to_add': searchResult
    }

    return render(request, 'main/base.html', context)

def delete(request, pk):
    s = Search.objects.get(id=pk)
    s.delete()
    return redirect('/')