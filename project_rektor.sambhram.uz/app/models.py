from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name="Lavozim nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lavozim"
        verbose_name_plural = "Lavozimlar"



class User(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name="To‘liq ism", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam", blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Viloyat")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Lavozim")

    # Qo‘shimcha rollar (ixtiyoriy)
    is_operator = models.BooleanField(default=False, verbose_name="Operator")
    is_manager = models.BooleanField(default=False, verbose_name="Rahbar")

    def __str__(self):
        if self.full_name:
            return f"{self.full_name} ({self.position})" if self.position else self.full_name
        return self.username

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"






class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name='Viloyat nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class Gender(models.Model):
    name = models.CharField(max_length=100, verbose_name='Jinsi nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jins'
        verbose_name_plural = 'Jinslar'


class ApplicationType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Murojat turi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Murojat turi'
        verbose_name_plural = 'Murojat turlari'


class Post(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Familiya')
    first_name = models.CharField(max_length=100, verbose_name='Ism')
    address = models.CharField(max_length=200, verbose_name='Manzil')
    tel_number = models.CharField(max_length=15, verbose_name="Telefon raqami")
    email = models.EmailField(max_length=254, verbose_name='Email')
    topic = models.CharField(blank=True, null=True, max_length=255, verbose_name="Murajatni qisqacha mazmuni")
    body = models.TextField(blank=True, null=True, verbose_name="Murajat matni")
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name="Viloyat")
    gender = models.ForeignKey('Gender', on_delete=models.CASCADE, verbose_name="Jinsi")
    application_type = models.ForeignKey('ApplicationType', on_delete=models.CASCADE, verbose_name="Murojat turi")
    files = models.FileField(upload_to='files/', blank=True, null=True, verbose_name="Fayl")

    # 🔗 Qabul qiluvchi foydalanuvchi yoki lavozim
    to_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='received_posts', verbose_name="Qabul qiluvchi foydalanuvchi")
    to_position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, blank=True, related_name='position_posts', verbose_name="Qabul qiluvchi lavozim")

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "So‘rov"
        verbose_name_plural = "So‘rovlar"
        ordering = ['-id']
