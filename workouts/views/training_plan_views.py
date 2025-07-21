from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView, ListView)
from django.contrib.auth import mixins
from workouts import forms, models
from common.mixins import OwnerRequiredMixin
from django.urls import reverse_lazy


class TrainingPlanCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.TrainingPlan
    template_name = 'workouts/training_plan/training_plan_create.html'
    context_object_name = 'training_plan'
    form_class = forms.TrainingPlanForm
    success_url = reverse_lazy('workouts:training_plan_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def form_valid(self, form):
        """
        Automatically set an owner after creating a new training plan.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user

        return super().form_valid(form)


class TrainingPlanDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.TrainingPlan
    template_name = 'workouts/training_plan/training_plan_delete.html'
    context_object_name = 'training_plan'
    success_url = reverse_lazy('workouts:training_plan_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


class TrainingPlanUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.TrainingPlan
    template_name = 'workouts/training_plan/training_plan_update.html'
    context_object_name = 'training_plan'
    form_class = forms.TrainingPlanForm
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_success_url(self):
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.get_object().slug})


class TrainingPlanDetailView(OwnerRequiredMixin, DetailView):
    model = models.TrainingPlan
    template_name = 'workouts/training_plan/training_plan_detail.html'
    context_object_name = 'training_plan'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['training_days'] = models.TrainingDay.objects.filter(training_plan=self.get_object())

        return context


class TrainingPlanListView(mixins.LoginRequiredMixin, ListView):
    model = models.TrainingPlan
    template_name = 'workouts/training_plan/training_plans_list.html'
    context_object_name = 'training_plans'
    ordering = ['name']
