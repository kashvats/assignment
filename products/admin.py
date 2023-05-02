from django.contrib import admin
from .models import User,product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ["item_name","item_image","price"]
    search_fields = ["item_name"]

admin.site.register(product, productAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "uuid", "created_at"]
    search_fields = ("id", "email", "uuid", "created_at")


admin.site.register(User, UserAdmin)