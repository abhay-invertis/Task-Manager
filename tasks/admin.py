from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Planner

@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title',)
