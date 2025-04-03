from django.db import models

class CutleryFactory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    phone_number = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name  # Returns factory name in Django Admin & queries

    class Meta:
        verbose_name = "Cutlery Factory"
        verbose_name_plural = "Cutlery Factories"