from django.shortcuts import redirect, render

from ticket.forms import TicketForm


def create_ticket_view(request):
    if request.method == "GET":
        form = TicketForm
        return render(request, 'ticket/create_ticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        img = request.POST.get("image")
        form.image = img

        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            
            new_ticket.save()
            return redirect('flux')
        else:
            return render(request, 'ticket/create_ticket.html', locals())
