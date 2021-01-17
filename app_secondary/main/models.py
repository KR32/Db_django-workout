from django.db import models

# Create your models here.


class testout(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=12)
    
    def __repr__(self) -> str:
        return self.name