from django.urls import path
from . import views

urlpatterns = [
    path("", views.samples, name="samples"),
    path("add_sample/", views.add_edit_sample, name="add_sample"),
    path("edit_samples/<int:pk>/", views.add_edit_sample, name="edit_samples"),
    path("species/", views.species, name="species"),
    path("add_species/", views.add_edit_species, name="add_species"),
    path("edit_species/<int:pk>/", views.add_edit_species, name="edit_species"),
]