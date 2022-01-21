from django.db import models

# Create your models here.
class Search(models.Model):
    query = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.query

class SearchField(models.Model):
    count = models.IntegerField(default=Search.objects.all().count())
    is_duplicate = models.BooleanField(default=False)
    validity = models.BooleanField(default=True)