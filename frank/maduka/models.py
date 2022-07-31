from django.db import models

# Create your models here.
class Frank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Maduka(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    frank = models.ForeignKey(Frank,related_name="maduka", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
