from __future__ import annotations
from django.db import models
from datetime import date, datetime

class Book(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    summary = models.TextField(max_length=1000, null=False, blank=False)
    quantity = models.IntegerField(null=False, default=0)
    publication_date = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
