# library/admin.py
from django.contrib import admin
from .models import Book, Student

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'year', 'quantity', 'available', 'access')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'group', 'age')
    search_fields = ('name', 'surname', 'group', 'age')
    filter_horizontal = ('borrowed_books',)