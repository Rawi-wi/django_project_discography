from django.urls import path
from songs import views

app_name = 'songs'

urlpatterns = [
    path('', views.songs_list, name='list'),
    path('create/', views.songs_create, name='create'),
    path('<int:pk>/', views.songs_detail, name='detail'),
    path('<int:pk>/edit/', views.songs_edit, name='edit'),
    path('<int:pk>/delete/', views.songs_delete, name='delete'),
]