from django.http import HttpResponse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from Articles.models import Blog, comment, like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View
import uuid


# Create your views here.
class Home(ListView):
    context_object_name='blogs'
    model=Blog
    template_name='Article/blog_list.html'


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
