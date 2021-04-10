from django.urls import path
from . import views
urlpatterns = [
   path('products/frontend',views.ProductFrontendAPIView.as_view()),
   path('products/backend',views.ProductBackendAPIView.as_view()),

]
