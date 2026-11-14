from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> b0cfb207362c1492d339ac1f151bad5e5698fc87
from albums import views

app_name = 'albums'

urlpatterns = [
    path('', views.albums_list, name='list'),
<<<<<<< HEAD
    path('create/', views.albums_create, name='create'),
    path('<int:pk>/', views.albums_detail, name='detail' ),
    path('<int:pk>/edit/', views.albums_edit, name='edit' ),
    path('<int:pk>/delete/', views.albums_delete, name='delete' ),
=======
>>>>>>> b0cfb207362c1492d339ac1f151bad5e5698fc87
]