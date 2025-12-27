from django.urls import path
from .views import index, success, user_login, PostListView, PostDetailView,  user_logout, main

urlpatterns = [
    path('', main, name='main'),
    path('main/', index, name='index'),
    path('success/', success, name='success'),
    path('login/', user_login, name='login'),
    path('detail/', PostListView.as_view(), name='list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('logout/', user_logout, name='logout'),
]
