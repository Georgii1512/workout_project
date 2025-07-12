from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import User
from django.urls import reverse, reverse_lazy
from common.mixins import VerifyRequestUserMixin
from . import forms
from workouts.models import ExerciseCategory


# Create your views here.

class UsersListView(ListView):
    template_name = 'users/users_list.html'
    queryset = User.objects.order_by('-date_joined')
    model = User
    context_object_name = 'users'
    paginate_by = 10


class UserCreateView(CreateView):
    """
    Serves for users registration.
    """
    template_name = 'users/registration.html'
    model = User
    context_object_name = 'user'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('users:users_list')


class UserUpdateView(VerifyRequestUserMixin, UpdateView):
    template_name = 'users/user_update.html'
    model = User
    context_object_name = 'user'
    form_class = forms.UserUpdateForm
    login_url = '/login/'

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'pk': self.request.user.pk})

    def is_requester_associated(self) -> bool:
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionError("You have ho permission!")
        else:
            return super().handle_no_permission()


class UserDetailView(VerifyRequestUserMixin, DetailView):
    template_name = 'users/user_detail.html'
    model = User
    context_object_name = 'user'

    def is_requester_associated(self) -> bool:
        return self.request.user == self.get_object()

