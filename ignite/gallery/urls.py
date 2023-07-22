from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # ex: /
    path("", views.projects, name="index"),
    path("<str:project_category>/", views.projects, name="projects"),
    # ex: /project/1/
    path("project/<int:project_id>/", views.project_view, name="project_view"),
    path("project/submit/", views.submit_project, name="submit_project"),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)