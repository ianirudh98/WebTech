from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control col-6","placeholder":"Your Name"}),label='Name')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control col-6","placeholder":"Password"}),label='Password')

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control col-6","placeholder":"Your Name"}),label='Name')
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control col-6","placeholder":"Email"}),label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control col-6","placeholder":"Password"}),label='Password')
    confirm = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput(attrs={"class":"form-control col-6","placeholder":"Re-enter Password"}))


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password != confirm:
            raise forms.ValidationError("Passwords must match!")
        return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("User Name already exists!")
        return username