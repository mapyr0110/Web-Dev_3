from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

# urlpatterns = [
#     path('products/', views.product_list),
#     path('products/<int:id>/', views.product_detail),
#     path('categories/', views.category_list),
#     path('categories/<int:id>/', views.category_detail),
#     path('categories/<int:id>/products/', views.category_products),
# ]

router = DefaultRouter()

router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = router.urls