from login import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(forms.ModelForm):
    """
    Customer Signup Form
    """
    password1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type':'password', 'class': 'form-control', 'placeholder':"Enter Password"},))
    password2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type':'password', 'class': 'form-control', 'placeholder':"Enter Password"},))

    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'company_name',
            'website_name',
            'profession',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Company Name'
        self.fields['website_name'].widget.attrs['placeholder'] = 'Website Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['company_name'].widget.attrs['class'] = 'form-control'
        self.fields['website_name'].widget.attrs['class'] = 'form-control'
        

    def clean(self):
        cleaned_data = super(self.__class__, self).clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError({'password2': 'Both password must be same'})
        return cleaned_data

    def save(self, commit=True):
        user = super(self.__class__, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user            


class Loginform(AuthenticationForm):
    """
    Custom Login Form
    """

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['type'] = 'password'