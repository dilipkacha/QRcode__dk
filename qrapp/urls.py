from django.urls import path
from . import views

urlpatterns = [

path('',views.home,name="home"),
path('scan/<int:id>/',views.track,name="scan")

]