from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from typing import Any
from .models import (Bakalavr, BakalavrCategory,Magistr, MagistratCategory, QabulApplication)
from .forms import (BakalavrForm, BakalavrCategoryForm, MagistrForm, MagistratCategoryForm, QabulApplicationForm)

# Index sahifasi
class IndexView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["bakalavr"] = Bakalavr.objects.all()
        context["magistr"] = Magistr.objects.all()
        return context
    
    template_name = "index.html"


# Login view
def login_view(request):
    # Agar foydalanuvchi allaqachon tizimga kirgan bo'lsa, dashboardga yo'naltirish
    if request.user.is_authenticated:
        return redirect("myapp:dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.username}!")
            return redirect("myapp:dashboard")
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")

    return render(request, "login.html")


# Dashboard view (faqat login qilingan foydalanuvchilar uchun)
@login_required
def dashboard(request):
    bakalavr_count = QabulApplication.objects.count()
    qabul = QabulApplication.objects.all()

    context = {
        'bakalavr_count': bakalavr_count,
        'qabul': qabul,
    }
    return render(request, "dashboard.html", context)





@login_required
def application_detail(request, pk):
    application = get_object_or_404(QabulApplication, pk=pk)
    bakalavr_count = QabulApplication.objects.count()
    context = {'app': application,'bakalavr_count': bakalavr_count}
    return render(request, 'application_detail.html', context)

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Siz tizimdan chiqdingiz.")
    return redirect("myapp:login")


class SuccessView(TemplateView):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["qabul"] = QabulApplication.objects.all()
        return context
    
    template_name="success.html"



class FormsView(TemplateView):
    template_name = "forms.html"

    def get(self, request, *args, **kwargs):
        form = QabulApplicationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = QabulApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("myapp:success")  # Muvaffaqiyat sahifasi

        return render(request, self.template_name, {"form": form})
