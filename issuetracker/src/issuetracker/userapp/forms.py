from django import forms
from utils import users as usersutil
# from userapp.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import models


models.Field


class UserNameInvalidException(forms.ValidationError):pass
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, min_length=10, label="Username")
    password = forms.CharField(max_length=40, min_length=10, label="Password",widget=forms.PasswordInput())
    
    def clean(self):
        # return True
        super().clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        usernameError = usersutil.validate_usernames(username)
        print("Username Error:"+str(usernameError))
        if usernameError:
            self.add_error("username", usernameError)

        passwordError = usersutil.validate_password(password)

        if passwordError:
            self.add_error("password", passwordError)

        ## check is user id password is correct

        if not authenticate(username=username, password=password):
            self.add_error("__all__", "Username or password invalid")
        print ("authenticated")    
        return self.cleaned_data
        
    
class RegisterForm(forms.Form):
    username= forms.CharField(max_length=50, min_length=10, label="Username")
    password= forms.CharField(max_length=50, min_length=10, label="Password", widget = forms.PasswordInput())
    confirmPassword = forms.CharField(max_length=50, min_length=10, label="Confirm Password", widget = forms.PasswordInput())

    def clean(self):
        super().clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirmPassword = self.cleaned_data.get("confirmPassword")

        usernameError = usersutil.validate_usernames(username)
        if usernameError:
            self.add_error("username", usernameError)

        passwordError = usersutil.validate_password(password)

        if passwordError:
            self.add_error("password", passwordError)

        if not password == confirmPassword:
            self.add_error("password", "Passwords donot match")
            self.add_error("confirmPassword", "Passwords donot match")

        ## check if exists in database
        
        
        if User.objects.filter(username = username):
            self.add_error("__all__","The username already exists")
        

        self.cleaned_data

    
