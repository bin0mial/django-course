from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from books.models import Book


class CategoryForm(ModelForm):
    def clean(self):
        super().clean()

        name = self.cleaned_data.get("name")
        if len(name) < 2:
            raise ValidationError("Category Must be at least 2 characters.")


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('ISBN', )

    def clean_title(self):
        title: str = self.cleaned_data.get("title")

        if not 10 <= len(title) <= 50:
            raise ValidationError("Title must be between 10 and 50 characters.")

        return title
