from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.course_list, name="courses"),
    path('<int:course_id>/', views.course_detail, name="course_detail"),
    path('categories/<slug:category_name>', views.course_list, name="courses_by_category"),
    path('search/', views.search, name="search"),
    path('add_course/', views.add_course, name="add_course"),
    path('add_category/', views.add_category, name="add_category"),
    path('add/',views.add,name="add_courses_post")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)