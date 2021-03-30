from django.urls import path
from . import views

app_nme = 'csvFiles'

urlpatterns = [

        path('', views.index, name='index.html'),
        #path('index', views.index, name='index.html'),
        path('upload.html',views.hotel, name= 'upload')
]