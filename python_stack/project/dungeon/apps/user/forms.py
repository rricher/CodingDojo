from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    # validators=[validate_confirm_password]
    confirm_password = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput()
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }