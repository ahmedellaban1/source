from django import forms
from django.contrib.auth.models import User


def fields_rename(fields):
    for i in fields:
        fields[i].widget.attrs['placeholder']  = fields[i].label
        fields[i].label = ''
        fields[i].help_text = ''


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_rename(self.fields)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_rename(self.fields)

