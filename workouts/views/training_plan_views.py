from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import OwnerRequiredMixin


class TrainingPlanCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
    form_class = forms.TrainingPlanForm

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)


class TrainingPlanDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'


class TrainingPlanUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
    form_class = forms.TrainingPlanForm


class TrainingPlanDetailView(OwnerRequiredMixin, DetailView):
    model = models.TrainingPlan
    context_object_name = 'training_plan'
