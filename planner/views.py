
from django.shortcuts import render, redirect
from .models import Module, Assignment, StudySession
from .forms import ModuleForm, AssignmentForm, StudySessionForm


def dashboard(request):
    modules = Module.objects.all()
    assignments = Assignment.objects.select_related("module").order_by("due_date")
    study_sessions = StudySession.objects.select_related("module").order_by("study_date")

    context = {
        "modules": modules,
        "assignments": assignments,
        "study_sessions": study_sessions,
        "total_modules": modules.count(),
        "pending_assignments": assignments.filter(status="pending").count(),
        "total_study_sessions": study_sessions.count(),
    }

    return render(request, "planner/dashboard.html", context)


def add_module(request):
    form = ModuleForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("planner:dashboard")

    return render(request, "planner/form.html", {
        "form": form,
        "title": "Add Module",
    })


def add_assignment(request):
    form = AssignmentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("planner:dashboard")

    return render(request, "planner/form.html", {
        "form": form,
        "title": "Add Assignment",
    })


def add_study_session(request):
    form = StudySessionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("planner:dashboard")

    return render(request, "planner/form.html", {
        "form": form,
        "title": "Schedule Study Session",
    })

