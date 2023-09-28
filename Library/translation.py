from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Book, Author, Genre


class CategoryTranslation(TranslationOptions):
    fields = ('category_name',)

class BookTranslation(TranslationOptions):
    fields = ('book_bio', 'category', 'genre')

class AuthorTranslation(TranslationOptions):
    fields = ('bio', 'category', 'genre')

class GenreTranslation(TranslationOptions):
    fields = ('genre_name',)


translator.register(Category, CategoryTranslation)
translator.register(Book, BookTranslation)
translator.register(Author, AuthorTranslation)
translator.register(Genre, GenreTranslation)

