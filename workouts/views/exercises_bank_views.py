from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView)
from workouts import forms, models
from common.mixins import OwnerRequiredMixin


class ExercisesBankCreateView(OwnerRequiredMixin, CreateView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    form_class = forms.ExercisesBankForm
    template_name = 'workouts/exercises_bank/exercises_bank_create.html'

    def form_valid(self, form):
        """
        For set current user as owner.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user

        return super().form_valid(form)


class ExercisesBankDeleteView(OwnerRequiredMixin, DeleteView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    template_name = 'workouts/exercises_bank/exercises_bank_delete.html'


class ExercisesBankUpdateView(OwnerRequiredMixin, UpdateView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    form_class = forms.ExercisesBankForm
    template_name = 'workouts/exercises_bank/exercises_bank_update.html'


class ExercisesBankDetailView(OwnerRequiredMixin, DetailView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    template_name = 'workouts/exercises_bank/exercises_bank_detail.html'

