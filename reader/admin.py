from django.contrib import admin

from .models import Book, Author, Review


# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')


admin.site.register(Book, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Review, ReviewAdmin)
