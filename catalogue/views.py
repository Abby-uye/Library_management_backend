from tkinter import Image

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from catalogue.models import Book, Author, Review, BookImage
from catalogue.pagination import DefaultPagination
from catalogue.permissions import IsAdminOrReadOnly
from catalogue.serializers import BookSerializer, AuthorSerializer, ReviewSerializer, BookImageSerializer


# class BookList(ListCreateAPIView):
#     def get_queryset(self):
#         return Book.objects.all()
#
#     def get_serializer_class(self):
#         return BookSerializer


# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# def get(self, request, pk):
#     book = get_object_or_404(Book, id=pk)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def put(self, request, pk):
#     book = get_object_or_404(Book, id=pk)
#     serializer = BookSerializer(book, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def delete(self):
#     book = get_object_or_404(Book)
#     book.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# class AuthorList(ListCreateAPIView):
#     def get_queryset(self):
#         return Author.objects.all()
#
#     serializer_class = AuthorSerializer
#

# def get(self, request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# def post(self, request):
#     serializer = AuthorSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     def get_queryset(self):
#         return Author.objects.all()
#
#     def get_serializer_class(self):
#         return BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['FirstName', 'LastName']
    ordering_fields = ['FirstName']
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre', 'summary']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {"book_pk": self.kwargs["book_pk"]}


class ImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer

    def get_queryset(self):
        return BookImage.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {"book_pk": self.kwargs[ 'book_pk']}


    # def get(self, request, pk):
    #     author = get_object_or_404(Author, id=pk)
    #     serializer = AuthorSerializer(author)
    #     author_qrcode = segno.make_qr("Abby is a fine girl")
    #     author_qrcode.save("Abby.png")
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def put(self, request, pk):
    #     author = get_object_or_404(Author, id=pk)
    #     serializer = AuthorSerializer(author, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, request, pk):
    #     author = get_object_or_404(Author, id=pk)
    #     author.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#

# @api_view(['GET', 'PUT', 'DELETE'])
# def manipulate_author(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr("Abby is a fine girl")
#         author_qrcode.save("Abby.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
