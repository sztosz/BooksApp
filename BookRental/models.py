from django.db import models


class RentingPerson(models.Model):
    name = models.CharField(verbose_name='Imię', max_length=20)
    surname = models.CharField(verbose_name='Nazwisko', max_length=20)
    pesel = models.CharField(verbose_name='PESEL', max_length=13)

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.surname)

    def __str__(self):
        return self.__unicode__()


class Book(models.Model):
    title = models.CharField(verbose_name='Nazwa książki', max_length=100)
    isbn = models.CharField(verbose_name='ISBN', max_length=13)

    def __unicode__(self):
        return '{0} - ISBN: {1}'.format(self.name, self.isbn)

    def __str__(self):
        return self.__unicode__()


class RentedBook(models.Model):
    rented_date = models.DateField(verbose_name='Data wypożyczenia')
    rental_days = models.IntegerField(verbose_name='Czas wypożyczenia')

    renting_person = models.ForeignKey(RentingPerson)

    book = models.ForeignKey(Book)

    def __unicode__(self):
        return '{0}: From {1}, for {2} days'.format(self.name, self.rented_date, self.rental_days)

    def __str__(self):
        return self.__unicode__()






