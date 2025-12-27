from django.db import models
from .validators import validate_non_negative
from django.core.validators import RegexValidator


class BakalavrCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class MagistratCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Bakalavr(models.Model):
    kategoriya = models.ForeignKey(BakalavrCategory, on_delete=models.CASCADE, related_name='bakalavrlar')  
    name = models.CharField(max_length=100)
    kunduzgi_kvota = models.IntegerField(validators=[validate_non_negative])

    def __str__(self):
        return self.name


class Magistr(models.Model):
    kategorya = models.ForeignKey(MagistratCategory, on_delete=models.CASCADE, related_name='magistrlar')   
    name = models.CharField(max_length=100)
    kunduzgi_kvota = models.IntegerField(validators=[validate_non_negative])

    def __str__(self):
        return self.name



class QabulCategory(models.Model):
    name = models.CharField("Yo'nalish nomi", max_length=200)

    class Meta:
        verbose_name = "Yo'nalish Kategoriyasi"
        verbose_name_plural = "Yo'nalish Kategoriyalari"

    def __str__(self):
        return self.name




class QabulApplication(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Telefon raqam formati noto‘g‘ri! Masalan: +998901234567"
    )

    full_name = models.CharField("F.I.SH (Familiya, Ism, Otasining ismi)",max_length=255)
    phone = models.CharField("Telefon raqami", max_length=20,validators=[phone_regex])
    address = models.CharField("Yashash manzilingiz",max_length=255)

    EDUCATION_CHOICES = [
        ('orta_maxsus', "O'rta maxsus"),
        ('oliy', "Oliy"),
        ('boshqa', "Boshqa"),
    ]
    education = models.CharField("Qaysi o'qishni tugatgansiz",max_length=20,choices=EDUCATION_CHOICES)
    LANGUAGE_LEVEL_CHOICES = [
        ('boshlangich', "Boshlang'ich"),
        ('orta', "O'rta"),
        ('yuqori', "Yuqori"),
        ('ona_tili', "Ona tili"),
    ]
    direction = models.CharField("Yo'nalish", max_length=255, blank=True, null=True)  # ← 🔥 BU YERDA EDI!
    
    category = models.ForeignKey(QabulCategory, on_delete=models.CASCADE, verbose_name="Yo'nalish kategoriyasi")
    language_level = models.CharField("Til bilish darajasi",max_length=20,choices=LANGUAGE_LEVEL_CHOICES)
    diploma = models.FileField("Shahodatnoma yoki diplom",upload_to='documents/diploma/')
    id_card = models.FileField("ID karta yoki pasport",upload_to='documents/id_card/')
    parent_passport = models.FileField( "Ota yoki onasi pasporti", upload_to='documents/parent_passport/')
    photo_3x4 = models.FileField("3x4 rasm", upload_to='photos/3x4/')
    created_at = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = "Qabul arizasi"
        verbose_name_plural = "Qabul arizalari"
        ordering = ['id']  # eng yangi arizalar birinchi chiqadi

    def __str__(self):
        return self.full_name
