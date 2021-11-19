from itertools import chain

from django.db.models import CharField, Value, Q
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from review.forms import ReviewForm


from review.models import Review
from ticket.forms import TicketForm
from ticket.models import Ticket
from user.models import User


def home_view(request):
    return render(request, 'index.html') 


@login_required
def flux_view(request):
    reviews = get_all_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = get_all_tickets()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
    answered_tickets = get_user_answered_tickets(request.user)
    return render(request, 'flux/flux.html', context={'posts': posts, 'answered_tickets':answered_tickets})

def get_all_reviews(user):
    reviews_list = Review.objects.all()
    return reviews_list 


def get_all_tickets():
    tickets_list = Ticket.objects.all()
    return tickets_list


def get_user_answered_tickets(userx):
    reviews_list = Review.objects.filter(user= userx)
    answers_list = []
    for review in reviews_list:
        answer = review.ticket
        answers_list.append(answer)
    return answers_list
    

def abos_view(request):
    return render(request, 'abonnements/abos.html')

def posts_view(request):
   
    reviews = get_user_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = get_user_tickets(request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    return render(request, 'posts/posts.html', context={'posts': posts})

def get_user_reviews(userx):
    reviews_list = Review.objects.filter(user= userx)
    return reviews_list 

def get_user_tickets(userx):
    tickets_list = Ticket.objects.filter(user= userx)
    return tickets_list

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

def modify_view(request, content_type, content_id):
    if request.method == "GET":
        if content_type == "REVIEW":
            requested_content = Review.objects.get(pk= content_id)
            form = ReviewForm(instance=requested_content)
            
        elif content_type == "TICKET":
            requested_content = Ticket.objects.get(pk= content_id)
            form = TicketForm(instance=requested_content)

        return render(request, 'ticket/modify.html', locals())
    elif request.method == "POST" and content_type == "REVIEW":
        instance_review = Review.objects.get(pk= content_id)
        form = ReviewForm(request.POST, request.FILES, instance=instance_review)
        form_review = form.save(commit=False)
        if form.is_valid():
            form_review.save()
        return redirect('posts')
    elif request.method == "POST" and content_type == "TICKET":
        instance_ticket = Ticket.objects.get(pk= content_id)
        form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        form_ticket = form.save(commit=False)
        if form.is_valid():
            form_ticket.save()
        return redirect('posts')
    else :
        return redirect('flux')


def delete_view(request, content_type, content_id):
    if content_type == "REVIEW":
        requested_content = Review.objects.get(pk= content_id)
        requested_content.delete()
        
    elif content_type == "TICKET":
        requested_content = Ticket.objects.get(pk= content_id)
        requested_content.delete()

    return redirect('posts')