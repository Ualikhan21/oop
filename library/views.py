# library/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student
from .forms import BookForm, StudentForm, AssignBookForm

def home(request):
    return render(request, 'library/tamplates/library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'library/student_list.html', {'students': students})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'library/add_student.html', {'form': form})

def assign_book(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = AssignBookForm(request.POST, instance=student)
        if form.is_valid():
            book = form.cleaned_data['book']
            
            # Additional validation
            if not book.access and (not student.age or student.age < 18):
                form.add_error('book', "This book is restricted to students 18+")
            elif book.available() <= 0:
                form.add_error('book', "No copies of this book available")
            else:
                student.borrowed_books.add(book)
                return redirect('student_detail', student_id=student.id)
    else:
        form = AssignBookForm(instance=student)
    
    return render(request, 'library/assign_book.html', {
        'form': form,
        'student': student
    })
def return_book(request, student_id, book_id):
    student = get_object_or_404(Student, pk=student_id)
    book = get_object_or_404(Book, pk=book_id)
    student.borrowed_books.remove(book)
    return redirect('student_detail', student_id=student.id)

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'library/student_detail.html', {'student': student})

def home(request):
    total_books = Book.objects.count()
    total_students = Student.objects.count()
    books_borrowed = sum([student.borrowed_books.count() for student in Student.objects.all()])
    
    return render(request, 'library/home.html', {
        'total_books': total_books,
        'total_students': total_students,
        'books_borrowed': books_borrowed
    })