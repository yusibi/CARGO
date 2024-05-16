from django.db import models
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    ROLES = (
        ('a', 'Замовник'),
        ('b', 'Адміністратор'),
    )
    customer_second_name = models.CharField(max_length=50, verbose_name='Прізвище')
    customer_first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    customer_phone_number = models.CharField(max_length=13, unique=True, verbose_name='Номер телефону')
    login = models.CharField(validators=[MinLengthValidator(5)], max_length=20, unique=True, verbose_name='Логін')
    password = models.CharField(unique=True, validators=[MinLengthValidator(5)], max_length=20, verbose_name="Пароль")
    role = models.CharField(max_length=1, choices=ROLES, verbose_name='Роль')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ['id']