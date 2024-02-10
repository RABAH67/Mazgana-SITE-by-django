from django import forms
from django.contrib.auth.forms import AuthenticationForm ,UsernameField ,UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField










class CustemRegistrationForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}),label="Last Name")
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control','id':'name'}))
    phone = PhoneNumberField(widget=forms.NumberInput(attrs={'autofocus':'True','class':'form-control','id':'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','id':'email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'name'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'name'}))

    class Meta:
        model = User
        
        fields = ['username','first_name','phone','email','password1','password2']
        
        
        
        
class LoginForm(AuthenticationForm):
    
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}),label="Last Name")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))
        

        
        
        
        
        
        
        
        
        