from django.urls import path
from workouts.views import daily_exercise_views as views

urlpatterns = [
    path('<slug:slug>/', views.DailyExerciseDetailView.as_view(), name='daily_exercise_detail'),
    path('<slug:slug>/update/', views.DailyExerciseUpdateView.as_view(), name='daily_exercise_update'),
    path('<slug:slug>/delete/', views.DailyExerciseDeleteView.as_view(), name='daily_exercise_delete'),
]
