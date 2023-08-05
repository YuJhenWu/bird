"""Ming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from order import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.test),
    path('map/',views.map),
    path('getMyloc/',views.getMyloc),
    
    ### homepage
    path('',views.index),
    
    path('TWmap/',views.TWmap),
    ### about
    path('about/', views.about),
    path('index_test/', views.index_test),

    ### birdlist 
    path('birdlist/', views.birdlist), 
    path('birdinfo/<int:sortType>/', views.birdinfo),

    ### guide 
    path('guide/', views.guide),
    path('basicKnowledge/', views.basicKnowledge),
    path('development/', views.development),
    path('equipment/', views.equipment),
    path('ethics/', views.ethics),
    
    ### realtime
    path('realtime/', views.realtime),
    path('info/', views.info),
    path('place/', views.place),
    path('recommend/', views.recommend),

    #### database
    path('order/', views.order),
    path('upload_img/', views.upload_img),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
