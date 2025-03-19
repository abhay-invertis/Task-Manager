from rest_framework import serializers
from .models import Planner

class PlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']  # ✅ Fix applied
