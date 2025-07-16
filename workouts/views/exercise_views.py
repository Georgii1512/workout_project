from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, DeleteView, ListView, UpdateView)
from django.contrib.auth import mixins
from workouts import forms, models


class ExerciseCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.Exercise
    context_object_name = 'exercise'
    form_class = forms.ExerciseForm
    success_url = reverse_lazy('workouts:exercises_list')
    template_name = 'workouts/exercise/exercise_create.html'

    def form_valid(self, form):
        """
        Set exercise owner.
        :param form:
        :return:
        """
        form.instance.owner = self.request.user

        return super().form_valid(form)


class ExerciseDeleteView(mixins.LoginRequiredMixin,
                         mixins.UserPassesTestMixin,
                         DeleteView):
    model = models.Exercise
    context_object_name = 'exercise'
    template_name = 'workouts/exercise/exercise_delete.html'
    success_url = reverse_lazy('workouts:exercises_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        """
        Checks whether a request user is an exercise owner.
        :return: True is a request user is an exercise owner else False
        """
        user = self.request.user
        exercise: models.Exercise = self.get_object()
        owner: models.Exercise = exercise.owner

        return user == owner


class ExerciseUpdateView(mixins.LoginRequiredMixin,
                         mixins.UserPassesTestMixin,
                         UpdateView):
    model = models.Exercise
    context_object_name = 'exercise'
    form_class = forms.ExerciseForm
    template_name = 'workouts/exercise/exercise_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        """
        Checks whether a request user is an exercise owner.
        :return: True is a request user is an exercise owner else False
        """
        user = self.request.user
        exercise: models.Exercise = self.get_object()
        owner: models.Exercise = exercise.owner

        return user == owner

    def get_success_url(self):
        return reverse_lazy('workouts:exercise_detail', kwargs={'slug': self.get_object().slug})


class ExerciseDetailView(mixins.LoginRequiredMixin, DetailView):
    model = models.Exercise
    context_object_name = 'exercise'
    template_name = 'workouts/exercise/exercise_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        yt_embedded_base_link = 'https://www.youtube.com/embed/'
        video_id = self.get_object().instruction_link.split('v=')[-1]
        context['instruction_yt_url'] = yt_embedded_base_link + video_id

        return context


class ExerciseListView(mixins.LoginRequiredMixin, ListView):
    model = models.Exercise
    context_object_name = 'exercises'
    template_name = 'workouts/exercise/exercises_list.html'
    ordering = ['category__name', 'name',]

    def get_queryset(self):
        exercise = models.Exercise.objects.filter(owner=self.request.user).prefetch_related('exercise_category')

        return exercise
