# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'birthdate',
            'role', 'gender', 'country', 'email', 'password1', 'password2'
        ]
        widgets = {
            'gender': forms.RadioSelect
        }
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude 'admin' role from registration form
        self.fields['role'].choices = [
            choice for choice in self.fields['role'].choices if choice[0] != 'admin'
        ]

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role == 'intent':
            self.instance.is_approved = False
        return role
