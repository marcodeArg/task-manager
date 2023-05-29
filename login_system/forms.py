from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password1"]

        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(
                    {"password1": "Incorrect username or password"}
                )
        else:
            raise forms.ValidationError({"username": "Username does not exist"})
        return cleaned_data
