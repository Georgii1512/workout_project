from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from workouts import forms, models
from common.mixins import OwnerRequiredMixin


class ExercisesBankCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    form_class = forms.ExercisesBankForm
    template_name = 'workouts/exercises_bank/exercises_bank_create.html'
    success_url = reverse_lazy('workouts:exercises_bank_list')

    def form_valid(self, form):
        """
        For set current user as owner.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ExercisesBankDeleteView(OwnerRequiredMixin, generic.DeleteView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    template_name = 'workouts/exercises_bank/exercises_bank_delete.html'


class ExercisesBankUpdateView(OwnerRequiredMixin, generic.UpdateView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    form_class = forms.ExercisesBankForm
    template_name = 'workouts/exercises_bank/exercises_bank_update.html'
    success_url = reverse_lazy('workouts:exercises_bank_list')


class ExercisesBankDetailView(OwnerRequiredMixin, generic.DetailView):
    model = models.ExercisesBank
    context_object_name = 'exercise_bank'
    template_name = 'workouts/exercises_bank/exercises_bank_detail.html'


class ExerciseBankList(LoginRequiredMixin, generic.ListView):
    model = models.ExercisesBank
    template_name = 'workouts/exercises_bank/exercises_bank_list.html'
    context_object_name = 'exercise_banks'

    def get_queryset(self):
        banks = models.ExercisesBank.objects.filter(owner=self.request.user)

        return banks
