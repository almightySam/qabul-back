from django import forms
from .models import (
    Bakalavr,
    Magistr,
    BakalavrCategory,
    MagistratCategory,
    QabulApplication, QabulCategory
)


class BakalavrCategoryForm(forms.ModelForm):
    class Meta:
        model = BakalavrCategory
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class MagistratCategoryForm(forms.ModelForm):
    class Meta:
        model = MagistratCategory
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BakalavrForm(forms.ModelForm):
    class Meta:
        model = Bakalavr
        fields = ['kategoriya', 'name', 'kunduzgi_kvota']

        widgets = {
            'kategoriya': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'kunduzgi_kvota': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MagistrForm(forms.ModelForm):
    class Meta:
        model = Magistr
        fields = ['kategorya', 'name', 'kunduzgi_kvota']

        widgets = {
            'kategorya': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'kunduzgi_kvota': forms.NumberInput(attrs={'class': 'form-control'}),
        }





class QabulCategoryForm(forms.ModelForm):
    class Meta:
        model = QabulCategory
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }




class QabulApplicationForm(forms.ModelForm):
    
    class Meta:
        model = QabulApplication
        fields = [
            'full_name', 'phone', 'address', 'education',
            'category', 'direction', 'language_level',
            'id_card', 'diploma', 'parent_passport', 'photo_3x4'
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Familiya, Ism, Otasining ismi"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "+998 90 123 45 67"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Manzilingizni kiriting"
            }),
            "education": forms.Select(attrs={
                "class": "form-control"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "language_level": forms.Select(attrs={
                "class": "form-control"
            }),
            "diploma": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "id_card": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "parent_passport": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "photo_3x4": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }
