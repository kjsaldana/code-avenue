from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from apps.dashboard.views import redirect_home

urlpatterns = [

    path('', redirect_home, name="home"),
    path("admin/", admin.site.urls),
    path('courses/', include("apps.courses.urls")),
    path('dashboard/', include("apps.dashboard.urls")),
    path('profile/', include("apps.profiles.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('instructor/', include("apps.courses.urls.instructor")),
    path('student/', include("apps.courses.urls.student"))
]
