from django.urls import path 
from core.views import RegisterView, UserCreateView

urlpatterns = [
    path("login/",RegisterView.as_view(),name="register"),
    path("create/",UserCreateView.as_view(),name="login")
    
]