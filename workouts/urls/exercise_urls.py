from django.urls import path
from workouts.views import exercise_views as views

urlpatterns = [
    path('create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
    path('<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('<int:pk>/update/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('<int:pk>/delete/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('list/', views.ExerciseListView.as_view(), name='exercises_list'),
]
