from django.db import models
from category.models import Category


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # RESTORED
    description = models.TextField()
    mission = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # NEW

    def requirement_list(self):
        return self.requirements.splitlines()

    def __str__(self):
        return self.title
