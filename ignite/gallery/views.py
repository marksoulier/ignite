from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectForm
# Create your views here.

def projects(request, project_category=None):
    if project_category:
        projects_list = Project.objects.filter(category=project_category)
    else:
        projects_list = Project.objects.all()
    context = {
        "projects_list": projects_list,
    }
    return render(request, "gallery/index.html", context)

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, "gallery/project_view.html", context)

def submit_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page after form submission
    else:
        form = ProjectForm()

    return render(request, "gallery/form.html", {"form": form})