from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('courses/', include("apps.courses.urls")),
    path('dashboard/', include("apps.dashboard.urls")),
    path('profile/', include("apps.profiles.urls"))
]
