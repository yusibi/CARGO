from .models import Customer
from django.shortcuts import render, redirect
from django.db import IntegrityError


def index1(request):
    return render(request, 'polls/guest page.html')


def index2(request):
    return render(request, 'polls/user page.html')


def index3(request):
    return render(request, 'polls/admin page.html')


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



