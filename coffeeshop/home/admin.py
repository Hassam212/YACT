from django.contrib import admin
from .models import Department, Drink, Table, OrderDrinks

# Register your models here.

admin.site.register(Department)
admin.site.register(Drink)
admin.site.register(Table)
admin.site.register(OrderDrinks)
