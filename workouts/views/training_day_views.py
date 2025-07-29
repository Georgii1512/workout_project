from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import OwnerRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class TrainingDayCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.TrainingDay
    template_name = 'workouts/training_day/training_day_create.html'
    context_object_name = 'training_day'
    form_class = forms.TrainingDayForm

    def get_success_url(self):
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.object.training_plan.slug})

    def form_valid(self, form):
        """
        Automatically set an owner after creating a new training day.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user
        form.instance.training_plan = get_object_or_404(models.TrainingPlan, slug=self.kwargs['slug'])

        return super().form_valid(form)


class TrainingDayDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.TrainingDay
    template_name = 'workouts/training_day/training_day_delete.html'
    context_object_name = 'training_day'

    def get_success_url(self):
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.object.training_plan.slug})


class TrainingDayUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.TrainingDay
    template_name = 'workouts/training_day/training_day_update.html'
    context_object_name = 'training_day'
    form_class = forms.TrainingDayForm

    def get_success_url(self):
        return reverse_lazy('workouts:training_day_detail', kwargs={'slug': self.object.slug})


class TrainingDayDetailView(OwnerRequiredMixin, DetailView):
    model = models.TrainingDay
    template_name = 'workouts/training_day/training_day_detail.html'
    context_object_name = 'training_day'

    def get_context_data(self, **kwargs):
        """
        Add daily exercises to context.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['daily_exercises'] = models.DailyExercise.objects.filter(day=self.get_object())

        return context
