from rest_framework.serializers import ModelSerializer
from .models  import Category, Genre, Author, Book

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        
class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')
        
        
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')
        
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')