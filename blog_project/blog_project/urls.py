"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# We are importing "class based views" such as LoginView and LogoutView,
# Thus we don't want to write custom function views for login & logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # AT first url pattern checks for the project.urls and if the correct pattern founds in project.urls,
    # Then it looks for where it is pointing, Since it points to "app_name".urls, and then it looks for
    # the remaining pattern in that "app_name".urls
    path('', include('blog_app.urls')),
    # users app
    path('users/', include('users.urls')),

    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)