from django.urls import path
from workouts.views import training_day_views as views
from workouts.views.daily_exercise_views import DailyExerciseCreateView
urlpatterns = [
    path('<slug:slug>/detail/', views.TrainingDayDetailView.as_view(), name='training_day_detail'),
    path('<slug:slug>/update/', views.TrainingDayUpdateView.as_view(), name='training_day_update'),
    path('<slug:slug>/delete/', views.TrainingDayDeleteView.as_view(), name='training_day_delete'),
    path('<slug:slug>/exercise/add/', DailyExerciseCreateView.as_view(), name='exercise_add'),
]
