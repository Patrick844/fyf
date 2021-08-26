
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from landing.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("landing.urls", namespace="landing")),
    path('courses/', include("courses.urls", namespace="courses")),
    path('user/', include("userapp.urls", namespace="userapp")),
    path('operator/', include("adminop.urls", namespace="operator")),
    path('packages/', include("package_registration.urls", namespace="packages")),
    path('account/signup/', SignUpView.as_view(), name="signup"),
    path('accounts/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
