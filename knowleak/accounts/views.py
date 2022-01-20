from django.shortcuts import render, redirect
from . forms import EditProfileForm, LoginForm, RegisterForm
from django.contrib.auth import  login, logout
from .backends import MyAuthBackend
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import User



def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = MyAuthBackend.authenticate(username,password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form':form})


def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registered')
            return redirect('login')
        else:
            messages.info(request, 'Wrong Informations')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def update_profile(request):
    current_user = request.user

    form = EditProfileForm()


    return render(request, 'update_profile.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')


def user_dashboard(request):
    current_user = request.user
    courses = current_user.courses_joined.all()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Information')
            return redirect('dashboard')

    else:
        form = EditProfileForm(instance=current_user)
        
    context = {
        'courses': courses,
        'form' : form
    }

    return render(request, 'dashboard.html', context)

    


def enroll_the_course(request):
    course_id = request.POST['course_id']
    user_id = request.POST['user_id']
    course = Course.objects.get(id = course_id)
    user = User.objects.get(id = user_id)
    course.students.add(user)
    return redirect('dashboard')

def release_the_course(request):
    course = Course.objects.get(id = request.POST['course_id'])
    user = User.objects.get(id = request.POST['user_id'])
    course.students.remove(user)
    return redirect('dashboard')