from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Book(models.Model):
    googleApiID = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    pageCount = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=255, null=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="the related user")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="the related book")
