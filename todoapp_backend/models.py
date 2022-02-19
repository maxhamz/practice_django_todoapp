from django.utils import timezone
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False, null=True, blank=True)
    last_modified_at = models.DateTimeField(default=timezone.now())
    
    class Meta:
        ordering = ('-created_at',)
          
    def __str__(self):
        return self.title
