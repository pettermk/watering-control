from django.db.models.signals import post_save
from django.dispatch import receiver

from web.models import OnOffController
import logging

@receiver(post_save, sender=OnOffController)
def update_controller(sender, instance, **kwargs):
    # Do something useful
    pass
