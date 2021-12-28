from django.urls import path, include
from Login_User.views import login, registrations, Profile

app_name="Login_User"
urlpatterns = [
    path("login/", login, name="login"),  
    path("registrations/", registrations, name="registrations"),  
    path("profile/", Profile, name="Profile"),  
]
