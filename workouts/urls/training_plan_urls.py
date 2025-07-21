from django.urls import path
from workouts.views import training_plan_views as views
from workouts.views.training_day_views import TrainingDayCreateView

urlpatterns = [
    path('create/', views.TrainingPlanCreateView.as_view(), name='training_plan_create'),
    path('list/', views.TrainingPlanListView.as_view(), name='training_plan_list'),
    path('<slug:slug>/', views.TrainingPlanDetailView.as_view(), name='training_plan_detail'),
    path('<slug:slug>/update/', views.TrainingPlanUpdateView.as_view(), name='training_plan_update'),
    path('<slug:slug>/delete/', views.TrainingPlanDeleteView.as_view(), name='training_plan_delete'),
    path('<slug:slug>/training-day/add/', TrainingDayCreateView.as_view(), name='training_day_add')
]
