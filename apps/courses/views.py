from django.shortcuts import render


def course_list(request):
    courses = [
        {
            "id": 1,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Three-month Course to Learn the Basics of Python and Start Coding.",
            "instructor": "Alison Walsh",
            "course_image": "images/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
        },
        {
            "id": 2,
            "level": "Beginner",
            "rating": 4.0,
            "course_title": "Beginner's Guide to Successful Company Management: Business And More",
            "instructor": "Patty Kutch",
            "course_image": "images/curso_2.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/20.jpg",
        },
        {
            "id": 3,
            "level": "Beginner",
            "rating": 3.6,
            "course_title": "A Fascinating Theory of Probability. Practice. Application. How to Outplay...",
            "instructor": "Alonzo Murray",
            "course_image": "images/curso_3.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/32.jpg",
        },
        {
            "id": 4,
            "level": "Beginner",
            "rating": 4.9,
            "course_title": "Introduction: Machine Learning and LLM. Implementation in Modern Software",
            "instructor": "Gregory Harris",
            "course_image": "images/curso_4.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/45.jpg",
        },
    ]
    return render(request, "courses/courses.html", {"courses": courses})


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
