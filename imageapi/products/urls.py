from django.contrib import admin
from django.urls import path, include
from products.views import ProductViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter




# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
#router.register("categories",CategoryViewSet)
#urlpatterns= router.urls


urlpatterns = [
    
    # path('', include(router.urls)),
    path('products/', ProductViewSet.as_view(), name='product-list'),

]
