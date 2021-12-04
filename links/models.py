from django.db import models
import time

# Create your models here.

class links(models.Model):
    token = models.TextField()
    redirect = models.TextField()
    create_time = models.TimeField()
    def addlink(self,tk,r):
        self.token = tk
        self.redirect = r
        self.create_time = time.time()
        self.save()
        return