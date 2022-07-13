from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("take", views.record_attendance, name='recordattendance'),
    path("view", views.view_attendance, name='viewattendance'),
    path("search", views.search_attendance, name='search-attendance'),
    path("signup", views.user_signup, name='signup'),
    path("login", views.user_login, name='login'),
    path("logout", views.user_logout, name='logout'),

]
