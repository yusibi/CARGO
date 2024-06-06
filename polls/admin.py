from django.contrib import admin
from . models import Customer, Order


class Customer_Admin(admin.ModelAdmin):
    list_display = ('id', 'customer_second_name', 'customer_first_name', 'customer_phone_number', 'login', 'password', 'role')
    list_filter = ('customer_second_name', 'customer_first_name', 'role',)
    search_fields = ('customer_second_name', 'customer_first_name', 'customer_phone_number', 'password', 'login',)


class Order_Admin(admin.ModelAdmin):
    list_display = ('id', 'customer_second_name', 'customer_first_name', 'customer_phone_number', 'email', 'type', 'wes', 'od_vumiry', 'city_1', 'city_2', 'date_1', 'date_2', 'discr', 'status')
    list_filter = ('customer_second_name', 'customer_first_name', 'city_1', 'city_2', 'date_1', 'date_2', 'status')
    search_fields = ('customer_second_name', 'customer_first_name', 'city_1', 'city_2', 'date_1', 'date_2', 'status',)


admin.site.register(Customer, Customer_Admin)
admin.site.register(Order, Order_Admin)
