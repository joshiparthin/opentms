from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from userapp.forms import LoginForm, RegisterForm
# from userapp.models import User
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kargs):
        form = LoginForm()
        return render(request,"user/login.html", {"form":form})
    
    def post(self, request, *args, **kargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            # request.session["user"]=form.cleaned_data.get("username")
            user = User.objects.filter(username=form.cleaned_data.get("username")).first()
            print("loging using ", user)
            login(request, user)
            return HttpResponseRedirect("/issue/list")
        else: 
            print("not valid")
            return render(request,"user/login.html",{"form":form})
    

    @staticmethod
    def logout(request):
        logout(request)
        return HttpResponseRedirect("/user/login")

class RegisterView(View):
    def get(self, request, *args, **kargs):
        form = RegisterForm()
        return render(request,"user/register.html", {"form":form})
    
    def post(self, request, *args, **kargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            userModel = User(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            userModel = User.objects.create_user(form.cleaned_data.get("username"), None, form.cleaned_data.get("password"))
            try:
                userModel.save()
            except Exception as e:
                form.add_error("all", "Error saving the user: "+ str(e))
            return HttpResponseRedirect("/user/login")
        else: 
            return render(request,"user/register.html",{"form":form})
