from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Articles.views import Home, CreateBlog

app_name='Articles'
urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("create_blog/", CreateBlog.as_view(), name="Create_Blog"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

