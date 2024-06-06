from .models import Customer, Order
from django.shortcuts import render, redirect, HttpResponse
from django.db import IntegrityError
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from smtplib import SMTPAuthenticationError
from django.db.models import Q


def index1(request):
    return render(request, 'polls/guest page.html')


def index2(request):
    customer_count = Customer.objects.filter(role='a').count()
    return render(request, 'polls/user page.html', {'customer_count': customer_count})


def index3(request):
    customer_count = Customer.objects.filter(role='a').count()
    return render(request, 'polls/admin page.html', {'customer_count': customer_count})


def authorization_1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(login=username, password=password)
            if customer:
                if customer.role == 'a':
                    return redirect('display user page')  # URL-ім'я сторінки для замовників
                elif customer.role == 'b':
                    return redirect('display admin page')  # URL-ім'я сторінки для адміністраторів
        except Customer.DoesNotExist:
            return redirect('authorization_error_1')  # URL-ім'я сторінки з помилкою авторизації
    return render(request, 'polls/authorization_one.html')


def authorization_2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(login=username, password=password)
            if customer:
                if customer.role == 'a':
                    return redirect('display user page')  # URL-ім'я сторінки для замовників
                elif customer.role == 'b':
                    return redirect('display admin page')  # URL-ім'я сторінки для адміністраторів
        except Customer.DoesNotExist:
            return redirect('authorization_error_2')  # URL-ім'я сторінки з помилкою авторизації
    return render(request, 'polls/authorization_two.html')


def authorization_error_1(request):
    return render(request, 'polls/auth_error_1.html')


def authorization_error_2(request):
    return render(request, 'polls/auth_error_2.html')


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            user_first_name = request.POST.get('name')
            customer_phone_number = request.POST.get('phone_number')
            login = request.POST.get('login')
            password = request.POST.get('password1')
            role = request.POST.get('role')

            # Створення об'єкта Customer
            if role == 'admin':
                role = 'b'  # перетворення 'admin' на 'b' відповідно до вашого варіанту у моделі
            else:
                role = 'a'  # перетворення 'user' на 'a' відповідно до вашого варіанту у моделі
            customer = Customer(customer_second_name=username, customer_first_name=user_first_name, customer_phone_number=customer_phone_number, login=login, password=password, role=role)
            customer.save()
            if role == 'a':
                return redirect('display user page')
            elif role == 'b':
                return redirect('display admin page')
        except IntegrityError:
            return render(request, 'polls/reg_error.html')
    return render(request, 'polls/registration.html')


def show_info_about_us(request):
    return render(request, 'polls/about us.html')


def show_service(request):
    return render(request, 'polls/service.html')


def order_delivery(request):
    # Отримуємо пароль із запиту POST
    password = request.POST.get('password')

    # Перевіряємо чи існує клієнт з таким паролем
    if password:
        try:
            # Отримуємо клієнта за паролем
            customer = Customer.objects.get(password=password)
            return render(request, 'polls/order_delivery.html', {
                'customer_second_name': customer.customer_second_name,
                'customer_first_name': customer.customer_first_name,
                'customer_phone_number': customer.customer_phone_number
            })
        except Customer.DoesNotExist:
            # Повідомлення про помилку авторизації
            error_message = "Помилка авторизації. Будь ласка, введіть коректний пароль."
            # Повертаємо дані форми разом з повідомленням про помилку
            return render(request, 'polls/order_delivery.html', {'error_message': error_message})

    # Якщо метод запиту POST і другий виклик виключення Customer.DoesNotExist
    if request.method == 'POST':
        customer_phone_number = request.POST.get('phone_number')
        # Отримуємо об'єкт Customer на основі номера телефону
        customer, created = Customer.objects.get_or_create(customer_phone_number=customer_phone_number)

        # Отримуємо дані з форми
        customer_surname = request.POST.get('surname')
        customer_name = request.POST.get('name')
        email = request.POST.get('email')
        type = request.POST.get('type')
        wes = request.POST.get('weight')
        city_1 = request.POST.get('city_1')
        city_2 = request.POST.get('city_2')
        od_v = request.POST.get('od_v')
        date_1 = request.POST.get('date1')
        date_2 = request.POST.get('date2')
        discr = request.POST.get('discript')

        # Створюємо об'єкт Order з відповідними даними та зв'язуємо його з об'єктом Customer
        order = Order.objects.create(
            customer_second_name=customer_surname,
            customer_first_name=customer_name,
            customer_phone_number=customer,  # Тут використовуємо об'єкт Customer
            email=email,
            type=type,
            wes=wes,
            city_1=city_1,
            city_2=city_2,
            od_vumiry=od_v,
            date_1=date_1,
            date_2=date_2,
            discr=discr,
            status="Не оброблене"
        )
        order.save()
        return redirect('res')

    return render(request, 'polls/order_delivery.html')


#def order_save(request):
    #if request.method == 'POST':
     ##   customer_phone_number = request.POST.get('phone_number')
        # Отримати об'єкт Customer на основі номера телефону
     #   customer = Customer.objects.get(customer_phone_number=customer_phone_number)

        # Отримати дані з форми
     #   customer_surname = request.POST.get('surname')
     #   customer_name = request.POST.get('name')
     #   email = request.POST.get('email')
     #   type = request.POST.get('type')
     #   wes = request.POST.get('weight')
     #   city_1 = request.POST.get('city_1')
     #   city_2 = request.POST.get('city_2')
     #   od_v = request.POST.get('od_v')
     #   date_1 = request.POST.get('date1')
     #   date_2 = request.POST.get('date2')
     #   discr = request.POST.get('discript')

        # Створити об'єкт Order з відповідними даними та зв'язати його з об'єктом Customer
     #   order = Order.objects.create(
     #       customer_second_name=customer_surname,
      #      customer_first_name=customer_name,
     #       customer_phone_number=customer,  # Тут використовуємо об'єкт Customer
      #      email=email,
      #      type=type,
      #      wes=wes,
     #       city_1=city_1,
     #       city_2=city_2,
     #       od_vumiry=od_v,
     #       date_1=date_1,
      #      date_2=date_2,
     #      discr=discr,
     #       status="a"
     #   )
     #   order.save()
    #    return redirect('res')
  #  return render(request, 'polls/order_delivery.html')


def send_notification_email(subject, plain_message, recipient_list, html_message=None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = ', '.join(recipient_list)

    # Attach the plain text and HTML message parts
    msg.attach(MIMEText(plain_message, 'plain'))
    if html_message:
        msg.attach(MIMEText(html_message, 'html'))

    try:
        # Connect to the SMTP server and send the message
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, recipient_list, msg.as_string())
        #except SMTPAuthenticationError as e:
        #return render(request, 'polls/post_error.html')
        # Тут можна обробити помилку подальше, наприклад, відправити повідомлення адміністратору
    except Exception as e:
        print(f"An error occurred while sending email: {e}")


def show_er(request):
    return render(request, 'polls/post_error.html')


def show_res(request):
    return render(request, 'polls/suc_order_mes.html')
