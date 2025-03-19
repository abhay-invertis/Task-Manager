from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils.dateparse import parse_date  # For parsing date strings

from .models import Planner
from .serializers import PlannerSerializer
from .permissions import IsAdminOrTaskOwner  # Custom permission

# Pagination Setup
class TaskPagination(PageNumberPagination):
    page_size = 5             # Display 10 tasks per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Planner.objects.all().order_by('-created_at')
    serializer_class = PlannerSerializer
    pagination_class = TaskPagination  # Pagination Added
    permission_classes = [IsAdminOrTaskOwner]  # Custom permission added

    # Permissions Setup
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]  # Public access for GET requests
        return [IsAuthenticated()]  # Authenticated users for POST, PUT, DELETE

    # Custom Queryset Logic for Authorization + Filtering
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by 'completed' status
        completed = self.request.query_params.get('completed')
        if completed is not None:
            queryset = queryset.filter(completed=completed.lower() == 'true')

        # Filter by 'created_after' date
        created_after = self.request.query_params.get('created_after')
        if created_after:
            try:
                queryset = queryset.filter(created_at__gte=parse_date(created_after))
            except ValueError:
                pass  # Ignore invalid date format

        # Filter by 'updated_after' date
        updated_after = self.request.query_params.get('updated_after')
        if updated_after:
            try:
                queryset = queryset.filter(updated_at__gte=parse_date(updated_after))
            except ValueError:
                pass  # Ignore invalid date format

        # Admins can see all tasks
        if self.request.user.is_staff:
            return queryset

        # Anonymous users should not see any tasks
        if self.request.user.is_anonymous:
            return queryset.none()

        # Regular users only see their own tasks
        return queryset.filter(created_by=self.request.user)

    # Creating Tasks - Only for Authenticated Users
    def perform_create(self, serializer):
        print(f'Authenticated User in perform_create: {self.request.user}')  # Debug print
        print(f'Serializer Data Before Save: {serializer.validated_data}')   # Debug data

        if self.request.user.is_anonymous:
            raise NotAuthenticated("Authentication credentials were not provided.")
        serializer.save(created_by=self.request.user)

    # Updating Tasks - Only Creator Can Modify
    def perform_update(self, serializer):
        task = self.get_object()
        if task.created_by != self.request.user:
            raise PermissionDenied("You are not allowed to update this task.")
        serializer.save()

    # Deleting Tasks - Only Creator Can Delete
    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("You are not allowed to delete this task.")
        instance.delete()
        return Response(
            {"detail": f"Task '{instance.title}' deleted successfully."},
            status=status.HTTP_200_OK
        )
