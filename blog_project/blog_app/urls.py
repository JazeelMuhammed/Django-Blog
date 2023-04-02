from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# Importing class based views
from .views import (
    BlogPostListView, BlogPostDetailView,
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView)


urlpatterns = [
    # path('', views.home, name='home'),
    # We should convert the class based views to Normal views using as_view()
    path('', BlogPostListView.as_view(), name='blog-home'),
    # FOR DISPLAYING A SINGLE BLOGPOST
    path('blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='blog-details'),
    path('blog/new/', BlogPostCreateView.as_view(), name='blog-create'),
    path('blogpost/<int:pk>/update', BlogPostUpdateView.as_view(), name='blog-update'),
    path('blogpost/<int:pk>/delete', BlogPostDeleteView.as_view(), name='blog-delete'),
    path('myposts/', views.my_blogs, name='my-posts'),
    path('about/', views.about, name='blog-about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)