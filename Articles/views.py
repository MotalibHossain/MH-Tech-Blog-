import imp
from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from Articles.models import Blog, comment, like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View
import uuid


# Create your views here.
# class Home(ListView):
#     context_object_name='blogs'
#     model=Blog
#     template_name='Article/blog_list.html'
def Home(request):
    blogs=Blog.objects.all()
    blog_titles=Blog.objects.filter(published=True).order_by("-published")[:5]
    context={"blogs":blogs,"blog_titles":blog_titles}
    return render(request, 'Articles/blog_list.html', context)

class CreateBlog(LoginRequiredMixin, CreateView):
    model=Blog
    template_name='Articles/create_blog.html'
    fields=('title','blog_content','blog_image')

    def form_valid(self, form):
        form_obj=form.save(commit=False)
        form_obj.author=self.request.user
        title=form_obj.title
        form_obj.slug=title.replace(" ", "-") +"-"+ str(uuid.uuid4())
        form_obj.save()
        return redirect(reverse_lazy('Articles:Home'))
@login_required
def aticle_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    if request.method=='POST':
        message=request.POST.get("message")
        blog=blog
        user=request.user
        print(user)
        comments=comment(user=user,blog=blog,comment=message)
        comments.save()
        return HttpResponseRedirect(reverse("Articles:aticle_details", kwargs={'slug':slug}))
        
    comments=comment.objects.all()
    already_like=like.objects.filter(blog=blog, user=request.user)
    if already_like:
        liked=True
    else:
        liked=False
    context={"blog":blog, "comments":comments, "liked":liked}
    return render(request, 'Articles/articles_details.html', context)


@login_required
def liked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=like.objects.filter(user=user, blog=blog)
    print(already_liked)
    if not already_liked:
        like_post=like(user=user, blog=blog)
        like_post.save()

    return HttpResponseRedirect(reverse("Articles:aticle_details", kwargs={'slug':blog.slug}))


@login_required
def unlike(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=like.objects.filter(user=user, blog=blog)
    already_liked.delete()
    return HttpResponseRedirect(reverse("Articles:aticle_details", kwargs={'slug':blog.slug}))
