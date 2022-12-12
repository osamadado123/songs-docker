from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Song(models.Model):
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name