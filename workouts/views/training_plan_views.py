from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import OwnerRequiredMixin, BankOwnerMixin, CategoryOwnerMixin


class TrainingPlanCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
    form_class = forms.ExercisesBankForm

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)


class TrainingPlanDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'


class TrainingPlanUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
    form_class = forms.ExercisesBankForm


class TrainingPlanDetailView(OwnerRequiredMixin, DetailView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
