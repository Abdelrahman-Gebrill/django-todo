from django.db import models

# Create your models here.
class TODO(models.Model):
    details = models.CharField(max_length=1000)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.details