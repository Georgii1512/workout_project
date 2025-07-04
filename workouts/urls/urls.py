from django.urls import path, include
from workouts.views import exercises_bank_views as bank

app_name = 'workouts'

urlpatterns = [
    path('exercises-bank/', include('workouts.urls.exercises_bank_urls')),
    path('exercise-category/', include('workouts.urls.exercise_category_urls')),
    path('exercise/', include('workouts.urls.exercise_urls')),
    path('training-plan/', include('workouts.urls.training_plan_urls')),
    path('training-day/', include('workouts.urls.training_day_urls')),
    path('daily-exercise/', include('workouts.urls.daily_exercise_urls')),

]
