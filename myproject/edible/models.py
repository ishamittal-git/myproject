from django.db import models

class CutleryFactory(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name  # Returns factory name in Django Admin & queries
