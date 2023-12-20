from django.db import models

# Create your models here.
class Pets(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    manufacture=models.CharField(max_length=20)
    
    
    def __str(self):
        return '{}'.format(self.name)