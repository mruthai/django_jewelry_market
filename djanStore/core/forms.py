from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """_summary_
    A login form for authenticated users.

        This form is used to authenticate users by providing their username and password.
        Attributes:
            username (CharField): A field for the username.
            password (CharField): A field for the password. 
    Args:
        AuthenticationForm (_type_): _description_
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class SignupForm(UserCreationForm):
    """ A signup form for authenticating users with password confirmation.

    This form is used for user registration by providing their desired username,
    email address, and password. It also includes a field to confirm the password.

    Attributes:
        username (CharField): A field for the username.
        email (CharField): A field for the email address.
        password1 (CharField): A field for the password.
        password2 (CharField): A field to confirm the password."""
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
