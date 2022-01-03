from django.shortcuts import redirect, render, get_list_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from Login_User.models import UserProfile
from django.contrib.auth import authenticate, login as auth_login, logout


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
    if request.user.is_authenticated:
        current_user=request.user
        user_id=current_user.id
        user_profile_info=UserProfile.objects.get(user__pk=user_id)


    context={"user_info":user_info, "user_profile_info":user_profile_info}
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
        print(current_user)
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
        return redirect(reverse_lazy('Articles:Home'))
    
    return render(request, 'Login_user/UpdateProfile.html')