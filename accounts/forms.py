from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import PasswordInput
from django.utils.translation import ugettext_lazy as _

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'placeholder': _('Your First Name'), 'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Your Last Name'), 'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'placeholder': _('Confirm Your Password'), 'class': 'form-input'}),

        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': _("Your Password")})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': _("Confirm Password")})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': _("Your Email")})


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError("This email already used")
        return data

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        cleaned_data = (password, password2)

        if password != password2:
            raise forms.ValidationError("The password does not match ")

        return cleaned_data



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Email or Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
