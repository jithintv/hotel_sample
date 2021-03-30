from django.db import models

class Hotel(models.Model):
    SR_NO = models.IntegerField()
    hotel_code = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    cost = models.IntegerField()
    Rating = models.FloatField()

    def __str__(self):
        return f':{self.hotel_code}'
