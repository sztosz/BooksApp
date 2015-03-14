from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .models import Book, RentingPerson, BookRent
from .serializers import BookSerializer, RentingPersonSerializer, BookRentSerializer


class BookRentView(generics.ListCreateAPIView):
    queryset = BookRent.objects.all()
    serializer_class = BookRentSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)



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






# class BookRentView(APIView):
#
#     def get(self, request, format=None):
#         rented_books = BookRent.objects.all()
#         serializer = BookRentSerializer(rented_books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookRentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class RentingPersonView(APIView):
#
#     def get(self, request, format=None):
#         renting_persons = RentingPerson.objects.all()
#         serializer = RentingPersonSerializer(renting_persons, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = RentingPersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookView(APIView):
#
#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
