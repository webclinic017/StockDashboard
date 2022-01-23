from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    #custom startup code
    def ready(self) -> None:
        #return super().ready()
        from listItems.models import SearchField
        from stocks.models import Stock
        from stocks.func import loadSP500, validateInput

        symbols = ['FB','AAPL','AMZN','NFLX','GOOGL']

        Stock.objects.all().delete()
        for i in range(len(symbols)):
            tickers,companies = loadSP500()
            convertedTicker,convertedCompany = validateInput(symbols[i],tickers,companies)[1:3]
            s = Stock(
                ticker = convertedTicker,
                company = convertedCompany
            )
            s.save()

        SearchField.objects.all().delete()
        SearchField(count=len(symbols)).save()