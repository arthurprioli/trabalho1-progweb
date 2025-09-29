"""
URL configuration for listador_jogos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.urls import path
from django.urls.base import reverse_lazy
from django.urls.conf import include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jogos/', include('jogos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('seguranca/register/', views.register, name='register'),
    path('seguranca/login/', LoginView.as_view(template_name="seguranca/login.html"), name='login'),
    path('seguranca/profile/', views.UserPageView, name='user-page'),
    path('seguranca/logout/', LogoutView.as_view(
        next_page=reverse_lazy('jogos:home-jogos')
    ), name='logout'),
    path('seguranca/passwordChange/', PasswordChangeView.as_view(
        template_name="seguranca/passwordChangeForm.html",
        success_url=reverse_lazy('password-change-done')
    ), name='password-change'),
    path('seguranca/passwordChangeDone/', PasswordChangeView.as_view(
        template_name="seguranca/passwordChangeDone.html",
    ), name='password-change-done'),
    path('perfil/<int:pk>/',views.ProfileView.as_view(),name='perfil')]