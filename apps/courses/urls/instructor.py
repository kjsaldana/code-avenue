from django.urls import path
from ..views.instructor import CourseUpdateView, CourseListView, CourseCreateView, CourseDeleteView, ModuleListView

app_name = 'instructor'

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    # URLs modulos
    path('course/<int:course_id>/modules/', ModuleListView.as_view(), name='module_list'),
]
