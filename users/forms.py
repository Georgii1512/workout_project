from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['avatar', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
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
