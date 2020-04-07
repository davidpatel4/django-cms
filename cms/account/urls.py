from django.urls import path,include
from account.views import UserCreateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/',LoginView.as_view(template_name = "account/login.html"),name="login"),
    path('', include('django.contrib.auth.urls')),
    path('signup',UserCreateView.as_view()),
 
]