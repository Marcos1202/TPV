
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="bases"

urlpatterns = [
    path('', 
        views.Home.as_view(),
        name = "base"),
    path('login/',
        auth_views.LoginView.as_view(template_name='bases/login.html'),
        name= 'login'
    ),
    path('logout/',
        auth_views.LogoutView.as_view(template_name='bases/login.html'),
        name= 'logout'
    ),
    
]
