from django.db import models
from django.contrib.auth.models import User
from sitelogic.models import Univarsty
from django.core.validators import RegexValidator
from django_countries.fields import CountryField



# Create your models here.

class Command(models.Model):
    
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False,null=False,verbose_name="Phone Number ") # Validators should be a list
    country = CountryField(default='DZ', blank=False,null=False,verbose_name="Choose your country ")
    nPassport = models.IntegerField(blank=False,null=False,verbose_name="The serial number of your passport ")
    dateOfBirth = models.DateField(blank=False,null=False,verbose_name="Date of birth ")
    passport = models.FileField(upload_to='Paasport_File', blank=False,null=False,verbose_name="Your Passport ")
    Certafica = models.FileField(upload_to='Certafica_File', blank=False,null=False,verbose_name="Latest education certificate ")
    contrat = models.FileField(upload_to='contrat_File', blank=False,null=False,verbose_name="The service contract after signing and filling it out ")
    talonImage = models.ImageField(upload_to='talon_images', blank=False,null=False,verbose_name="A Picture of the payment receipt ")
    Command_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercommand')
    post = models.ForeignKey(Univarsty, on_delete=models.CASCADE, related_name='univarsty')
    
        
    
    def __str__(self):
        return self.user.username + ' ' + self.user.first_name  + ' ' + 'Commande' + ' ' + self.post.name 