from tkinter import Image

from rest_framework import serializers

from catalogue.models import Book, Author, Review, BookImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['FirstName', 'LastName', 'date_of_birth', 'date_of_death']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'book', 'date', 'review']

    def create(self, validated_data):
        book_pk = self.context['book_pk']
        Review.objects.create(book=book_pk, **validated_data)


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['image']

    def create(self, validated_data):
        book_pk = self.context['book_pk']
        return BookImage.objects.create(book=book_pk, **validated_data)



