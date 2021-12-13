from bs4.dammit import encoding_res
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

    def get_title(self):
        import requests
        from bs4 import BeautifulSoup
        try:
            r = requests.get(self.redirect,timeout=5,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'})
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,'html.parser')
            title = soup.title.string
        except:
            title = "No Title"
        return title