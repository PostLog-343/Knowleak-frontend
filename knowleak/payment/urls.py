from django.urls import path
from .views import (
    index,
    payment,
    result,
    success,
    fail,
)

urlpatterns = [
    path('', index, name='payment_index'),
    path('payment/', payment, name='payment'),
    path('result/', result, name='payment_result'),
    path('success/', success, name='success'),
    path('failure/', fail, name='failure'),
]