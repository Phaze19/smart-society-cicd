from django.db import models

class Resident(models.Model):
    name = models.CharField(max_length=100)
    flat_number = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.flat_number})"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
