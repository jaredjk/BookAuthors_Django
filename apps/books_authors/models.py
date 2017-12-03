from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model): #created model 'Book'
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: name = {} desc = {}>".format(self.name, self.desc)

class Author(models.Model): #created model 'Authors' 
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    notes = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ManyToManyField(Book, related_name = "authors") #many to many. 
    def __repr__(self):
        return "<User object: first_name = {} last_name = {} email = {} book = {} >".format(self.first_name, self.last_name, self.email, self.book)