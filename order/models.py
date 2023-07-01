from django.db import models

# Create your models here.

#出沒區域 (one habitat has many region)
#class RegionModel(models.Model):
    #!!!!!!!需要改成陣列
   ## region = models.CharField(max_length=30,null=True)
#def __str__(self):
   # return self.region

class BirdModel(models.Model):
    id = models.PositiveIntegerField(null=False,primary_key=True)
    #鳥名稱相關
    name = models.CharField(max_length=30,null=False,unique=True) # name can't empty
    familyName = models.CharField(max_length=30,null=True)
    scientificName = models.CharField(max_length=30,null=True)
    englishName = models.CharField(max_length=30,null=True)
    nickName = models.CharField(max_length=30,null=True)
    #鳥等級
    level = models.PositiveIntegerField(null=True)
    #鳥時間相關
    startMonth = models.PositiveIntegerField(null=True)
    endMonth = models.PositiveIntegerField(null=True)
    season = models.PositiveIntegerField(null=True)
    #鳥棲息地(one habitat has many region)
    #!!!!!!habitat = models.ForeignKey('RegionModel', on_delete=models.CASCADE)
    habitat = models.CharField(max_length=30,null=True)

    description = models.TextField(null=True)
    #鳥圖片相關
    image = models.ImageField(upload_to='image/',null=True)
    photoby = models.CharField(max_length=30,null=False)# photoby can't empty

def __str__(self):
    return self.name
