from django.contrib import admin
from .models import Coffee
# Register your models here.
@admin.register(Coffee)
class AdminCoffee(admin.ModelAdmin):
    list_display=['id' , 'name','amount' , 'payment_id' , 'paid']