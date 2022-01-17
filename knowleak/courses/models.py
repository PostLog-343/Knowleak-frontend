from django.db import models
from teachers.models import Teacher
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date = models.DateField(auto_now=False)
    token = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
