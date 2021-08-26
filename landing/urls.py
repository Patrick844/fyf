
from .views import landing_home, coming_soon, packages_page, CourseView
from django.urls import path

app_name = "landing"

urlpatterns = [
    path('', landing_home, name="home"),
    path('packages', packages_page, name="packages"),
    path('courses', CourseView.as_view(), name="courses"),
    path('coming_soon/', coming_soon, name="coming-soon"),




]
