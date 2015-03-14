from django.db import models


class BookRent(models.Model):
    rented_date = models.DateField(verbose_name='Data wypożyczenia')
    rental_days = models.IntegerField(verbose_name='Czas wypożyczenia')

    renting_person = models.ForeignKey(RentingPerson)

    book = models.ForeignKey(Book)


class RentingPerson(models.Model):
    name = models.CharField(verbose_name='Imię')
    surname = models.CharField(verbose_name='Nazwisko')
    pesel = models.IntegerField(verbose_name='PESEL', max_length=13)


class Book(models.Model):
    name = models.CharField(verbose_name='Nazwa książki')
    isbn = models.IntegerField(verbose_name='ISBN')