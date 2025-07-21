from django.urls import path
from workouts.views import training_day_views as views

urlpatterns = [
    path('<slug:slug>/detail/', views.TrainingDayDetailView.as_view(), name='training_day_detail'),
    path('<slug:slug>/update/', views.TrainingDayUpdateView.as_view(), name='training_day_update'),
    path('<slug:slug>/delete/', views.TrainingDayDeleteView.as_view(), name='training_day_delete'),
]
