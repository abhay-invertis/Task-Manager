
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# DRF Router for CRUD operations
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='planner')

urlpatterns = [
    path('', include(router.urls)),  # Task endpoints
]
