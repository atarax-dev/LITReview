from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from review.forms import ReviewForm
from ticket.models import get_ticket_with_id

def create_review_view(request, ticket_id):
    if request.method == "GET":
        form = ReviewForm
        ticket = get_ticket_with_id(ticket_id)
        print("ticket id =", ticket_id)
        print("ticket= ",ticket)
        print ("request.POST= ", request.POST)
        print ("request.GET= ", request.GET)
        print(ticket.title)
        
        return render(request, 'review/create_review.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST, request.FILES) 
        print ("request.POST= ", request.POST)
        print ("form.data=", form.data)
        print("ticket id=", ticket_id)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.ticket_id = ticket_id
            new_review.save()
            # TODO coder la condition
            return redirect('flux')
        else :
            return HttpResponse("raté mais va")

