from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
                                label ='Username', 
                                max_length= 100,
                                widget = forms.TextInput(attrs={'class':'form-control'}),)
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control'}),)
    password = forms.CharField(
                                label = "Password", 
                                max_length= 100, 
                                min_length= 5,
                                widget = forms.PasswordInput(attrs={'class':'form-control'}),)
    password1 = forms.CharField(
                                label = "Confirm password", 
                                max_length= 100, 
                                min_length= 5,
                                widget = forms.PasswordInput(attrs={'class':'form-control'}),)

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise ValidationError("Email já registrado")
        return email

    # def clean_password1(self):
    #     p1 = self.cleaned_data['password']
    #     p2 = self.cleaned_data['password1']
    #     if p1 != p2:
    #         raise ValidationError('As senhas são diferentes!')
    #     return p1
    
    # def clean_password2(self):
    #     p1 = self.cleaned_data['password']
    #     p2 = self.cleaned_data['password1']
    #     if p1 != p2:
    #         raise ValidationError('As senhas são diferentes!')
    #     return p2

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password1')
        
        if p1 and p2 :
            if p1 != p2: 
                raise ValidationError('As senhas são diferentes')