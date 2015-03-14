from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from BookRental import views as book_rental_views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'BooksApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/books-rented/$', view=book_rental_views.BookRentView.as_view()),
    url(r'^api/v1/books-rented/(?P<pk>[0-9]+)/$', view=book_rental_views.BookRentDetail.as_view()),
    url(r'^api/v1/books/$', view=book_rental_views.BookView.as_view()),
    url(r'^api/v1/books/(?P<pk>[0-9]+)/$', view=book_rental_views.BookDetail.as_view()),
    url(r'^api/v1/renting-persons/$', view=book_rental_views.RentingPersonView.as_view()),
    url(r'^api/v1/renting-persons/(?P<pk>[0-9]+)/$', view=book_rental_views.RentingPersonDetail.as_view()),

)
