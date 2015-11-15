from django import forms

from users.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']