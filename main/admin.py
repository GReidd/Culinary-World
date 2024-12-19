from django.contrib import admin
from main.models import Cards


# Register your models here.
@admin.register(Cards)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
