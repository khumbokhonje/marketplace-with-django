from django.db import models

# Create your models here.
class Health(models.Model):
    title = models.CharField(max_length=156)
    text = models.CharField(max_length=10000)

    def __str__(self):
        return f"Title:{self.title}"