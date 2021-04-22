from django.contrib import admin

# Register your models here.
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = (['title'])

admin.site.register(Book, BookAdmin)
