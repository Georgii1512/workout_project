from django.urls import path, include

app_name = 'workouts'

urlpatterns = [
    path('exercises-bank/', include('workouts.workout_urls.exercises_bank_urls')),
    path('exercise-category/', include('workouts.workout_urls.exercise_category_urls')),
    path('exercise/', include('workouts.workout_urls.exercise_urls')),
    path('training-plan/', include('workouts.workout_urls.training_plan_urls')),
    path('training-day/', include('workouts.workout_urls.training_day_urls')),
    path('daily-exercise/', include('workouts.workout_urls.daily_exercise_urls')),

]
