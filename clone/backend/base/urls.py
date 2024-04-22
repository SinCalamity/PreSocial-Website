from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('creator/', views.getCreators, name="creators"),
    path('creator/<str:pk>', views.getCreator, name="creator"),
    
]