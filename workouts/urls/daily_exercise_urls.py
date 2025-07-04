from django.urls import path
from workouts.views import daily_exercise_views as views

urlpatterns = [
    path('create/', views.DailyExerciseCreateView.as_view(), name='daily_exercise_create'),
    path('d<int:pk>/', views.DailyExerciseDetailView.as_view(), name='daily_exercise_detail'),
    path('<int:pk>/update/', views.DailyExerciseUpdateView.as_view(), name='daily_exercise_update'),
    path('<int:pk>/delete/', views.DailyExerciseDeleteView.as_view(), name='daily_exercise_delete'),
]
