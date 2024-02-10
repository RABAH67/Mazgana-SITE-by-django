from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.



class Profaile(models.Model):
    
    image = models.ImageField(default='images/user.png')
    country = CountryField(blank=True, null=True)
    Npassport = models.CharField(max_length=9,verbose_name="passport number")
    dateOfBirth = models.DateField(blank=True, null=True)
    passportPDF = models.FileField()
    certaficatePDF = models.FileField()
    contrat = models.FileField()
    virefayd = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return '{} profile'.format(self.user.username)

    

