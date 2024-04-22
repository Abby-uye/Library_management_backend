from rest_framework import serializers

from catalogue.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['FirstName', 'LastName', 'date_of_birth', 'date_of_death']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail'
    #)

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
