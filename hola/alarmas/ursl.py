from django.urls import path
from .import views

app_name='alarmas'

urlpatterns = [
    path("", views.index, name="index"),
    path("v2", views.v2, name="v2"),
     ]