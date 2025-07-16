from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (CreateView, DetailView, DeleteView, UpdateView, ListView)
from workouts import forms, models

# TODO: Add uniqueness constraint failure handling
class ExerciseCategoryCreateView(mixins.LoginRequiredMixin, CreateView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    form_class = forms.ExerciseCategoryForm
    template_name = 'workouts/exercise_category/exercise_category_create.html'
    success_url = reverse_lazy('workouts:exercises_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Set the owner to the current user
        print(form.instance.slug)

        return super().form_valid(form)


class ExerciseCategoryDeleteView(mixins.LoginRequiredMixin,
                                 mixins.UserPassesTestMixin,
                                 DeleteView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    template_name = 'workouts/exercise_category/exercise_category_delete.html'
    success_url = reverse_lazy('workouts:exercises_list')

    def test_func(self):
        """
        Checks whether a request user is an exercise category owner.
        :return: True is a request user is the owner else False
        """
        user = self.request.user
        exercise_category: models.ExerciseCategory = self.get_object()
        owner: models.ExerciseCategory = exercise_category.owner

        return user == owner


class ExerciseCategoryUpdateView(mixins.LoginRequiredMixin,
                                 mixins.UserPassesTestMixin,
                                 UpdateView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    form_class = forms.ExerciseCategoryForm
    template_name = 'workouts/exercise_category/exercise_category_update.html'
    success_url = reverse_lazy('workouts:exercises_list')

    def test_func(self):
        """
        Checks whether a request user is an exercise category owner.
        :return: True is a request user is the owner else False
        """
        user = self.request.user
        exercise_category: models.ExerciseCategory = self.get_object()
        owner: models.ExerciseCategory = exercise_category.owner

        return user == owner


class ExerciseCategoryDetailView(mixins.LoginRequiredMixin, DetailView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_category'
    template_name = 'workouts/exercise_category/exercise_category_detail.html'


class ExerciseCategoryListView(mixins.LoginRequiredMixin, ListView):
    model = models.ExerciseCategory
    context_object_name = 'exercise_categories'
    template_name = 'workouts/exercise_category/exercise_categories_list.html'
    ordering = ['name']

    def get_queryset(self):
        exercise_category = models.ExerciseCategory.objects.filter(owner=self.request.user)

        return exercise_category
