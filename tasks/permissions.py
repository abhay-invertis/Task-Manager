from rest_framework import permissions

class IsAdminOrTaskOwner(permissions.BasePermission):
    """
    Custom permission to allow:
    - Admins to view all tasks.
    - Regular users can only modify their own tasks.
    """

    def has_object_permission(self, request, view, obj):
        # Admin users have full access
        if request.user.is_staff:
            return True

        # Regular users can modify only their own tasks
        return obj.created_by == request.user
