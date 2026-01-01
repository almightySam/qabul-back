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



from django.http import HttpResponse
from openpyxl import Workbook
from django.contrib.auth.decorators import login_required


@login_required
def export_qabul_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Qabul arizalari"

    # Sarlavhalar
    headers = [
        "ID",
        "F.I.SH",
        "Telefon",
        "Manzil",
        "Ta'lim",
        "Til darajasi",
        "Yo'nalish kategoriyasi",
        "Yo'nalish",
        "Yaratilgan sana",
    ]
    ws.append(headers)

    # Ma'lumotlar
    for app in QabulApplication.objects.all():
        ws.append([
            app.id,
            app.full_name,
            app.phone,
            app.address,
            app.get_education_display(),
            app.get_language_level_display(),
            app.category.name if app.category else "",
            app.direction or "",
            app.created_at.strftime("%d.%m.%Y %H:%M"),
        ])

    # Javob
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=qabul_arizalari.xlsx'

    wb.save(response)
    return response



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
    qs = QabulApplication.objects.order_by('-created_at')
    bakalavr_count = QabulApplication.objects.count()
    approved_count = QabulApplication.objects.filter(is_published=True).count()
    pending_count = QabulApplication.objects.filter(is_published=False).count()
    total_count = QabulApplication.objects.count()
    qabul = QabulApplication.objects.all()
    paginator = Paginator(qs, 10)  # 1 sahifada 10 ta
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)

    context = {
        'applications': applications,
        'bakalavr_count': bakalavr_count,
        'qabul': qabul,
        'approved_count': approved_count,
        'pending_count': pending_count,
        'total_count': total_count,
    }
    return render(request, "dashboard.html", context)





@login_required
def application_detail(request, pk):
    app = get_object_or_404(QabulApplication, pk=pk)

    if request.method == "POST":
        app.is_published = True
        app.save()

    bakalavr_count = QabulApplication.objects.filter(is_published=True).count()

    context = {
        'app': app,
        'bakalavr_count': bakalavr_count
    }
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
