from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self):
        #to change display name in django model 
        return self.title
