from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>', views.course_detail, name="course_detail"),
    path('categories/<slug:category_slug>', views.course_list, name="courses_by_category"),
    path('tags/<slug:tag_slug>', views.course_list, name="courses_by_tag"),
    path('search/', views.search, name="search"),
    path('add_course/', views.add_course, name="add_course"),
    path('add_category/', views.add_category, name="add_category"),
    path('add_tag/', views.add_tag, name="add_tag"),
    path('add/',views.add,name="add_courses_post")
]