from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=5)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=1)
    close = models.DecimalField(max_digits=8,decimal_places=2,default=1)
    change = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    change_p = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    low_52wk = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    high_52wk = models.DecimalField(max_digits=8,decimal_places=2,default=0)