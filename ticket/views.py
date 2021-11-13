from django.shortcuts import redirect, render

from ticket.forms import TicketForm

def show_ticket_view(request):
    return render(request, "ticket_snippet.html")

def create_ticket_view(request):
    if request.method == "GET":
        form = TicketForm
        return render(request, 'ticket/create_ticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flux')
        else :
            return redirect('flux')
