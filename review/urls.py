from django.urls import path

from review.views import create_review_view

app_name = 'review'
urlpatterns = [
    path('', create_review_view, name='review'),

]
