from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from workouts import forms, models
from django.urls import reverse_lazy


class DailyExerciseCreateView(LoginRequiredMixin, CreateView):
    model = models.DailyExercise
    template_name = 'workouts/daily_exercise/daily_exercise_create.html'
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm

    def form_valid(self, form):
        """
        Set owner.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to a training plan detail view.
        :return: Training plan detail view URL.
        """
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.object.training_plan.slug})


class DailyExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.DailyExercise
    template_name = 'workouts/daily_exercise/daily_exercise_delete.html'
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm

    def get_success_url(self):
        """
        Redirect to a training plan detail view.
        :return: Training plan detail view URL.
        """
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.object.training_plan.slug})


class DailyExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = models.DailyExercise
    template_name = 'workouts/daily_exercise/daily_exercise_update.html'
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm

    def get_success_url(self):
        """
        Redirect to a training plan detail view.
        :return: Training plan detail view URL.
        """
        return reverse_lazy('workouts:training_plan_detail', kwargs={'slug': self.object.training_plan.slug})


class DailyExerciseDetailView(LoginRequiredMixin, DetailView):
    model = models.DailyExercise
    template_name = 'workouts/daily_exercise/daily_exercise_detail.html'
    context_object_name = 'daily_exercise'
    form_class = forms.DailyExerciseForm

