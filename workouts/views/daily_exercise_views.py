from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from workouts import forms, models


class DailyExerciseCreateView(LoginRequiredMixin, CreateView):
    model = models.DailyExercise
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm


class DailyExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.DailyExercise
    context_object_name = 'daily_exercise'


class DailyExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = models.DailyExercise
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm


class DailyExerciseDetailView(LoginRequiredMixin, DetailView):
    model = models.DailyExercise
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm

