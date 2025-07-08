from django.views.generic import (CreateView, DetailView, DeleteView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import CategoryOwnerMixin


class ExerciseCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.Exercise
    context_object_name = 'exercise'
    form_class = forms.ExerciseForm


class ExerciseDeleteView(CategoryOwnerMixin, DeleteView):
    model = models.Exercise
    context_object_name = 'exercise'


class ExerciseUpdateView(CategoryOwnerMixin, DeleteView):
    model = models.Exercise
    context_object_name = 'exercise'
    form_class = forms.ExerciseForm


class ExerciseDetailView(CategoryOwnerMixin, DetailView):
    model = models.Exercise
    context_object_name = 'exercise'
    form_class = forms.ExerciseForm

