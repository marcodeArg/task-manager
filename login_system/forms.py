from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-contol"}),
    )

    def clean_username(self):
        username = self.cleaned_data["username"]

        if not User.objects.filter(username=username).exist():
            raise forms.ValidationError({"username": "Username does not exist"})
        return username
