from django.urls import path
from .views import (
    payment,
    result,
    success,
    fail,
)

urlpatterns = [
    path('', payment, name='payment'),
    path('result/', result, name='payment_result'),
    path('success/', success, name='success'),
    path('failure/', fail, name='failure'),
]