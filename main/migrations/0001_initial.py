# Generated by Django 5.0.2 on 2024-03-05 04:23

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_summa', models.PositiveIntegerField(verbose_name='Summa')),
            ],
            options={
                'verbose_name': 'Cassa',
                'verbose_name_plural': 'Kassa',
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Raqami')),
            ],
            options={
                'verbose_name': 'Garage',
                'verbose_name_plural': 'Garaj',
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
            ],
            options={
                'verbose_name': 'Occupation',
                'verbose_name_plural': 'Soxa',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='FIO')),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(code='password number', message='Invalid password number', regex='(?=^.{8}$)((?=.*\\d)|(?=.*\\W+))(?![.\n])(?=.[A-Z])(?=.*[a-z]).*$')], verbose_name='Parol')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Yoshi')),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalid phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')], verbose_name='Telefon raqam')),
                ('email', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid email', message='Invalide email', regex='^[-\\w.]+@([A-z0-9]+\\.)+[A-z]{2,4}$')], verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Foydalanuvchilar',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Yashash manzil')),
                ('experience', models.IntegerField()),
                ('wages', models.IntegerField(verbose_name='Oylik maoshi')),
                ('start_work_time', models.TimeField(verbose_name='Ish boshlash vaqti')),
                ('end_work_time', models.TimeField(verbose_name='Ish tugash vaqti')),
                ('day_off', models.DateField(blank=True, null=True, verbose_name='Dam olish kuni')),
                ('queue', models.IntegerField(default=0, verbose_name='Navbat holati')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='employee_qr_codes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USER')),
                ('garage', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.garage', verbose_name='Garaji')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.occupation', verbose_name='Kasbi')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Xodimlar',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.uuid4, max_length=36, unique=True, verbose_name='Buyurtma kodi')),
                ('owner_name', models.CharField(max_length=255, verbose_name='Mijoz FIO')),
                ('owner_phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalide phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')], verbose_name='Mijozning telefon raqami')),
                ('owner_car_number', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalide car number', regex='^[\x00-9]{2}[A-Z][0-9]{3}[A-Z]{2}$')], verbose_name='Mijozning avtomobil raqami')),
                ('car_passport_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Invalide passport number', regex='^[A-Z]{3}[0-9]{7}$')], verbose_name='Mijozning avtomobil passportining raqami')),
                ('status', models.CharField(choices=[(1, 'is waiting'), (2, 'is being corrected'), (3, 'finished'), ('is waiting', 'is waiting'), ('is being corrected', 'is being corrected'), ('finished', 'finished')], max_length=18)),
                ('problem', models.TextField(blank=True, null=True, verbose_name='Muammo')),
                ('service_cost', models.IntegerField(blank=True, null=True, verbose_name='Hizmat narxi')),
                ('start_date', models.DateField(auto_now=True, verbose_name='Buyurtma boshlangan sanasi')),
                ('start_time', models.TimeField(auto_now=True, verbose_name='Buyurtma boshlangan vaqti')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Tugalangan sanasi')),
                ('end_time', models.TimeField(blank=True, null=True, verbose_name='Tugalangan vaqqti')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='order_qr_codes/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Hodim')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Buyurtma',
                'unique_together': {('car_passport_number', 'start_date', 'start_time')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'comment'), ('2', 'camplain'), ('3', 'suggestion'), ('comment', 'comment'), ('camplain', 'camplain'), ('suggestion', 'suggestion')], max_length=10, verbose_name='Turi')),
                ('text', models.TextField(verbose_name='Jumla')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Buyurtma')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.uuid4, max_length=36, unique=True, verbose_name="To'lov kodi")),
                ('payment', models.PositiveIntegerField(verbose_name="To'lov sumasi")),
                ('data', models.DateField(auto_now=True, verbose_name="To'lov sanasi")),
                ('payment_type', models.CharField(choices=[('1', 'card'), ('2', 'cash'), ('3', 'other '), ('card', 'card'), ('cash', 'cash'), ('other', 'other')], max_length=5, verbose_name="To'lov turi")),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='payment_qr_codes/')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Buyurtma')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': "To'lov",
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_answer', models.TextField(verbose_name='Tekshiruv natijasi')),
                ('things_done', models.TextField(verbose_name='Qilingan ishlar')),
                ('total_cost', models.PositiveIntegerField(verbose_name='Xarajatlar')),
                ('total_benefit', models.PositiveIntegerField(verbose_name='Foyda')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee', verbose_name='Hodim')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Buyurtma')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Xisobot',
            },
        ),
    ]