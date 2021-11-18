from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


def get_ticket_with_id(ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return ticket 


