
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Articles.urls')),
    path("User/",include('Login_User.urls')),
]
