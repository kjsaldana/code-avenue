from django.shortcuts import render

def course_list(request):
    return render(request, "courses/courses.html")

def course_detail(request):
    return render(request, "courses/course.html")

def course_lessons(request):
    return render(request, "courses/course.html")