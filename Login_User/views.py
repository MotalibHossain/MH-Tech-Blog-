from django.shortcuts import redirect, render, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from Login_User.models import UserProfile
from Articles.models import Blog, comment
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        valid_User=authenticate(request, username=username, password=password)

        if valid_User is not None:
            auth_login(request, valid_User)
            return redirect(reverse_lazy("Articles:Home"))
        else:
            contex={"message":"Wrong informations", "class":"alert alert-warning alert-dismissible fade show"}
            return render(request, 'Login_user/login.html', contex)

    return render(request, 'Login_User/login.html')


def registrations(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=" "
        address=" "
        bio=f"I am {username}."

        check_email=User.objects.filter(email=email).first()

        if check_email:
            contex={"message":"User alrady exits", "class":"alert alert-warning alert-dismissible fade show"}
            return render(request, 'Login_user/registrations.html', contex)
        
        user=User.objects.create_user(username=username, email=email, password=password)
        profile=UserProfile(user=user,phone=phone, address=address, bio=bio)
        profile.save()

        valid_User=authenticate(request, username=username, password=password)

        if valid_User is not None:
            auth_login(request, valid_User)
            return redirect(reverse_lazy("Articles:Home"))
        else:
            return HttpResponse("Ragistrations fail")

    return render(request, 'Login_user/registrations.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("Articles:Home"))


def Profile(request, username):
    user_info=get_list_or_404(User, username=username)
    posted_articles=Blog.objects.filter(author=request.user)
    
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)


    context={"user_info":user_info, "user_profile_info":user_profile_info, "posted_articles":posted_articles}
    return render(request, 'Login_user/profile.html',context)


def Update_Profile(request, username):
    user_info=get_list_or_404(User, username=username)
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)
        
    context={"user_info":user_info, "user_profile_info":user_profile_info}
    return render(request, 'Login_user/UpdateProfile.html',context)


def update_user(request,username):
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)
        user_profile_info_id=user_profile_info.id
        print(user_profile_info_id)

    if request.method=="POST":
        username=request.POST.get("username")
        phone=request.POST.get("phone")
        bio=request.POST.get("bio")
        address=request.POST.get("address")

        user=User.objects.filter(id=user_id).update(username=username)
        UserProfile.objects.filter(pk=user_profile_info_id).update(phone=phone, bio=bio, address=address)
        return HttpResponseRedirect(reverse('Login_User:Profile', kwargs={'username':username}))
    
    return render(request, 'Login_user/UpdateProfile.html')

# def EditBlog(request,pk):
#     post=Blog.objects.filter(pk=pk)
#     # print(post.title)

#     context={"post":post}
#     return render(request, 'Articles/edit_blog.html', context)


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model=Blog
    template_name='Articles/edit_blog.html'
    fields=('title','blog_content','blog_image')

    def get_success_url(self, **kwargs):
        return reverse_lazy("Articles:aticle_details", kwargs={'slug':self.object.slug})


def delete_blog(request,pk):
    post=Blog.objects.filter(pk=pk)

    for i in post:
        author=i.author

    user=request.user
    if author== user:
        post.delete()
        return HttpResponseRedirect(reverse('Login_User:Profile', kwargs={'username':user.username}))
    else:
        message="You can't delete this post. Because you are not author this post."
        return render(request, 'Login_user/profile.html', {"message":message})
        # return HttpResponseRedirect(reverse('Login_User:Profile', kwargs={'username':user.username}))
