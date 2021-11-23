from django.urls import path

from review.views import create_onestep_review_view, create_review_view

app_name = 'review'
urlpatterns = [
    path('', create_review_view, name='review'),
    path('<int:ticket_id>/', create_review_view),
    path('one_step_review/', create_onestep_review_view, name='onestep'),
]
