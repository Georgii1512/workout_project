from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from abc import ABC, abstractmethod

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest
from django.views.generic.detail import SingleObjectMixin
from workouts.models import Exercise

class VerifyRequestUserMixin(LoginRequiredMixin, UserPassesTestMixin, ABC):
    """
    Mixin to ensure that the requesting user is associated with the object. Need to retrieve user or user identifier
    from the request and compare it with object field that refers to the associated user. Child classes must implement
    the `is_requester_associated()` method.
    """

    @abstractmethod
    def is_requester_associated(self) -> bool:
        """
        This method should compare the requesting user or its identifier with object field that refers to the
        associated user.
        :return: True if the requesting user is associated with the object, False otherwise.
        """
        raise NotImplementedError("Child classes must implement the `is_requester_associated()` method.")

    def test_func(self):
        return self.is_requester_associated()


class OwnerRequiredMixin(VerifyRequestUserMixin, SingleObjectMixin):
    """
    Mixin to ensure that the requesting user is the owner of the object.
    Assumes that the view has a `get_object()` method that returns the object.
    """

    owner_field = 'owner'  # Default field name that links the object to its owner
    request: HttpRequest

    def is_requester_associated(self) -> bool:
        obj = super().get_object()
        owner = getattr(obj, self.owner_field, None)
        if owner is None:
            raise ImproperlyConfigured(
                f"The object does not have an attribute '{self.owner_field}'."
            )
        return owner == self.request.user


class BankOwnerMixin(LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin):
    """
    Mixin to check whether request use is exercises bank owner.
    """
    request: HttpRequest

    def test_func(self):
        """
                Checks whether request user is exercises bank owner.
                :return: True is request user is exercises bank owner else False
                """
        user = self.request.user
        obj = super().get_object()
        bank_owner = obj.exercises_bank.owner

        return user == bank_owner

class CategoryOwnerMixin(BankOwnerMixin):
    def test_func(self):
        user = self.request.user
        owner: Exercise = super().get_object().exercise_category.exercises_bank.owner

        return user == owner

