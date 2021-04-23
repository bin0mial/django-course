from django.contrib import admin

from books.forms import CategoryForm, BookForm
from books.models import Book, Category, ISBN


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('id', 'title', "ISBN")
    list_display_links = ('id', 'title')
    list_filter = ("categories",)
    search_fields = ('title',)
    readonly_fields = ('ISBN',)


class CategoryBookInline(admin.StackedInline):
    model = Book.categories.through
    extra = 1
    max_num = 10


class BookInline(admin.StackedInline):
    model = Book


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    inlines = (CategoryBookInline,)


class ISBNAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_title', 'book_title')
    inlines = (BookInline,)


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ISBN, ISBNAdmin)
