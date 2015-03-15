from django.conf.urls import patterns, url
from BookRental import views

urlpatterns = patterns(
    '',
    url(r'^v1/books-rented/$', view=views.RentedBookView.as_view()),
    url(r'^v1/books-rented/(?P<pk>[0-9]+)/$', view=views.RentedBookDetail.as_view()),
    url(r'^v1/books/$', view=views.BookView.as_view()),
    url(r'^v1/books/(?P<pk>[0-9]+)/$', view=views.BookDetail.as_view()),
    url(r'^v1/renting-persons/$', view=views.RentingPersonView.as_view()),
    url(r'^v1/renting-persons/(?P<pk>[0-9]+)/$', view=views.RentingPersonDetail.as_view()),
)
