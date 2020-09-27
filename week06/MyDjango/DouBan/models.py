from django.db import models

# Create your models here.
# 图书or电影
class t1(models.Model):
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()
