from django.urls import path
from workouts.views import exercises_bank_views as views

urlpatterns = [
    path('create/', views.ExercisesBankCreateView.as_view(), name='exercises_bank_create'),
    path('<int:pk>/', views.ExercisesBankDetailView.as_view(), name='exercises_bank_detail'),
    path('<int:pk>/update/', views.ExercisesBankUpdateView.as_view(), name='exercises_bank_update'),
    path('<int:pk>/delete/', views.ExercisesBankDeleteView.as_view(), name='exercises_bank_delete'),
    path('list/', views.ExerciseBankList.as_view(), name='exercises_bank_list')
]
