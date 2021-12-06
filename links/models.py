from django.db import models
import time

# Create your models here.

class link(models.Model):
    token = models.CharField(max_length=200)
    redirect = models.CharField(max_length=200)
    create_time = models.IntegerField()
    def addlink(self,tk,r):
        self.token = tk
        self.redirect = r
        self.create_time = time.time()
        self.save()
        return