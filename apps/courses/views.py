from django.shortcuts import render, get_object_or_404
from .models import Course
from django.db.models import Q
from django.core.paginator import Paginator


def course_list(request):
    courses = Course.objects.all()
    query = request.GET.get("query")

    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(owner__first_name__icontains=query)
        )

    paginator = Paginator(courses, 8)
    page_number = request.GET.get("page")
    courses_obj = paginator.get_page(page_number)

    # parametro usados para quitar page previo
    query_params = request.GET.copy()

    if "page" in query_params:
        query_params.pop("page")

    query_string = query_params.urlencode()

    return render(request, "courses/courses.html",
                  {"courses_obj": courses_obj, "query": query, "query_string": query_string})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.prefetch_related("contents")

    return render(request, "courses/course_detail.html", {"course": course, "modules": modules})


def course_lessons(request, slug):
    course = get_object_or_404(Course, slug=slug)
    course_title = course.title
    modules = course.modules.prefetch_related("contents")

    return render(request, "courses/course_lessons.html", {"course_title": course_title, "modules": modules})
