from django.contrib import admin
from django.urls import path ,include
from.import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    
    path('login/',views.login,name='login'),
   path('signup',views.signup,name='signup'),
   path('books',views.books,name='books'),
   path('loginpage',views.loginpage,name='loginpage'),
   path('buy',views.buy,name='buy'),
]

