from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand','plate','factory_year', 'model_year', 'purchase_value', 'sale_value', 'sold')
    search_fields = ('model', 'brand', 'plate')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)