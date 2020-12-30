from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=120)
    email= models.EmailField()
    phone= models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
    


