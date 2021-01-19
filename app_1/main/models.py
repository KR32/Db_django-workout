from django.db import models

# Create your models here.


class testout(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null = True)
    phone_number = models.CharField(max_length=12, null=True)
    notes = models.TextField(null=True)
        
    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=128, null=True)
    comments = models.CharField(max_length=128, null = True)

    def __repr__(self) -> str:
        return self.language

class country_information(models.Model):
    country_id =  models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=128, null=True)
    nationality = models.CharField(max_length=128, null=True)
    dailing_code = models.CharField(max_length=128, null=True)
    country_name = models.CharField(max_length=128, null=True)
    language_id = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.country_name