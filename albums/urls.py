from django.urls import path


from albums import views

app_name = 'albums'

urlpatterns = [
    path('', views.albums_list, name='list'),
    path('create/', views.albums_create, name='create'),
    path('<int:pk>/', views.albums_detail, name='detail' ),
    path('<int:pk>/edit/', views.albums_edit, name='edit' ),
    path('<int:pk>/delete/', views.albums_delete, name='delete' ),
]