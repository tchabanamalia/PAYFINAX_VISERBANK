from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 
    



class Reclamation(models.Model):
    titre = models.CharField(max_length=100, null=True)
    message = models.TextField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)




class Depots(models.Model):
    date_depot = models.DateTimeField(default=timezone.now)
    montant = models.FloatField(null=True)
    conversion = models.CharField(max_length=100, null=True)
    en_attente = models.BooleanField(default=False, null=True, blank=True)
    approuves = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=100, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    paiement = models.ForeignKey('Paiement', on_delete=models.CASCADE)




    
class Retrait(models.Model):
    date_retrait = models.DateTimeField(default=timezone.now)
    montant = models.FloatField(null=True)
    conversion = models.CharField(max_length=100, null=True)
    en_attente = models.BooleanField(default=False, null=True, blank=True)
    approuves = models.BooleanField(default=False, null=True, blank=True)
    status = models.CharField(max_length=100, null=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    paiement = models.ForeignKey('Paiement', on_delete=models.CASCADE)





class Pays(models.Model):
    nom = models.CharField(max_length=100, null=True)
    localisation = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    



class Paiement(models.Model):
    type_paiement = models.CharField(max_length=100, null=True)
    monaie = models.CharField(max_length=100, null=True)
    type_paiement = models.CharField(max_length=100, null=True)
    taux = models.IntegerField(default=0, null=True, blank=True)
    charge = models.CharField(max_length=100, null=True) ##
    limite_retrait = models.CharField(max_length=100, null=True) ##
    status = models.CharField(max_length=100, null=True)
    pays = models.ManyToManyField("Pays", verbose_name="Pays", blank=True)




class Notification(models.Model):
    message = models.TextField()
    paiement = models.ForeignKey('Paiement', on_delete=models.CASCADE)
