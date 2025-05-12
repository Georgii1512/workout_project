from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from abc import ABC, abstractmethod


class VerifyRequestUserMixin(LoginRequiredMixin, UserPassesTestMixin, ABC):
    """
    Mixin to ensure that the requesting user is associated with the object. Need to retrieve user or user identifier
    from the request and compare it with object field that refers to the associated user. Child classes must implement
    the `get_verification()` method.
    """

    @abstractmethod
    def is_requester_associated(self) -> bool:
        """
        This method should compare the requesting user or its identifier with object field that refers to the
        associated user.
        :return: True if the requesting user is associated with the object, False otherwise.
        """
        pass

    def test_func(self):
        return self.is_requester_associated()
