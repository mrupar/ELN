from django.urls import path
from . import views

urlpatterns = [
    path("add_user/", views.add_user_view, name="add_user"),
    path("logout/", views.logout_view, name="logout"), 
    path("profile/", views.profile_view, name="profile"), 
]