from django.urls import path
from .views import *

app_name = "myapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", dashboard, name="dashboard"),  # kichik harf bilan
    path('application/<int:pk>/', application_detail, name='application_detail'),
    path("Hujjat-topshirish/", FormsView.as_view(), name="qabul_form"),  # kichik harf bilan
    path("Ariza-yuborildi/", SuccessView.as_view(), name="success"),

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
