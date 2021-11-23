from django.shortcuts import redirect, render

from review.forms import ReviewForm
from ticket.forms import TicketForm
from ticket.models import get_ticket_with_id


def create_review_view(request, ticket_id):

    if request.method == "GET":
        form = ReviewForm
        ticket = get_ticket_with_id(ticket_id)

        return render(request, 'review/create_review.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST, request.FILES) 

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.ticket_id = ticket_id
            new_review.save()
            return redirect('flux')
        else:
            return render(request, 'review/create_review.html', locals())


def create_onestep_review_view(request):

    if request.method == "GET":
        form1 = TicketForm
        form2 = ReviewForm
    
        return render(request, "review/create_onestep_review.html", locals())
    
    elif request.method == "POST":
        form1 = TicketForm(request.POST, request.FILES)  
        form2 = ReviewForm(request.POST, request.FILES)
        img = request.POST.get("image")
        form1.image = img
        if form1.is_valid():
            new_ticket = form1.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            if form2.is_valid():
                new_review = form2.save(commit=False)
                new_review.user = request.user
                new_review.ticket_id = new_ticket.id
                new_review.save()
                return redirect('flux')
            else:
                return render(request, "review/create_onestep_review.html", locals())
        else:
            return render(request, "review/create_onestep_review.html", locals())
