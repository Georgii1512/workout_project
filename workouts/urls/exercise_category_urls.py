from django.urls import path
from workouts.views import exercise_category_views as views

urlpatterns = [
    path('create/', views.ExerciseCategoryCreateView.as_view(), name='exercise_category_create'),
    path('<int:pk>/', views.ExerciseCategoryDetailView.as_view(), name='exercise_category_detail'),
    path('<int:pk>/update/', views.ExerciseCategoryUpdateView.as_view(), name='exercise_category_update'),
    path('<int:pk>/delete/', views.ExerciseCategoryDeleteView.as_view(), name='exercise_category_delete'),
]
