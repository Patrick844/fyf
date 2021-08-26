

from adminop.views import OperatorDetailsView, OperatorView
from userapp.views import OrderDetailsView, OrderView
from django.urls import path

app_name = "operator"


urlpatterns = [
    path('', OperatorView.as_view(),
         name="reservations"),
    path('reservation//<int:pk>', OperatorDetailsView.as_view(),
         name="reservation-detail"),
]
