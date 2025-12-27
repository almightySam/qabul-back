from django.contrib import admin
from .models import (
    BakalavrCategory,
    MagistratCategory,
    Bakalavr,
    Magistr,
    QabulCategory, QabulApplication
)


# ------------------------
# INLINE MODELLAR
# ------------------------

class BakalavrInline(admin.TabularInline):
    model = Bakalavr
    extra = 1


class MagistrInline(admin.TabularInline):
    model = Magistr
    extra = 1


# ------------------------
# CATEGORY ADMIN
# ------------------------

@admin.register(BakalavrCategory)
class BakalavrCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [BakalavrInline]


@admin.register(MagistratCategory)
class MagistratCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [MagistrInline]


# ------------------------
# ASOSIY MODELLAR
# ------------------------

@admin.register(Bakalavr)
class BakalavrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kategoriya', 'kunduzgi_kvota')
    list_filter = ('kategoriya',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Magistr)
class MagistrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kategorya', 'kunduzgi_kvota')
    list_filter = ('kategorya',)
    search_fields = ('name',)
    list_per_page = 20



@admin.register(QabulCategory)
class QabulCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(QabulApplication)
class QabulApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "education",
        "category",
        "language_level",
        "created_at",
    )
    list_filter = ("education", "category", "language_level", "created_at")
    search_fields = ("full_name", "phone", )
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Shaxsiy ma'lumotlar", {
            "fields": ("full_name", "phone", "address")
        }),

        ("Ta'lim ma'lumotlari", {
            "fields": ("education", "category", "language_level")
        }),

        ("Hujjatlar", {
            "fields": ("diploma", "id_card", "parent_passport", "photo_3x4")
        }),

        ("Tizim", {
            "fields": ("created_at",)
        }),
    )