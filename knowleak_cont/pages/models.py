from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField

class Course(models.Model):
    "img = models.ImageField(upload_to='static/assets/img/posts')"
    title = models.CharField(max_length=50)
    briefInstr = models.TextField()
    courseOwner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    creationDate = DateTimeField(auto_now_add=True)
    classTime = DateTimeField()

    def __str__(self):
        return self.title