from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    #custom startup code
    def ready(self) -> None:
        #return super().ready()
        from listItems.models import Search, SearchField
        Search.objects.all().delete()
        s1 = Search(query='FB')
        s1.save()
        s2 = Search(query='AAPL')
        s2.save()
        s3 = Search(query='AMZN')
        s3.save()
        s4 = Search(query='NFLX')
        s4.save()
        s5 = Search(query='GOOGL')
        s5.save()

        from stocks.func import saveSP500
        saveSP500()

        SearchField.objects.all().delete()
        SearchField().save()