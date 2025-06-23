from django.db import models

# Create your models here.
# donations/models.py
from django.db import models
from category.models import Category  # Shared model

class Donation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='donation_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def progress_percent(self):
        return (self.raised_amount / self.goal_amount) * 100 if self.goal_amount else 0

    def __str__(self):
        return self.title
