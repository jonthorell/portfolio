from django.db.models import CharField, Model
from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class project(models.Model):
    '''Class used to create the projects model '''

    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    github_url= models.CharField(max_length=60, blank=False, null=False, unique=False, default="localhost")
    github_url_title= models.CharField(max_length=60, blank=False, null=False, unique=False, default="Github: Title of repo")
    github_description = models.CharField(max_length=255, blank=True,null=True, default="Add description")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def get_status(self):
        return self.status
