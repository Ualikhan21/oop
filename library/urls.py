from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This will be /library/
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/assign/', views.assign_book, name='assign_book'),
    path('students/<int:student_id>/return/<int:book_id>/', views.return_book, name='return_book'),
]