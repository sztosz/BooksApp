from rest_framework import serializers
from .models import Book, RentedBook, RentingPerson


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book


class RentingPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentingPerson


class RentedBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentedBook




