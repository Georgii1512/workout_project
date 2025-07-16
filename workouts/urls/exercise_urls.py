from django.urls import path
from workouts.views import exercise_views as views

urlpatterns = [
    path('create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
    path('list/', views.ExerciseListView.as_view(), name='exercises_list'),
    path('<slug:slug>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('<slug:slug>/update/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('<slug:slug>/delete/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
]
