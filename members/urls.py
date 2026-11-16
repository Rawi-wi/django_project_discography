from django.urls import path
from members import views

app_name = 'members'

urlpatterns = [
    path('', views.members_list, name='list'),
    path('create/', views.members_create, name='create'),
    path('<int:pk>/', views.members_detail, name='detail'),
    path('<int:pk>/edit/', views.members_edit, name='edit'),
]
