from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Articles.views import Home, CreateBlog, aticle_details, liked, unlike

app_name='Articles'
urlpatterns = [
    path("", Home, name="Home"),
    path("create_blog/", CreateBlog.as_view(), name="Create_Blog"),
    path("aticle_details/<str:slug>/", aticle_details, name="aticle_details"),
    path("liked/<int:pk>/", liked, name="liked"),
    path("unlike/<int:pk>/", unlike, name="unlike"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

