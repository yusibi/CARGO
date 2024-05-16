from django.contrib import admin
from . models import Customer


class Customer_Admin(admin.ModelAdmin):
    list_display = ('id', 'customer_second_name', 'customer_first_name', 'customer_phone_number', 'login', 'password', 'role')
    list_filter = ('customer_second_name', 'customer_first_name', 'role',)
    search_fields = ('customer_second_name', 'customer_first_name', 'customer_phone_number', 'password', 'login',)


admin.site.register(Customer, Customer_Admin)

