from django.shortcuts import render
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

    return render(request, "courses/courses.html", {"courses_obj": courses_obj, "query": query, "query_string": query_string})


def course_detail(request):
    course = {
        "course_title": "Apps de Django",
        "course_link": "course_lessons",
        "course_image": "images/curso_2.jpg",
        "info_course": {
            "lessons": 79,
            "duration": 8,
            "instructor": "Ricardo Moran"
        },
        "course_content": [
            {
                "id": 1,
                "name": "Introducción al curso",
                "lessons": [
                    {
                        "name": "¿Que aprenderás en el curso?",
                        "type": "video",
                    },
                    {
                        "name": "¿Como usar la plataforma?",
                        "type": "file"
                    }
                ]
            },
            {
                "id": 2,
                "name": "Modelos y el ORM",
                "lessons": [
                    {
                        "name": "Diseño de modelos de datos",
                        "type": "video",
                    },
                    {
                        "name": "Aplicando migraciones a la base de datos",
                        "type": "video"
                    },
                    {
                        "name": "Hoja de trucos de consultas con el ORM",
                        "type": "file"
                    }
                ]
            },
            {
                "id": 3,
                "name": "Vistas y Templates",
                "lessons": [
                    {
                        "name": "Lógica en las vistas (Views)",
                        "type": "video",
                    },
                    {
                        "name": "Pasando diccionarios de contexto",
                        "type": "video"
                    },
                    {
                        "name": "Ejercicios prácticos de maquetación",
                        "type": "file"
                    }
                ]
            }
        ]
    }

    return render(request, "courses/course_detail.html", {"course": course})


def course_lessons(request):
    return render(request, "courses/course_lessons.html")
