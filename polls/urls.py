from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1, name='guest page'),
    path('user_page/', views.index2, name='display user page'),
    path('admin_page/', views.index3, name='display admin page'),
    path('registration/', views.register, name='register'),
    path('authorization/', views.authorization, name='author'),
    path('authorization_error/', views.authorization_error, name='authorization_error'),
    path('about_us/', views.show_info_about_us, name='ab_us'),
    path('service/', views.show_service, name='service'),
    #path('polls/', views.index1, name='index2'),

]