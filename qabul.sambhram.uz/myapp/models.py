from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator

# Create your models here.
class QabulHolati(models.Model):
    nomi = models.CharField(max_length=100, default="Online Qabul", verbose_name="Qabul turi",blank=True,null=True,)
    ochiq = models.BooleanField(default=True,blank=True,null=True, verbose_name="Qabul ochiqmi?")
    xabar = models.TextField(
        default="Online qabul tugallandi. Hujjat topshirish istagida bo'lganlar Sambhram NTM qabul komissiyasiga murojaat qilishlarini so'raymiz.",
        verbose_name="Yopiq holatda ko'rsatiladigan xabar",blank=True,null=True,
    )
    
    class Meta:
        verbose_name = "Qabul holati"
        verbose_name_plural = "Qabul holati"
    
    def __str__(self):
        return f"{self.nomi} - {'Ochiq' if self.ochiq else 'Yopiq'}"

class Education(models.Model):
    title = models.CharField(max_length=150, verbose_name="Yonalish")
    
    class Meta:
        verbose_name = "Yonalish kiriting"
        verbose_name_plural = "Yonalish Fanlar"
    
    def __str__(self):
        return self.title

class Till(models.Model):
    title = models.CharField(max_length=150, verbose_name="til bilish daraja")
    
    class Meta:
        verbose_name = "til bilish daraja"
        verbose_name_plural = "til bilish daraja"
    
    def __str__(self):
        return self.title

class UserModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="F.I.SH")
    
    # Faqat PDF va JPG fayllar uchun FileField ishlatamiz
    files = models.FileField(
        upload_to='files/', 
        verbose_name='shahodatnoma yoki diplom',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]
    )
    
    pasport = models.FileField(
        upload_to='files/', 
        verbose_name='ota yoki onasi pasporti',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]
    )
    
    id_card = models.FileField(
        upload_to='files/', 
        verbose_name='ID-karta yoki pasport', 
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]
    )
    
    # Faqat rasm uchun ImageField saqlaymiz
    photo = models.ImageField(upload_to='files_photo', verbose_name='3x4 rasim')
    
    created = models.DateTimeField(auto_now_add=True, blank=True)
    shaxar = models.CharField(max_length=350, verbose_name="yashash manzilingiz")
    number = PhoneNumberField(verbose_name="Telefon raqami")
    education = models.CharField(max_length=150, verbose_name="Qaysi O'qishni tugatgansiz")
    
    userFan = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name="Yo'nalishni tanlang")
    userTill = models.ForeignKey(Till, on_delete=models.CASCADE, verbose_name="Fanni tanlang")
    
    class Meta:
        verbose_name = "Ro'yxatdan o'tganlar"
        verbose_name_plural = "Ro'yxatdan o'tganlar"
    
    def __str__(self):
        return self.name