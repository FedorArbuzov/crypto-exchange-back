from django.contrib import admin

from deals.models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass