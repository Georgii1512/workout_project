from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import OwnerRequiredMixin


class TrainingDayCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.TrainingDay
    context_object_name = 'training_day'
    form_class = forms.TrainingDayForm


class TrainingDayDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.TrainingDay
    context_object_name = 'training_day'


class TrainingDayUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.TrainingDay
    context_object_name = 'training_day'
    form_class = forms.TrainingDayForm


class TrainingDayDetailView(OwnerRequiredMixin, DetailView):
    model = models.TrainingDay
    context_object_name = 'training_day'

