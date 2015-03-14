from rest_framework import serializers
from .models import Book, BookRent, RentingPerson


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book


class RentingPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentingPerson


class BookRentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRent




