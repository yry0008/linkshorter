from django.db import models
import time

# Create your models here.

class link(models.Model):
    token = models.CharField(max_length=200,default='')
    redirect = models.CharField(max_length=200,default="")
    create_time = models.IntegerField()
    del_token = models.CharField(max_length=200,default='')
    cnt = models.IntegerField(default=0)
    def addlink(self,tk,r,dk):
        self.token = tk
        self.redirect = r
        self.create_time = time.time()
        self.del_token = dk
        self.save()
        return