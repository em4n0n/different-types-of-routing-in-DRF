from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# URL pattern for a class method
# urlpatterns = [
#     path('orders', views.Orders.listOrders)
# ]

# URL pattern for routing a class-based view
# urlpatterns = [
#     path('books/<int:pk>', views.BookView.as_view())
# ]

# URL patterns for routing class that extend viewsets
urlpatterns = [
    path('books', views.BookView.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    )),
    path('books/<int:pk>',views.BookView.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }
    ))
]

# # Routing with SimpleRouter class in DRF
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')
# urlpatterns = router.urls