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

    def __str__(self):
        return self.customer_phone_number


class Order(models.Model):
    STATUSES = (
        ('Не оброблене', 'Не оброблене'),
        ('Прийняте', 'Прийняте'),
        ('У виконанні', 'У виконанні'),
        ('Виконане', 'Виконане'),
    )
    customer_second_name = models.CharField(max_length=50, verbose_name='Прізвище')
    customer_first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    customer_phone_number = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Номер телефону')
    email = models.CharField(max_length=50, verbose_name='Електронна пошта')
    type = models.CharField(max_length=50, verbose_name='Тип доставки')
    wes = models.IntegerField(verbose_name='Кількість вантажу')
    city_1 = models.CharField(max_length=50, verbose_name='Місто відпр.')
    city_2 = models.CharField(max_length=50, verbose_name='Місто приб.')
    od_vumiry = models.CharField(max_length=10, verbose_name='Одиниця виміру')
    date_1 = models.DateField(verbose_name='Дата відправ.')
    date_2 = models.DateField(verbose_name='Дата приб.')
    discr = models.TextField(verbose_name='Опис вантажу')
    status = models.CharField(max_length=20, choices=STATUSES, default='Не оброблене', verbose_name='Статус')

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        ordering = ['id']

