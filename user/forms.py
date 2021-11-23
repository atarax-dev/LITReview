from django.forms import ModelForm
from user.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'pass1', 'pass2']
