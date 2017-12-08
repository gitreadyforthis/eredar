from django import forms

from reader.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('document',)
        exclude = [
            'description', 'owner', 'title', 'author'
        ]
