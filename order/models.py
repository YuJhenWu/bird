from django.db import models

class BirdModel(models.Model):
    #id = models.PositiveIntegerField(null=False,primary_key=True)
    #鳥名稱相關
    name = models.CharField(max_length=30,null=False,unique=True) # name can't empty
    familyName = models.CharField(max_length=30,blank=True)
    scientificName = models.CharField(max_length=30,blank=True)
    englishName = models.CharField(max_length=30,blank=True)
    nickName = models.CharField(max_length=30,blank=True)
    #鳥等級
    level = models.CharField(max_length=30,blank=True)
    #鳥時間相關
    startMonth = models.CharField(max_length=30,blank=True)
    endMonth = models.CharField(max_length=30,blank=True)
    season = models.CharField(max_length=30,blank=True)
    #鳥棲息地
    habitat = models.TextField(blank=True)
    description = models.TextField(blank=True)
    #鳥圖片相關
    image = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos',null = True)
    photoby = models.TextField(blank=True)

def __str__(self):
    return self.name
