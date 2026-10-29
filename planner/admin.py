from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Module, Assignment, StudySession


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "due_date", "priority", "status")
    list_filter = ("priority", "status", "module")
    search_fields = ("title", "module__code", "module__name")
    ordering = ("due_date",)


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "study_date", "duration_minutes", "completed")
    list_filter = ("completed", "module")
    search_fields = ("title", "module__code", "module__name")
    ordering = ("study_date",)
