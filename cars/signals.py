from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from django.contrib.auth.models import User



def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value_sale=Sum('sale_value')
    )['total_value_sale'] or 0 

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

