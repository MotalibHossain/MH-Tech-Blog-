from django.urls import path, include
from Login_User.views import login, registrations, Profile,logout_view,Update_Profile,update_user, UpdateBlog, delete_blog

app_name="Login_User"
urlpatterns = [
    path("login/", login, name="login"),  
    path("registrations/", registrations, name="registrations"),  
    path("logout_view/", logout_view, name="logout_view"),  
    path('profile/<str:username>', Profile, name="Profile"),  
    path('Update_Profile/<str:username>', Update_Profile, name="Update_Profile"),  
    path('update_user/<str:username>', update_user, name="update_user"),
    # path('edit_blog/<pk>', EditBlog, name="EditBlog"),
    path('edit_blog/<pk>', UpdateBlog.as_view(), name="EditBlog"),
    path('delete_blog/<pk>', delete_blog, name="delete_blog"),

]
