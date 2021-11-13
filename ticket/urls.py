from django.urls import path

from ticket.views import create_ticket_view


app_name = 'ticket'
urlpatterns = [
    path('', create_ticket_view, name='ticket'),

]
