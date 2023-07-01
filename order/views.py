from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render
from django.http import HttpResponse
from order.models import BirdModel
# Create your views here.
def page(request):
    return render(request,'page.html',locals())

def index(request):
    Bird = BirdModel.objects.all()
    return render(request,'index.html',locals())

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



