from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student

# Create your views here.

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'students/login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('user_login')

# Student list view
@login_required(login_url='user_login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Add student view
@login_required(login_url='user_login')
def add_student(request):
    if request.method == 'POST':
        student = Student(
            student_id=request.POST['student_id'],
            name=request.POST['name'],
            college=request.POST['college'],
            major=request.POST['major'],
            class_name=request.POST['class_name']
        )
        student.save()
        messages.success(request, 'Student added successfully')
        return redirect('student_list')
    return render(request, 'students/add_student.html')

# Edit student view
@login_required(login_url='user_login')
def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.college = request.POST['college']
        student.major = request.POST['major']
        student.class_name = request.POST['class_name']
        student.save()
        messages.success(request, 'Student updated successfully')
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'student': student})

# Delete student view
@login_required(login_url='user_login')
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully')
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})
