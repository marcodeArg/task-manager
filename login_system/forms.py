from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # Doens't work
    # error_css_class = "invalid-feedback"

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        new_data = {
            "class": "form-control",
        }

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(new_data)


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = "form-control"

    def clean_username(self):
        username = self.cleaned_data["username"]

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username does not exist")
        return username
