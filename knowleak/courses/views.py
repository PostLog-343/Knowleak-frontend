from cmath import pi
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from courses.forms import FileForm
from . models import Course, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User
from django.shortcuts import redirect
from .zoom import createMeeting
from django.contrib import messages

def course_list(request, category_name=None):
    category_page = None
    categories = Category.objects.all()
    current_user = request.user

    if category_name != None:
        category_page = get_object_or_404(Category, slug=category_name)
        courses = Course.objects.filter(available=True, category= category_page)

    else:
        courses = Course.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(courses, 4)

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



def course_detail(request,  course_id):
    current_user = request.user
    course = Course.objects.get(id = course_id)
    courses = Course.objects.all()
    categories = categories = Category.objects.all()
    token = course.token
    user_token = current_user.token
    student_count = course.students.count()

    teacher = course.teacher
    is_teacher = (current_user == teacher)
    
    if student_count != 0:
        coin_willbepaid = token/student_count
    else:
        coin_willbepaid = token
    can_enrolled = False

    if user_token>=coin_willbepaid:
        can_enrolled = True
    

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
        'can_enrolled' : can_enrolled,
        'coin_willbepaid' : coin_willbepaid,
        'is_teacher' : is_teacher
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
    teachers = User.objects.filter(is_teacher=True)
    categories = Category.objects.all()
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    context = {
        'teachers' : teachers,
        'categories' : categories,
        'form' : form
    }


    return render(request, 'add_course.html', context)



def add(request):
    print(request.FILES)
    if request.method == 'POST' :
        name = request.POST.get("name")
        teacher = request.user
        x = request.POST.get("category")
        if x:
            category = Category.objects.get(name=x)
        else:
            category = None

        description = request.POST.get("description")
        token = request.POST.get("token")
        fileform = FileForm(request.POST, request.FILES)
        if fileform.is_valid():
            image = fileform.cleaned_data["image"]
            
            if(name != None and teacher != None and category != None):
                o_ref = Course(name=name, teacher=teacher,category = category,  description = description, token=token, image=image)
                if o_ref:
                    """informations = createMeeting()
                    o_ref.zoom_link = informations[0]
                    o_ref.zoom_password = informations[1]"""
                    o_ref.save()
                
        else:
            messages.info(request, 'Name or Category information is missing')

   
    return redirect("/courses/add_course/")

def add_category(request):
    
    name = request.POST.get("name")
    slug = request.POST.get("slug")
    print(name, slug)
    
    if(name != None and slug != None):
        o_ref = Category(name=name, slug=slug.lower())
        o_ref.save()
    
    return redirect("/courses/add_course/")

