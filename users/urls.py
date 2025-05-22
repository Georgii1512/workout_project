from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('users-list/', views.UsersListView.as_view(), name='users_list'),
    path('user-update/<str:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('user-detail/<str:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('register/', views.UserCreateView.as_view(), name='user_register')
]
