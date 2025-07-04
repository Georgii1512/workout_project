from django.urls import path
from workouts.views import training_day_views as views

urlpatterns = [
    path('create/', views.TrainingDayCreateView.as_view(), name='training_day_create'),
    path('<int:pk>/', views.TrainingDayDetailView.as_view(), name='training_day_detail'),
    path('<int:pk>/update/', views.TrainingDayUpdateView.as_view(), name='training_day_update'),
    path('<int:pk>/delete/', views.TrainingDayDeleteView.as_view(), name='training_day_delete'),

]
