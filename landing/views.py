from landing.forms import SignUpForm
from django.shortcuts import render, HttpResponse, reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CourseView(TemplateView):
    template_name = "landing/courses.html"


class SignUpView(TemplateView):
    template_name = "account/signup-alternative.html/"

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)

        form = SignUpForm
        context.update({
            "form": form
        })
        return context


# Create your views here.
def landing_home(request):
    # return render(request,"landing/home_page.html")
    return render(request, "landing/home_page.html")


def coming_soon(request):
    return render(request, "landing/coming_soon.html")


def packages_page(request):
    return render(request, "landing/packages.html")
