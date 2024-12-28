from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users_view, name="users"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<int:pk>/", views.edit_user, name="edit_user"),
    path("logout/", views.logout_view, name="logout"), 
    path("profile/", views.profile_view, name="profile"), 
]