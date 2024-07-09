from . import views
from django.urls import path

app_name = 'login_signup'
urlpatterns = [path("", views.index, name='index'),
                path("login", views.login, name='login'),
                path("signup", views.signup, name='signup'),
                path('dashboard', views.dashboard, name='dashboard')]