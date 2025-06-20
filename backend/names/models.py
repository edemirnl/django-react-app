from django.db import models

# Create your models here.
class Name(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name