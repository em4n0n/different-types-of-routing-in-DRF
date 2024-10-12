from django.urls import path
from . import views

# URL pattern for a class method
# urlpatterns = [
#     path('orders', views.Orders.listOrders)
# ]

# URL pattern for routing a class-based view
urlpatterns = [
    path('books/<int:pk>', views.BookView.as_view())
]
