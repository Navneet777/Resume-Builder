from django.urls import path
from myapp import views

urlpatterns = [
path('',views.index,name="index"),
path('myresume/',views.myresume,name="myresume"),
path('myresume2/',views.myresume2,name="myresume2")
]
