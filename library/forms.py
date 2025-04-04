# library/forms.py
from django import forms
from .models import Book, Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'year', 'quantity', 'access']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'group', 'age']

class AssignBookForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.none(),
        label="Select a book to assign"
    )
    
    class Meta:
        model = Student
        fields = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Get all available books
        available_books = Book.objects.filter(quantity__gt=0).exclude(
            id__in=self.instance.borrowed_books.values_list('id', flat=True))
        
        # Filter based on student age and book access
        student_age = self.instance.age
        if student_age and student_age < 18:
            available_books = available_books.filter(access=True)
        
        self.fields['book'].queryset = available_books   
    class Meta:
        model = Student
        fields = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(quantity__gt=0).exclude(
            id__in=self.instance.borrowed_books.values_list('id', flat=True))