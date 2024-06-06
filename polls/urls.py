from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1, name='guest page'),
    path('user_page/', views.index2, name='display user page'),
    path('admin_page/', views.index3, name='display admin page'),
    path('registration/', views.register, name='register'),
    path('authorization_1/', views.authorization_1, name='author_1'),
    path('authorization_2/', views.authorization_2, name='author_2'),
    path('authorization_error/', views.authorization_error_1, name='authorization_error_1'),
    path('authorization_error/', views.authorization_error_2, name='authorization_error_2'),
    path('about_us/', views.show_info_about_us, name='ab_us'),
    path('service/', views.show_service, name='service'),
    path('order_delivery/', views.order_delivery, name='delivery'),
    #path('order_delivery/', views.order_save, name='delivery'),
    #path('order_deliveryy/', views.show_info, name='show_info'),
    #path('result/', views.show_res, name='res'),
    path('result/', views.show_res, name='res'),
    path('error/', views.show_er, name='er'),
    #path('polls/', views.index1, name='index2'),
    #path('my_deliveries/', views.show_my_del, name='my_dev'),
    #path('my_deliveries/', views.list_of_orders, name='my_dev'),
    path('list_of_orders/', views.show_list_of_orders, name='list'),

]

