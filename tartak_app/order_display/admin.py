from django.contrib import admin
from .models import Client, Order, Element
# Register your models here.


@admin.register(Client)
class PostAdmin(admin.ModelAdmin):
    list_display = ["first_name"]
    search_fields = ['first_name', 'last_name']
    



@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    list_display = ['client', 'created','due', 'status', 'slug']
    search_fields = ['client', 'due']
    raw_id_fields = ['client']
    date_hierarchy = 'due'
    ordering = ['status', 'due']
    
    
@admin.register(Element)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'width','height', 'length', 'volume', 'order', 'unit']
    search_fields = ['name', 'order']
    raw_id_fields = ['order']
    ordering = ['order']



