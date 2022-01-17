from importlib.metadata import requires
from pyexpat import model
from statistics import mode
from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to="courses\%Y\%m\%d", default="courses/default_course_image.jpg")
    token = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
