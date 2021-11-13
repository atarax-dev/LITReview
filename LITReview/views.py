from itertools import chain

from django.db.models import CharField, Value, Q
from django.http import request
from django.shortcuts import render

from review.models import Review
from ticket.forms import TicketForm
from ticket.models import Ticket


def home_view(request):
    return render(request, 'index.html') 

def flux_view(request):
    # reviews = get_users_viewable_reviews(request.user)
    # reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = get_users_viewable_tickets()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = tickets
    # posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
    return render(request, 'flux/flux.html', context={'posts': posts})

def get_users_viewable_reviews(user):
    # TODO 
    pass

def get_users_viewable_tickets():
    tickets_list = Ticket.objects.all()
    return tickets_list
    

def abos_view(request):
    return render(request, 'abonnements/abos.html')

def posts_view(request):
    return render(request, 'posts/posts.html')