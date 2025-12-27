from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Murojaat (Post) modeli uchun forma.
    Foydalanuvchi tomonidan yuboriladigan barcha ma'lumotlarni qabul qiladi.
    """

    class Meta:
        model = Post
        fields = [
            'last_name', 'first_name', 'address', 'tel_number', 'email',
            'topic', 'body', 'region', 'gender', 'application_type',
            'files', 'to_user', 'to_position'
        ]
        widgets = {
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Familiyangizni kiriting'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Ismingizni kiriting'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Manzilingizni kiriting'
            }),
            'tel_number': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': '+998901234567'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'example@gmail.com'
            }),
            'topic': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Murojaatning qisqacha mazmuni'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5, 'placeholder': 'Murojaat matnini kiriting...'
            }),
            'region': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'application_type': forms.Select(attrs={'class': 'form-select'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'to_user': forms.Select(attrs={'class': 'form-select'}),
            'to_position': forms.Select(attrs={'class': 'form-select'}),
        }

    # Qo‘shimcha validatsiya (masalan, telefon raqami formati)
    def clean_tel_number(self):
        tel = self.cleaned_data.get('tel_number')
        if tel and not tel.startswith('+998'):
            raise forms.ValidationError("Telefon raqami +998 bilan boshlanishi kerak!")
        if len(tel) < 9:
            raise forms.ValidationError("Telefon raqami juda qisqa!")
        return tel

    # Agar foydalanuvchi ham, lavozim ham bo‘sh bo‘lsa — xato
    def clean(self):
        cleaned_data = super().clean()
        to_user = cleaned_data.get('to_user')
        to_position = cleaned_data.get('to_position')

        if not to_user and not to_position:
            raise forms.ValidationError("Iltimos, murojaatni qabul qiluvchi foydalanuvchi yoki lavozimni tanlang.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Foydalanuvchi nomi'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Parol'
    }))