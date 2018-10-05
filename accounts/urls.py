from django.urls import path
from . import views

urlpatterns = [
    path('senior/signup/', views.SeniorSignUp, name='senior_signup'),
    path('supporter/signup/', views.SupporterSignUp, name='supporter_signup'),
]
