from django.contrib import admin
from .models import Category,Book,Author,Genre
from  .forms import Bookforms,Authorforms
# Register your models here.




class AuthorAdmin(admin.ModelAdmin):
    form = Authorforms
    list_display = ('author_name','author_image','bio','date_of_birth','is_dead','date_of_death','category','genre')
    search_fields = ['author_name','category','genre']

class BookAdmin(admin.ModelAdmin):
    form = Bookforms
    list_display = ('book_name','book_image','page','created_at','price','book_bio','category','author','genre')
    search_fields = ['book_name','category','genre']

admin.site.register(Category)
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)