from django.urls import path
from ..views.instructor import CourseUpdateView, CourseListView, CourseCreateView, CourseDeleteView, ModuleListView, \
    ModuleCreateView, ModuleUpdateView, ModuleDeleteView, ContentListView, ContentCreateUpdateView, ContentDeleteView, \
    ModuleOrderView, ContentOrderView

app_name = 'instructor'

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    # URLs modulos
    path('course/<int:course_id>/modules/', ModuleListView.as_view(), name='module_list'),
    path('course/<int:course_id>/modules/add/', ModuleCreateView.as_view(), name='module_add'),
    path('module/<int:pk>/edit/', ModuleUpdateView.as_view(), name='module_edit'),
    path('module/<int:pk>/delete/', ModuleDeleteView.as_view(), name='module_delete'),
    # URLs contenido
    path('module/<int:module_id>/contents/', ContentListView.as_view(), name='content_list'),
    path('module/<int:module_id>/content/<model_name>/add/', ContentCreateUpdateView.as_view(), name='content_add'),
    path('module/<int:module_id>/content/<int:id>/<model_name>/edit/', ContentCreateUpdateView.as_view(),
         name='content_edit'),
    path('content/<int:pk>/delete/', ContentDeleteView.as_view(), name='content_delete'),
    path('module/order/', ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', ContentOrderView.as_view(), name='content_order')
]
