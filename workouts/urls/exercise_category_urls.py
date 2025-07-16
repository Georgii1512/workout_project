from django.urls import path
from workouts.views import exercise_category_views as views

urlpatterns = [
    path('create/', views.ExerciseCategoryCreateView.as_view(), name='exercise_category_create'),
    path('list/', views.ExerciseCategoryListView.as_view(), name='exercise_categories_list'),
    path('<slug:slug>/', views.ExerciseCategoryDetailView.as_view(), name='exercise_category_detail'),
    path('<slug:slug>/update/', views.ExerciseCategoryUpdateView.as_view(), name='exercise_category_update'),
    path('<slug:slug>/delete/', views.ExerciseCategoryDeleteView.as_view(), name='exercise_category_delete'),

]
