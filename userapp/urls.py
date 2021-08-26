

from userapp.views import OrderDetailsView, OrderView
from django.urls import path

app_name = "userapp"


urlpatterns = [
    path('orders/', OrderView.as_view(),
         name="orders"),
    path('orders/<int:pk>', OrderDetailsView.as_view(),
         name="order-detail"),
]
