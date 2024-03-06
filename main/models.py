from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.exceptions import ValidationError
import uuid

# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name='FIO')
    password = models.CharField(max_length=255, verbose_name='Parol', validators=[
        RegexValidator(
            regex='(?=^.{8}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.[A-Z])(?=.*[a-z]).*$',
            message='Invalid password number',
            code = 'password number'
        )
    ])
    age = models.IntegerField(verbose_name='Yoshi', null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    email = models.CharField(max_length=255, unique=True, verbose_name='Email', validators=[
        RegexValidator(
            regex='^[-\w.]+@([A-z0-9]+\.)+[A-z]{2,4}$',
            message = 'Invalide email',
            code = 'Invalid email'
        )
    ])

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'



class Employee(models.Model):
    user = models.OneToOneField(to='User', verbose_name='USER', on_delete=models.CASCADE)
    address = models.TextField(verbose_name='Yashash manzil')
    occupation = models.ForeignKey(to='Occupation', verbose_name='Kasbi', on_delete=models.CASCADE)
    garage = models.OneToOneField(to='Garage', null=True, blank=True, verbose_name='Garaji', on_delete=models.CASCADE)
    experience = models.IntegerField()
    wages = models.IntegerField(verbose_name='Oylik maoshi')
    start_work_time = models.TimeField(verbose_name='Ish boshlash vaqti')
    end_work_time = models.TimeField(verbose_name='Ish tugash vaqti')
    day_off = models.DateField(null=True, blank=True, verbose_name='Dam olish kuni')
    queue = models.IntegerField(default=0, verbose_name='Navbat holati')
    qr_code = models.ImageField(upload_to='employee_qr_codes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Xodimlar'

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.user.username} + {self.garage.number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


class Order(models.Model):
    employee = models.ForeignKey(to='Employee', verbose_name='Hodim', on_delete=models.CASCADE)
    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4, verbose_name='Buyurtma kodi')
    owner_name = models.CharField(max_length=255, verbose_name='Mijoz FIO')
    owner_phone_number = models.CharField(max_length=13, verbose_name='Mijozning telefon raqami', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    owner_car_number = models.CharField(max_length=8, verbose_name='Mijozning avtomobil raqami', validators=[
        RegexValidator(
            regex='^[\0-9]{2}[A-Z][0-9]{3}[A-Z]{2}$',
            message = 'Invalide car number',
            code = 'Invalid number'
        )
    ])
    car_passport_number = models.CharField(max_length=10, verbose_name='Mijozning avtomobil passportining raqami', validators=[
        RegexValidator(
            regex='^[A-Z]{3}[0-9]{7}$',
            message='Invalide passport number',
            code = 'Invalid number'
        )
    ])
    status = models.CharField(max_length=18, choices=(
        (1, 'is waiting'),
        (2, 'is being corrected'),
        (3, 'finished'),
        ('is waiting', 'is waiting'),
        ('is being corrected', 'is being corrected'),
        ('finished', 'finished')
    ))
    problem = models.TextField(verbose_name='Muammo', null=True, blank=True)
    service_cost = models.IntegerField(verbose_name='Hizmat narxi', null=True, blank=True)
    start_date = models.DateField(auto_now=True, verbose_name='Buyurtma boshlangan sanasi',)
    start_time = models.TimeField(auto_now=True, verbose_name='Buyurtma boshlangan vaqti')
    end_date = models.DateField(null=True, blank=True, verbose_name='Tugalangan sanasi')
    end_time = models.TimeField(null=True, blank=True, verbose_name='Tugalangan vaqqti')
    qr_code = models.ImageField(upload_to='order_qr_codes/', blank=True, null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Buyurtma'
        unique_together = ['car_passport_number', 'start_date', 'start_time']

    def clean(self):
        if self.employee.day_off == self.start_date:
            raise ValidationError('On this day the master rests')

    def clean(self):
        if self.start_date < self.end_date:
            raise ValidationError('The date of acceptance of the order should not be less than the date of completion')

    def clean(self):
        if self.start_date == self.end_date:
            if self.start_time < self.end_time:
                raise ValidationError('The time of receiving the order should not be less than the time of completion')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.code}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)

        self.qr_code.save(f'qr_code_{self.code}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


class Payment(models.Model):
    order = models.OneToOneField(to='Order', verbose_name='Buyurtma', on_delete=models.CASCADE)
    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4, verbose_name="To'lov kodi")
    payment = models.PositiveIntegerField(verbose_name="To'lov sumasi")
    data = models.DateField(auto_now=True, verbose_name="To'lov sanasi")
    payment_type = models.CharField( max_length=5, verbose_name="To'lov turi", choices=(
        ('1', 'card'),
        ('2', 'cash'),
        ('3', 'other '),
        ('card', 'card'),
        ('cash', 'cash'),
        ('other', 'other')
    ))
    qr_code = models.ImageField(upload_to='payment_qr_codes/', blank=True, null=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "To'lov"

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            border=3,
            box_size=5,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.code}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)


class Report(models.Model):
    employee = models.ForeignKey(to='Employee', verbose_name='Hodim', on_delete=models.CASCADE)
    order = models.OneToOneField(to='Order', verbose_name='Buyurtma', on_delete=models.CASCADE)
    analysis_answer = models.TextField(verbose_name='Tekshiruv natijasi')
    things_done = models.TextField(verbose_name='Qilingan ishlar')
    total_cost = models.PositiveIntegerField(verbose_name='Xarajatlar')
    total_benefit = models.PositiveIntegerField(verbose_name='Foyda')

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Xisobot"


class Cassa(models.Model):
    total_summa = models.PositiveIntegerField(verbose_name='Summa')

    class Meta:
        verbose_name = "Cassa"
        verbose_name_plural = "Kassa"


class Garage(models.Model):
    number = models.IntegerField(unique=True, verbose_name='Raqami')

    class Meta:
        verbose_name = "Garage"
        verbose_name_plural = "Garaj"


class Occupation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Occupation'
        verbose_name_plural = 'Soxa'


class Comment(models.Model):
    order = models.ForeignKey(to='Order', verbose_name='Buyurtma', on_delete=models.CASCADE)
    type = models.CharField(max_length=10,verbose_name='Turi', choices=(
        ('1', 'comment'),
        ('2', 'camplain'),
        ('3', 'suggestion'),
        ('comment', 'comment'),
        ('camplain', 'camplain'),
        ('suggestion', 'suggestion')
    ))
    text = models.TextField(verbose_name='Jumla')
    create_at = models.DateTimeField(auto_now=True)


