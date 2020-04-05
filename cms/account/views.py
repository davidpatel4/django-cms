from django.shortcuts import render
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpForm
# Create your views here.


class UserCreateView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm
    success_url ="/blogs"