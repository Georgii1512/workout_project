from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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
        training_day_slug = self.kwargs.get('slug')
        if training_day_slug:
            form.instance.day = get_object_or_404(models.TrainingDay, slug=training_day_slug)

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to a training plan detail view.
        :return: Training plan detail view URL.
        """
        return reverse_lazy('workouts:training_day_detail', kwargs={'slug': self.object.day.slug})

    def get_form(self, form_class = forms.DailyExerciseForm) -> forms.DailyExerciseForm:
        """
        Retrieve and configure the form instance used in the view.
        :param form_class: The form class to instantiate. Defaults to forms.DailyExerciseForm.
        :return: A configured instance of the specified form class.
        """
        form: forms.DailyExerciseForm = super().get_form(form_class)
        form.fields['exercise'].queryset = models.Exercise.objects.filter(owner=self.request.user)

        return form


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
        return reverse_lazy('workouts:training_day_detail', kwargs={'slug': self.object.day.slug})


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
        return reverse_lazy('workouts:daily_exercise_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        """
        Automatically set an owner and training day after creating a new training day.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user
        form.instance.training_day = models.TrainingDay.objects.get(slug=self.kwargs['slug'])

        return super().form_valid(form)


class DailyExerciseDetailView(LoginRequiredMixin, DetailView):
    model = models.DailyExercise
    template_name = 'workouts/daily_exercise/daily_exercise_detail.html'
    context_object_name = 'daily_exercise'

