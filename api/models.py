from __future__ import annotations
from django.db import models
from datetime import date, datetime


class Book(models.Model):
    name: str = models.CharField(max_length=200, unique=True, null=False, blank=False)
    author: str = models.CharField(max_length=200, unique=True, null=False, blank=False)
    summary: str = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
    )
    quantity: int = models.IntegerField(null=False, blank=True)
    publication_date: date = models.DateField(null=True, blank=True)
    language: str = models.CharField(max_length=50, null=False, blank=True)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
