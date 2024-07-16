from django.db import models


class Txn(models.Model):
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    user_category = models.CharField(max_length=200, default=None)
    user_subcategory = models.CharField(max_length=200, default=None)
    type = models.CharField(max_length=200)
    amount = models.FloatField()
    memo = models.CharField(max_length=200)
    post_date = models.DateTimeField("date posted")
    txn_date = models.DateTimeField("date created")
