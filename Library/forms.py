from django import forms
from .models import Book,Author,Category,Genre


class Bookforms(forms.ModelForm):
    book_bio_uz = forms.CharField()
    book_bio_ru = forms.CharField(required=False)
    book_bio_en = forms.CharField(required=False)

    category_uz = forms.CharField()
    category_ru = forms.CharField(required=False)
    category_en = forms.CharField(required=False)

    genre_uz = forms.CharField()
    genre_ru = forms.CharField(required=False)
    genre_en = forms.CharField(required=False)


    class Meta:
        model = Book
        exclude = ('book_bio','category','genre')
class Authorforms(forms.ModelForm):
    bio_uz = forms.CharField()
    bio_ru = forms.CharField(required=False)
    bio_en = forms.CharField(required=False)

    category_uz = forms.CharField()
    category_ru = forms.CharField(required=False)
    category_en = forms.CharField(required=False)

    genre_uz = forms.CharField()
    genre_ru = forms.CharField(required=False)
    genre_en = forms.CharField(required=False)

    class Meta:
        model = Author
        exclude = ('bio','category','genre')
