from django.shortcuts import render, get_object_or_404
from . models import Course, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from teachers.models import Teacher
from django.shortcuts import redirect

def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user

    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category= category_page)

    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(available=True, tags=tag_page)

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
        'tags':tags,
        
    }

    return render(request, 'courses.html', context)



def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id = course_id)
    courses = Course.objects.all().order_by('-date') 
    categories = categories = Category.objects.all()
    tags = Tag.objects.all()
  

    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()

    else:
        enrolled_courses = courses

    #enrolled_courses = current_user.courses_joined.all()
    context = {
        'course': course,
        'enrolled_courses': enrolled_courses,
        'categories': categories,
        'tags': tags,
        'user' : current_user,
    }
    return render(request, 'course.html', context)

def search(request):
    
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags= Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags
    }
    return render(request, 'courses.html', context)

def add_course(request):
    teachers = Teacher.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
   

    context = {
        'teachers' : teachers,
        'categories' : categories,
        'tags' : tags
    }


    return render(request, 'add_course.html', context)

def add(request):
   
    teacher = request.POST.get("teacher")
    category = request.POST.get("category")

    print(teacher, category)
    return redirect("/courses/add_course/")

def add_category(request):
    
    name = request.POST.get("name")
    slug = request.POST.get("slug")
    print(name, slug)
    
    if(name != None and slug != None):
        o_ref = Category(name=name, slug=slug.lower())
        o_ref.save()
    
    return redirect("/courses/add_course/")



def add_tag(request):
    name = request.POST.get("tag")
    tags = Tag.objects.all()
    if(name != None):
        o_ref = Tag(name=name, slug=name.upper())
        if o_ref in tags: 
            o_ref.save()


    return redirect('/courses/add_course/')


""" def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags= Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags
    }

    return render(request, 'courses.html', context) """

""" def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags= Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags
    }

    return render(request, 'courses.html', context) """

""" def course_list(request):
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags= Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags':tags
    }

    return render(request, 'courses.html', context) """