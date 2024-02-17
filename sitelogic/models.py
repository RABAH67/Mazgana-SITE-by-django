from django.db import models

# Create your models here.


class Univarsty(models.Model):
    
    photo = models.ImageField(upload_to='univarsty/')
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.CharField(default='000')
    univarstyURL = models.URLField()   
    
    
    def __str__(self):
        
        return self.name 
    

