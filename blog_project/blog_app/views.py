from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import BlogPost
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

# Like the @loginrequired decorator we used.
from django.contrib.auth.mixins import LoginRequiredMixin
# We are importing another mixin to ensure that the correct user is updating the post
from django.contrib.auth.mixins import UserPassesTestMixin


def home(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, "blog/home.html", context)


# WE ARE CONVERTING THE home() view to a Class Based View
# We are using a ListView here since we are listing out the blogs.
class BlogPostListView(ListView):
    model = BlogPost
    # BY DEFAULT CLASS BASED VIEWS LOOKS FOR TEMPLATES WITH A CERTAIN NAMING PATTERN.
    # ie; "<app_name/model_<view_type>.html>". Here "view_type" is a List
    template_name = 'blog/home.html'
    # By Default ListView passes a "<list obj>" instead of {'posts': posts} to the Templates. We change that to "posts"
    context_object_name = 'posts'
    # by default ListView displays list of objects in an "oldest_post" first manner,
    # We can change this by putting a "-" sign before date attribute
    ordering = ['-date_posted']


class BlogPostDetailView(DetailView):
    model = BlogPost    # Returns a "<app_name/model_<view_type>.html>". Here "view_type" is "<detail_obj>"
    template_name = 'blog/single_blog_details.html'


# HERE COMES THE ADVANTAGE OF CLASS BASED VIEWS,ie; WE DON'T WANT TO CREATE A
# "forms.py" for "BlogCreation". All we did was tell our "CreateView" we just want to create a BlogPost model
# LIKE @loginrequired decorator we use "LoginRequiredMixin" in Class Based Views.
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content']
    success_url = '/'

    # WE ARE CHECKING VALIDATIONS IN A CLASS BASED MANNER
    def form_valid(self, form):
        # WE ARE OVERRIDING AUTHOR OF THE FORM IN PARENT CLASS
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # GETTING a SPECIFIC OBJECT using get_object() method
        blogpost = self.get_object()
        if self.request.user == blogpost.author:
            # Only allows to update if requested "user" == "author of BlogPost"
            return True
        return False


# "Login is required" and "MUST BE CORRECT USER to delete a BlogPost"
class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = '/'


    def test_func(self):
        # GETTING a SPECIFIC OBJECT using get_object() method
        blogpost = self.get_object()
        if self.request.user == blogpost.author:
            # Only allows to update if requested "user" == "author of BlogPost"
            return True
        return False


def my_blogs(request):
    my_blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_blogs.html', {'posts': my_blogs})


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})



