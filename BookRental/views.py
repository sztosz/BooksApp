from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .models import Book, RentingPerson, RentedBook
from .serializers import BookSerializer, RentingPersonSerializer, RentedBookSerializer


class RentedBookView(generics.ListCreateAPIView):
    queryset = RentedBook.objects.all()
    serializer_class = RentedBookSerializer


class RentedBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentedBook.objects.all()
    serializer_class = RentedBookSerializer


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
