from rest_framework import serializers
from .models import Book, RentedBook, RentingPerson


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book


class RentingPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentingPerson


class RentedBookSerializer(serializers.ModelSerializer):
    book = serializers.CharField()
    renting_person = serializers.CharField()

    class Meta:
        model = RentedBook
        fields = ('id', 'rented_date', 'rental_days', 'renting_person', 'book', 'is_overdue')

    def create(self, validated_data):
        book = Book.objects.get(title=validated_data['book'])
        name, surname = validated_data['renting_person'].split()
        renting_person = RentingPerson.objects.get(name=name, surname=surname)

        rented_book = RentedBook(rented_date=validated_data['rented_date'], rental_days=validated_data['rental_days'],
                                 renting_person=renting_person, book=book)
        rented_book.save()
        return rented_book

    def update(self, instance, validated_data):
        name, surname = validated_data['renting_person'].split()
        instance.renting_person = RentingPerson.objects.get(name=name, surname=surname)
        instance.book = Book.objects.get(title=validated_data['book'])
        instance.rented_date = validated_data['rented_date']
        instance.rental_days = validated_data['rental_days']
        instance.save()
        return instance






