from django.shortcuts import render, get_object_or_404
from . models import Course, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from teachers.models import Teacher
from django.shortcuts import redirect

def course_list(request, category_slug=None):
    category_page = None
    categories = Category.objects.all()
    current_user = request.user

    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category= category_page)

    else:
        courses = Course.objects.all().order_by('-date')

    page = request.GET.get('page', 1)
    paginator = Paginator(courses, 2)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
    else:
        enrolled_courses = courses

    
    context = {
        'courses': courses,
        'enrolled_courses': enrolled_courses,
        'user' : current_user,
        'categories': categories,
        
    }

    return render(request, 'courses.html', context)



def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date') 
    categories = categories = Category.objects.all()
  

    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()

    else:
        enrolled_courses = courses

    #enrolled_courses = current_user.courses_joined.all()
    context = {
        'course': course,
        'enrolled_courses': enrolled_courses,
        'categories': categories,
        'user' : current_user,
    }
    return render(request, 'course.html', context)

def search(request):
    
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
    }
    return render(request, 'courses.html', context)

def add_course(request):
    teachers = Teacher.objects.all()
    categories = Category.objects.all()

    context = {
        'teachers' : teachers,
        'categories' : categories,
    }


    return render(request, 'add_course.html', context)

def add(request):
   
    name = request.POST.get("name")
    teacher = request.POST.get("teacher")
    category = request.POST.get("category")
    description = request.POST.get("description")
    date = request.POST.get("date")

    print(name, teacher, category, description, date)

    if(name != None and date != ""):
        o_ref = Course(name=name,   description = description, date = date)
        o_ref.save()

    return redirect("/courses/add_course/")

def add_category(request):
    
    name = request.POST.get("name")
    slug = request.POST.get("slug")
    print(name, slug)
    
    if(name != None and slug != None):
        o_ref = Category(name=name, slug=slug.lower())
        o_ref.save()
    
    return redirect("/courses/add_course/")
