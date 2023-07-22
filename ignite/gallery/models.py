from django.db import models
from django.utils import timezone
import json

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    team = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True, default="No contact info")

    related_links = models.CharField(max_length=200, blank=True, default="No related links")
    description = models.CharField(max_length=400)
    date_made = models.DateTimeField("date project made")
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200, blank=True, default="No sub category")
    entity = models.CharField(max_length=200, blank=True, default="No entity")



    #access images at http://example.com/media/images/image_filename.jpg
    #may need to have media file servered by a web server Apache
    #save up to 5 images to the database, maybe just add image1, image2, etc. to the model
    
    # The first image is required
    image = models.ImageField(upload_to="images/")
    
    # Up to 4 additional images are optional
    image2 = models.ImageField(upload_to="images/", blank=True, null=True)
    image3 = models.ImageField(upload_to="images/", blank=True, null=True)
    image4 = models.ImageField(upload_to="images/", blank=True, null=True)
    image5 = models.ImageField(upload_to="images/", blank=True, null=True)

    submitted_date = models.DateTimeField("date submited",default=timezone.now)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    def set_team(self, team_list):
        # Convert the list to a JSON string and save it in the database
        self.team = json.dumps(team_list)

    def get_team(self):
        # Retrieve the JSON string from the database and convert it back to a list
        if self.team:
            return json.loads(self.team)
        return []