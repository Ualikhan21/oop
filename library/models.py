# library/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    quantity = models.IntegerField(default=1)
    access = models.BooleanField(default=True, verbose_name="Available for under 18")
    
    def available(self):
        return self.quantity - self.student_set.count()
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    def is_available_for(self, age):
        """Check if book is available for user of given age"""
        if self.access:
            return True
        return age >= 18 if age else False 

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    age = models.IntegerField()
    borrowed_books = models.ManyToManyField(Book, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.group})"