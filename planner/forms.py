
from django import forms
from .models import Module, Assignment, StudySession


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ["code", "name", "description"]


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [
            "title",
            "description",
            "module",
            "due_date",
            "priority",
            "status",
        ]
        widgets = {
            "due_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = [
            "module",
            "title",
            "study_date",
            "duration_minutes",
            "notes",
            "completed",
        ]
        widgets = {
            "study_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }