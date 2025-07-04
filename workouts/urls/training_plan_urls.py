from django.urls import path
from workouts.views import training_plan_views as views


urlpatterns = [
    path('create/', views.TrainingPlanCreateView.as_view(), name='training_plan_create'),
    path('<int:pk>/', views.TrainingPlanDetailView.as_view(), name='training_plan_detail'),
    path('<int:pk>/update/', views.TrainingPlanUpdateView.as_view(), name='training_plan_update'),
    path('<int:pk>/delete/', views.TrainingPlanDeleteView.as_view(), name='training_plan_delete'),
]