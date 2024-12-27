from django.urls import path
from . import views

urlpatterns = [
    path("", views.samples, name="samples"),
    path("add_sample/", views.add_edit_sample, name="add_sample"),
    path("edit_samples/<int:pk>/", views.add_edit_sample, name="edit_samples"),
    path("species/", views.species, name="species"),
    path("add_species/", views.add_edit_species, name="add_species"),
    path("edit_species/<int:pk>/", views.add_edit_species, name="edit_species"),
    path("projects/", views.projects, name="projects"),
    path("add_project/", views.add_edit_project, name="add_project"),
    path("edit_project/<int:pk>/", views.add_edit_project, name="edit_project"),
    path("sample_providers/", views.sample_provider, name="sample_providers"),
    path("add_sample_provider/", views.add_edit_sample_provider, name="add_sample_provider"),
    path("edit_sample_provider/<int:pk>/", views.add_edit_sample_provider, name="edit_sample_provider"),
]