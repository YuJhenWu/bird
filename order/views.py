from contextlib import _RedirectStream, redirect_stderr

from django.shortcuts import render
from django.http import HttpResponse
from order.models import BirdModel
import json
import requests
### for test
def test(request):
    weather_msg = get_data()
    recent_msg = recent()
    if request.method == "POST":
        loc1= request.POST['loc1']
        loc2= request.POST['loc2']
        if(loc1 =="" or loc2 ==""):
            distance_msg = "error"
        elif(distance(loc1,loc2) !=  "error"):
            distance_msg = distance(loc1,loc2)
        else:
            distance_msg = "error"
    return render(request,'test.html',locals())

### homepage
def index(request):
    BirdModel.objects.all()
    weather_msg = get_data()
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
    birds = bList()
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
    birds = bList()
    recent_msg = recent()
    return render(request,'realtime/realtime.html',locals())

def info(request):
    return render(request,'realtime/info.html')

def place(request):
    return render(request,'realtime/place.html')

def recommend(request):
    return render(request,'realtime/recommend.html')

def TWmap(request):
    return render(request,'svgMap/TWmap.html')

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
### 
def TWtownship():
    place_data = ["臺北市", "新北市", "台中市", "臺南市", "高雄市", "基隆市",
                  "桃園市", "新竹市", "新竹縣", "苗栗縣", "彰化縣", "南投縣",
                  "雲林縣", "嘉義市", "嘉義縣", "屏東縣", "宜蘭縣", "花蓮縣",
                  "台東縣", "澎湖縣", "金門縣", "連江縣"]
    return place_data
###
def bList():
    blist = [
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
    return blist

#### weather_API
def get_data():
    place = TWtownship()
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWB-A38B5122-DF26-47EB-A652-1AD1A5643F5C",
        "locationName": place[5],
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
    
        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

        msg = {
            'location' : location,
            'weather_state': weather_state,
            'rain_prob':rain_prob,
            'min_tem':min_tem,
            'comfort':comfort,
            'max_tem':max_tem}
        
    return msg 
### ebird_API
def recent():
    regionCode = 'TW'
    url = "https://api.ebird.org/v2/data/obs/"+regionCode+"/recent"

    payload={}
    headers = {
    'X-eBirdApiToken': 'ihe647qob150'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    json_to_dict_ebird = json.loads(response.text)

    #print(json_to_dict)
    recent_datas = json_to_dict_ebird
    
    return recent_datas

### google_API
def distance(loc1,loc2): 
    params = {
        'key':'AIzaSyDJCPBc_-meh9F9V3iSXKsHelmBOQeJ7aY',
        'origins': loc1,
        'destinations': loc2,
        'mode': 'driving'} # mode: walking , driving , bicycling , transit

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?&libraries=places,drawing,geometry&v=3&callback=initMap"'
    response = requests.get(url, params=params)

    print(response.text)
    json_to_dict_google = json.loads(response.text)
    
    print(json_to_dict_google)
    errorMSG = "error"
    distance_data = {
        #'destination_addresses' : json_to_dict_google['destination_addresses'][0], 
        #'origin_addresses' : json_to_dict_google['origin_addresses'][0],
        'destination_addresses' : loc1, 
        'origin_addresses' : loc2,
        'distance' : json_to_dict_google['rows'][0]['elements'][0]['distance']['text'],
        'duration': json_to_dict_google['rows'][0]['elements'][0]['duration']['text']}

    if(json_to_dict_google['status'] == "OK" and json_to_dict_google['rows'][0]['elements'][0]['status'] == "OK"):
        return distance_data
    else:
        return errorMSG
