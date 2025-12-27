from django import forms
from .models import UserModel, Education, Till
from phonenumber_field.phonenumber import PhoneNumber
import phonenumbers
from phonenumbers import PhoneNumberFormat

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'number', 'shaxar', 'education', 'userFan', 'userTill', 'files', 'id_card', 'pasport', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'F.I.SH kiriting', 'class': 'form-control'}),
            'number': forms.TextInput(attrs={'placeholder': 'Masalan: +998901234567', 'class': 'form-control'}),
            'shaxar': forms.TextInput(attrs={'placeholder': 'Shahar yoki viloyat', 'class': 'form-control'}),
            'education': forms.TextInput(attrs={'placeholder': 'Masalan: O‘rta maxsus, Oliy', 'class': 'form-control'}),
            'userFan': forms.Select(attrs={'class': 'form-control'}),
            'userTill': forms.Select(attrs={'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'id_card': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pasport': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'F.I.SH (Familya, Ism, Otasining ismi)',
            'number': 'Telefon raqami',
            'shaxar': 'Yashash manzilingiz',
            'education': 'Qaysi o‘qishni tugatgansiz',
            'userFan': 'Yo‘nalish',
            'userTill': 'Til bilish darajasi',
            'files': 'Shahodatnoma yoki diplom',
            'id_card': 'ID karta yoki pasport',
            'pasport': 'Ota yoki onasi pasporti',
            'photo': '3x4 rasim',
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['userFan'].queryset = Education.objects.all()
        self.fields['userTill'].queryset = Till.objects.all()
        for field in self.fields:
            self.fields[field].required = True

