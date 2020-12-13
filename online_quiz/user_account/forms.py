from django import forms
from .models import UserAccount


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)

