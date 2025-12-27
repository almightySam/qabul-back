from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from .models import Region, Gender, ApplicationType, Position, Post
from .forms import PostForm


User = get_user_model()


class PostModelTest(TestCase):
    """ Post modeli testlari """

    def setUp(self):
        self.region = Region.objects.create(name="Toshkent")
        self.gender = Gender.objects.create(name="Erkak")
        self.app_type = ApplicationType.objects.create(name="Shikoyat")
        self.position = Position.objects.create(name="Operator")
        self.user = User.objects.create_user(
            username="operator1",
            password="test1234",
            full_name="Ali Karimov",
            position=self.position
        )

    def test_create_post(self):
        """ Post muvaffaqiyatli yaratilishini test qiladi """
        post = Post.objects.create(
            last_name="Karimov",
            first_name="Ali",
            address="Toshkent, Chilonzor",
            tel_number="+998901112233",
            email="ali@example.com",
            topic="Internet muammosi",
            body="Menga internet juda sekin ishlayapti",
            region=self.region,
            gender=self.gender,
            application_type=self.app_type,
            to_user=self.user,
        )
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.last_name, "Karimov")
        self.assertEqual(post.to_user.username, "operator1")
        self.assertTrue(isinstance(post, Post))


class PostFormTest(TestCase):
    """ Post formasi uchun testlar """

    def setUp(self):
        self.region = Region.objects.create(name="Samarqand")
        self.gender = Gender.objects.create(name="Ayol")
        self.app_type = ApplicationType.objects.create(name="Taklif")
        self.position = Position.objects.create(name="Direktor")
        self.user = User.objects.create_user(
            username="direktor1",
            password="test1234",
            full_name="Dilnoza Qodirova",
            position=self.position
        )

    def test_valid_post_form(self):
        """ To‘liq to‘ldirilgan forma valid ekanligini tekshiradi """
        data = {
            'last_name': 'Qodirova',
            'first_name': 'Dilnoza',
            'address': 'Samarqand, Registon',
            'tel_number': '+998901234567',
            'email': 'dilnoza@example.com',
            'topic': 'Taklif haqida',
            'body': 'Yangi tizim joriy etish taklifi',
            'region': self.region.id,
            'gender': self.gender.id,
            'application_type': self.app_type.id,
            'to_user': self.user.id,
        }
        file = SimpleUploadedFile("test.txt", b"Test fayl mazmuni")
        form = PostForm(data=data, files={'files': file})
        self.assertTrue(form.is_valid())

    def test_invalid_phone_number(self):
        """ Telefon raqami noto‘g‘ri bo‘lsa, forma xato qaytaradi """
        data = {
            'last_name': 'Qodirova',
            'first_name': 'Dilnoza',
            'address': 'Samarqand, Registon',
            'tel_number': '12345',
            'email': 'dilnoza@example.com',
            'region': self.region.id,
            'gender': self.gender.id,
            'application_type': self.app_type.id,
            'to_user': self.user.id,
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('tel_number', form.errors)

    def test_empty_receiver(self):
        """ to_user va to_position ikkalasi ham bo‘sh bo‘lsa, xato bo‘lishi kerak """
        data = {
            'last_name': 'Aliyev',
            'first_name': 'Aziz',
            'address': 'Toshkent',
            'tel_number': '+998909876543',
            'email': 'aziz@example.com',
            'region': self.region.id,
            'gender': self.gender.id,
            'application_type': self.app_type.id,
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)


