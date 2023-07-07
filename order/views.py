from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render
from django.http import HttpResponse
from order.models import BirdModel
# Create your views here.

### homepage
def index(request):
    BirdModel.objects.all()
    return render(request,'index.html',locals())

#### about
def aboutus(request):
    return render(request,'about/aboutus.html')

def contactus(request):
    return render(request,'about/contactus.html')

#### birdlist
def birdlist(request):
    return render(request,'birdlist/birdlist.html')

def birdinfo(request, sortType):
    birds = [
        {'COMMONNAME' : 'duck',
        'SCIENTIFICNAME':'小水鴨',
        'COUNTY':'台北',
        'LOCALITY':'輔仁大學中美堂',
        'LOCALITYTYPE':'校園',
        'LATITUDE':'121.43219692276416',
        'LONGITUDE':'25.038967086993015'},

        {'COMMONNAME' : 'duck22',
        'SCIENTIFICNAME':'小水鴨22',
        'COUNTY':'台北22',
        'LOCALITY':'輔仁大學中美堂22',
        'LOCALITYTYPE':'校園22',
        'LATITUDE':'121.43219692276416',
        'LONGITUDE':'25.038967086993015'},]
    return render(request,'birdlist/birdinfo.html', locals())

### guide 
def guide(request):
    return render(request,'guide/guide.html')

def basicKnowledge(request):
    return render(request,'guide/basicKnowledge.html')

def development(request):
    return render(request,'guide/development.html')

def equipment(request):
    return render(request,'guide/equipment.html')

def ethics(request):
    return render(request,'guide/ethics.html')

### realtime
def realtime(request):
    return render(request,'realtime/realtime.html')

def info(request):
    return render(request,'realtime/info.html')

def place(request):
    return render(request,'realtime/place.html')

def recommend(request):
    return render(request,'realtime/recommend.html')


### database
def order(request):
    if request.method == "POST":
        #鳥名稱相關
        name= request.POST['name']
        familyName  = request.POST['familyName']
        englishName  = request.POST['englishName']
        nickName  = request.POST['nickName']
        #鳥等級
        level  = request.POST['level']
        #鳥時間相關
        startMonth  = request.POST['startMonth']
        endMonth  = request.POST['endMonth']
        season  = request.POST['season']
        #鳥棲息地
        habitat  = request.POST['habitat']
        #鳥描述
        description  = request.POST['description']
        #鳥圖片相關
        
        image  = request.POST['image']
        photoby  = request.POST['photoby']

        unit = BirdModel.objects.create( 
            name=name,
            familyName=familyName,
            englishName=englishName,
            nickName=nickName,

            level=level,

            startMonth=startMonth,
            endMonth=endMonth,
            season=season,

            habitat=habitat,

            description=description,

            image=image,
            photoby=photoby
            )
        unit.save()  
    return render(request,'order.html',locals())



