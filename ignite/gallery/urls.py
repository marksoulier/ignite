from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("project_form/", views.submit_project, name="submit_project"),
    path("completed_form/", views.completed_form, name="completed_form"),
    # ex: /project/1/
    path("project/<int:project_id>/", views.project_view, name="project_view"),
    path("<str:project_category>/", views.projects, name="projects"),
    path("", views.projects, name="index"),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)