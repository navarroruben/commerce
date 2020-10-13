from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

from datetime import datetime


class User(AbstractUser):
    pass


class Listing(models.Model):
    item_name = models.CharField(max_length=32)
    starting_price = models.DecimalField(max_digits=8, decimal_places=2)
    short_desc = models.CharField(max_length=64)
    long_desc = models.TextField()
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Bid(models.Model):
    bidding_price = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(default=datetime.now())


class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.title}"
