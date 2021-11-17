from django.shortcuts import redirect, render

from review.forms import ReviewForm

def create_review_view(request, ticket_id=None):
    if request.method == "GET":
        form = ReviewForm
        return render(request, 'review/create_review.html', locals())
    elif request.method == "POST":
        form = ReviewForm(request.POST, request.FILES) 
        # TODO trouver comment récuperer ce putain de ticket id (ticket_snippet.html)
        print ("request.POST= ",request.POST)
        print ("form.data=",form.data)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.ticket = ticket_id
            new_review.save()
            # TODO coder la condition
            return redirect('flux')
        else :
            form = ReviewForm
            return render(request, 'review/create_review.html', locals())

