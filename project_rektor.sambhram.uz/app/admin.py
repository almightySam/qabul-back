from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Region, Gender, ApplicationType, Position, User, Post


# =======================
#  REGION ADMIN
# =======================
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)
    verbose_name = 'Viloyat'


# =======================
#  GENDER ADMIN
# =======================
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)
    verbose_name = 'Jins'


# =======================
#  APPLICATION TYPE ADMIN
# =======================
@admin.register(ApplicationType)
class ApplicationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)
    verbose_name = 'Murojaat turi'


# =======================
#  POSITION ADMIN
# =======================
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)
    verbose_name = 'Lavozim'


# =======================
#  USER ADMIN (Custom)
# =======================
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom foydalanuvchi admin paneli
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Shaxsiy maʼlumotlar'), {
            'fields': ('full_name', 'first_name', 'last_name', 'email', 'phone', 'region', 'position')
        }),
        (_('Ruxsatlar'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Qoʻshimcha holatlar'), {
            'fields': ('is_operator', 'is_manager')
        }),
        (_('Muhim sanalar'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'full_name', 'email', 'phone', 'region', 'position', 'is_staff', 'is_superuser'),
        }),
    )

    list_display = ('username', 'full_name', 'email', 'phone', 'region', 'position', 'is_operator', 'is_manager', 'is_active')
    list_filter = ('region', 'position', 'is_operator', 'is_manager', 'is_staff', 'is_superuser')
    search_fields = ('username', 'full_name', 'email', 'phone', 'position__name')
    ordering = ('id',)
    readonly_fields = ('last_login', 'date_joined')


# =======================
#  POST ADMIN
# =======================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Murojaatlarni boshqarish admin paneli
    """
    list_display = (
        'id', 'last_name', 'first_name', 'topic',
        'region', 'application_type', 'to_user', 'to_position', 'created_at'
    )
    list_filter = ('region', 'application_type', 'gender', 'to_position')
    search_fields = ('last_name', 'first_name', 'email', 'topic', 'body', 'to_user__username', 'to_position__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Shaxsiy maʼlumotlar', {
            'fields': ('last_name', 'first_name', 'address', 'tel_number', 'email', 'gender')
        }),
        ('Murojaat tafsilotlari', {
            'fields': ('topic', 'body', 'region', 'application_type', 'files')
        }),
        ('Kimga yuborilgan', {
            'fields': ('to_user', 'to_position')
        }),
        ('Qo‘shimcha maʼlumotlar', {
            'fields': ('created_at',)
        }),
    )
