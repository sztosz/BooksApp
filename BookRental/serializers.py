from rest_framework import serializers
from .models import Book, BookRent, RentingPerson


class BookRentSerializer(serializers.ModelSerializer):
    pass