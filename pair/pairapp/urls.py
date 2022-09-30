from django.urls import path
from . import views

app_name = "pairapp"

urlpatterns = [path("index/", views.index)]
