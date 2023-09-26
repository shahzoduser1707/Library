from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=300,default='')

    class Meta:
        db_table = 'Category'
    def __str__(self) -> str:
        return self.category_name
    
class Genre(models.Model):
    genre_name = models.CharField(max_length=200,default='')


    class Meta:
        db_table = 'Genre'
    def __str__(self) -> str:
        return self.genre_name



class Author(models.Model):
    author_name = models.CharField(max_length=200,default='')
    author_image = models.ImageField(upload_to='author/')
    bio = models.TextField(default='')
    date_of_birth = models.DateTimeField(default=datetime.now)
    is_dead = models.BooleanField(default=False)
    date_of_death = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Author'
    def __str__(self) -> str:
        return self.author_name
    

class Book(models.Model):
    book_name = models.CharField(max_length=300,default='')
    book_image = models.ImageField(upload_to='book/')
    page = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(default=1)
    book_bio = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

