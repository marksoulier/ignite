from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'owner', 'description', 'date_made', 'category', 'image', 'sub_category', 'related_links', 'contact_info', 'team', 'image2', 'image3', 'image4', 'image5','entity']

    def clean(self):
        cleaned_data = super().clean()
        # Check if any required fields are missing
        if not cleaned_data['name'] or not cleaned_data['owner'] or not cleaned_data['description'] or not cleaned_data['date_made'] or not cleaned_data['category']:
            raise forms.ValidationError("All required fields must be filled.")
        
        # Check if image field is empty
        image = cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Please attach an image.")
        return cleaned_data