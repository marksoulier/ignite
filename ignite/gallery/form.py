from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'owner', 'description', 'date_made', 'category', 'image']

    def clean(self):
        cleaned_data = super().clean()
        # Check if any fields are missing
        if any(not cleaned_data[field] for field in self.fields):
            raise forms.ValidationError("All fields are required.")
        return cleaned_data