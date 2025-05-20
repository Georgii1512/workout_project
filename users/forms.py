from django.forms.models import ModelForm
from .models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'password']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username']

    def clean_avatar(self):
        """
        Used to set default avatar if previous cleared.
        :return: avatar
        """
        avatar = self.cleaned_data.get('avatar')
        if not avatar:
            avatar = 'default_user_photo.png'
            return avatar

        return avatar
