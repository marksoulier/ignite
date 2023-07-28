from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .form import ProjectForm
# Create your views here.

def projects(request, project_category=None):
    # Retrieve all approved projects sorted by submitted_date in descending order
    approved_projects = Project.objects.filter(approved=True).order_by('-submitted_date')

    # If project_category is provided, filter the approved projects based on the category
    if project_category:
        projects_list = approved_projects.filter(category=project_category)
        context = {
            "projects_list": projects_list,
            "category": project_category,
        }
        return render(request, "gallery/category_description.html", context)
    else:
        projects_list = approved_projects
        context = {
            "projects_list": projects_list,
        }
        return render(request, "gallery/home_description.html", context)

def project_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, "gallery/project_view.html", context)

def submit_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data without committing to the database yet
            project = form.save(commit=False)

            # Check if the optional fields are empty and set them to default values if so
            project.sub_category = form.cleaned_data.get("sub_category", "No sub category")
            project.related_links = form.cleaned_data.get("related_links", "No related links")
            project.contact_info = form.cleaned_data.get("contact_info", "No contact info")
            team_list = form.cleaned_data.get("team")
            if team_list:
                project.set_team(team_list)
            else:
                project.set_team([])

            # Save the project with all the data
            project.save()

            return redirect('completed_form')  # Redirect to a success page after form submission
        else:
            print(form.errors)
            print(form.cleaned_data)
    else:
        form = ProjectForm()

    return render(request, "gallery/form.html", {"form": form})

def completed_form(request):
    return render(request, "gallery/completed_form.html", {})