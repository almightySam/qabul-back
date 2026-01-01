from django.urls import path
from app.views import  user_login, user_logout, main

urlpatterns = [
    path('', main, name='main'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
