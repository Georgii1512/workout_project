from django.urls import path, include

app_name = 'workouts'

urlpatterns = [
    path('exercise-category/', include('workouts.urls.exercise_category_urls')),
    path('exercise/', include('workouts.urls.exercise_urls')),
    path('training-plan/', include('workouts.urls.training_plan_urls')),
    path('training-day/', include('workouts.urls.training_day_urls')),
    path('daily-exercise/', include('workouts.urls.daily_exercise_urls')),

]
