
from package_registration.views import BookRegistration, PaymentView, SummaryView
from django.urls import path

app_name = "packages"


urlpatterns = [
    path('registration/<int:pk>', BookRegistration,
         name="package-registration"),
    path('summary/<int:pk>', SummaryView.as_view(),
         name="registration-summary"),
    path('payment/<int:pk>', PaymentView.as_view(),
         name="registration-payment")




]
