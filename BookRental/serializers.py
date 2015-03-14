from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import Book, BookRent, RentingPerson


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        # fields = ('name', 'isbn')


class RentingPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentingPerson
        # fields = ('name', 'surname', 'pesel')


class BookRentSerializer(serializers.ModelSerializer):
    # renting_person = RentingPersonSerializer()
    # book = BookSerializer()

    class Meta:
        model = BookRent
        # fields = ('rented_date', 'rental_days', 'renting_person', 'book')



