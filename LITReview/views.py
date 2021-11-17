from itertools import chain

from django.db.models import CharField, Value, Q
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from review.models import Review
from ticket.forms import TicketForm
from ticket.models import Ticket
from user.models import User


def home_view(request):
    return render(request, 'index.html') 


@login_required
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


def create_user(request):
    # récupérer les données du formulaire
    username = request.POST.get("register_name")
    pass1 = request.POST.get("pass1")
    pass2 = request.POST.get("pass2")
    if pass1 == pass2 and not username_exists(username):
        user = User.objects.create_user(username, '', pass1)
        return HttpResponse("Votre compte a été créé. Connectez vous via l'écran de connexion") 
    elif pass1 != pass2:
        return HttpResponse("La confirmation du mot de passe ne correspond pas. Réessayez")
    else:
        return HttpResponse("Username déjà existant. Réessayez")
    print(username)
    print(pass1)
    print(pass2)
    # vérifs données du formulaire
    # création utilisateur
    # afficher vous etes bien créé ou erreur 

    return render(request, 'flux/flux.html', locals()) 


def username_exists(username):
    if User.objects.filter(username=username).exists():
        return True

    return False


def log_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('flux')
    else:
        return HttpResponse("Compte invalide. Réessayez")

def logout_user(request):
    logout(request)
    return redirect('/') 