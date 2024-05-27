from .models import Customer
from django.shortcuts import render, redirect
from django.db import IntegrityError


def index1(request):
    return render(request, 'polls/guest page.html')


def index2(request):
    customer_count = Customer.objects.filter(role='a').count()
    return render(request, 'polls/user page.html', {'customer_count': customer_count})


def index3(request):
    customer_count = Customer.objects.filter(role='a').count()
    return render(request, 'polls/admin page.html', {'customer_count': customer_count})


def authorization(request):
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
            return redirect('authorization_error')  # URL-ім'я сторінки з помилкою авторизації
    return render(request, 'polls/authorization.html')


def authorization_error(request):
    return render(request, 'polls/auth_error.html')


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
                return redirect('display admin page.css')
        except IntegrityError:
            return render(request, 'polls/reg_error.html')
    return render(request, 'polls/registration.html')

def show_info_about_us(request):
    return render(request, 'polls/about us.html')