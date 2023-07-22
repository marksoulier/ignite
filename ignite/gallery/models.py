from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date_made = models.DateTimeField("date project made")
    category = models.CharField(max_length=200)

    #access images at http://example.com/media/images/image_filename.jpg
    #may need to have media file servered by a web server Apache
    #save up to 5 images to the database, maybe just add image1, image2, etc. to the model
    image = models.ImageField(upload_to="images/")

    submitted_date = models.DateTimeField("date submited",default=timezone.now)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name