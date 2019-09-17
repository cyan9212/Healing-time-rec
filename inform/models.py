from django.db import models


class Shop(models.Model):
    place = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    road_address = models.CharField(max_length=100)
    address_url = models.CharField(max_length=400)
    info_url = models.CharField(max_length=400)
    score = models.FloatField(default=0)


class Review(models.Model):
    place = models.CharField(max_length=100)
    url = models.CharField(max_length=400)
    title = models.CharField(max_length=100)
    review_title = models.CharField(max_length=200)
    review = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=True)
