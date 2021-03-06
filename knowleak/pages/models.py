from django.db import models

# Class of contact back-end:
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, default="Anonymous User")
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.username
