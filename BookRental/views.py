from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .models import Book, RentingPerson, BookRent
from .serializers import BookSerializer, RentingPersonSerializer, BookRentSerializer


class BookRentView(generics.ListCreateAPIView):
    queryset = BookRent.objects.all()
    serializer_class = BookRentSerializer


class BookRentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookRent.objects.all()
    serializer_class = BookRentSerializer


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RentingPersonView(generics.ListCreateAPIView):
    queryset = RentingPerson.objects.all()
    serializer_class = RentingPersonSerializer


class RentingPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentingPerson.objects.all()
    serializer_class = RentingPersonSerializer
