from django.conf.urls import patterns, include, url
from django.contrib import admin
from BookRental import urls as book_rental_urls

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'BooksApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(book_rental_urls)),


)
