from django.shortcuts import redirect, render

from ticket.forms import TicketForm

def create_ticket_view(request):
    if request.method == "GET":
        form = TicketForm
        return render(request, 'ticket/create_ticket.html', locals())
    elif request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        # TODO voir pour utiliser le request.FILES
        
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            img = request.POST.get("image")
            new_ticket.image = img
            new_ticket.save()
            # TODO coder la condition
            return redirect('flux')
        else :
            return redirect('flux')



