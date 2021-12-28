from django.urls import path, include
from Articles.views import home

app_name='Articles'
urlpatterns = [
    path("", home, name="home"),
    
]
