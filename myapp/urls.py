from django.urls import *
from myapp.views import *

urlpatterns = [
    path('', index, name="index"),
    path('employee', employee, name="employee"),
    path('product', product, name="product"),
    path('contact', contact, name="contact"),
]