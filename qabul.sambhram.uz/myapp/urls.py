from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index, name="index"),
    path('jadval', table, name="table"),
    path('success', success, name="success"),
    path('login', login_view, name="login_view"),

  
]

