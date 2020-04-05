from django.urls import path,include
from account.views import UserCreateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup',UserCreateView.as_view()),
 
]