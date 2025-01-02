from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('add_category', views.add_edit_category, name='add_category'),
    path('edit_category/<int:pk>', views.add_edit_category, name='edit_category'),
    path('threads/<int:category_id>/', views.threads, name='threads'),
    path('<int:category_id>/add_thread', views.add_edit_thread, name='add_thread'),
    path('delete_threads/', views.delete_threads, name='delete_threads'),
    path('posts/<int:thread_id>', views.posts, name='posts'),
]
