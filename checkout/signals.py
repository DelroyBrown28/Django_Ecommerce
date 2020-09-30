from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save=OrderLineItem)
def update_on_save(sender, created, **kwargs):
    # Update order total on lineitem update/create

    instance.order.update_total()


@receiver(post_delete=OrderLineItem)
def update_on_save(sender, **kwargs):
    # Update order total on lineitem delete

    instance.order.update_total()
