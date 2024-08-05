"""Medicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Medicine_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('Sign_up/',views.Sign_up, name='Sign_up'),
    path('login/',views.login, name='login'),
    path('logout/',views.Logout, name='logout'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('news/',views.news, name='news'),
    path('feedback/',views.feedback, name='feedback'),
    path('search/',views.search, name='search'),
      path('forget_password/',
        auth_views.PasswordResetView.as_view(
            template_name='fp.html'
        ),
        name='password_reset'),
    path('forget_password/done/',
        auth_views.PasswordResetDoneView.as_view(
           template_name='fp_done.html'
        ),
        name='password_reset_done'),
    path('forget_password-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
           template_name='fp_confirm.html'
        ),
        name='password_reset_confirm'),
    path('forget_password-complete/done/',
        auth_views.PasswordResetCompleteView.as_view(
           template_name='fp_complete.html'
        ),
        name='password_reset_complete'),
          path('change_password/',
        auth_views.PasswordChangeView.as_view(
           template_name='cp.html'
        ),
        name='password_change'),
    path('change_password/done/',
        auth_views.PasswordChangeDoneView.as_view(
           template_name='cp_done.html'
        ),
        name='password_change_done'),
]
