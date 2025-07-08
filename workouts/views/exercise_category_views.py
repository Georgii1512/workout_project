from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import BankOwnerMixin


class ExerciseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    form_class = forms.ExerciseCategoryForm


class ExerciseCategoryDeleteView(BankOwnerMixin, DeleteView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'


class ExerciseCategoryUpdateView(BankOwnerMixin, DeleteView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    form_class = forms.ExerciseCategoryForm


class ExerciseCategoryDetailView(BankOwnerMixin, DetailView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'

