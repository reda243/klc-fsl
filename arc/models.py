#from __future__ import unicode_literals

from django.db import models



class logements(models.Model):
    Type= models.CharField(max_length=255)
    Television= models.BooleanField()
    Douche= models.BooleanField()
    Hammam= models.BooleanField()
    Baignoire= models.BooleanField()
    Seche_cheveux= models.BooleanField()
    Balcon= models.BooleanField()
    Terrasse= models.BooleanField()
    Parking= models.BooleanField()
    Climatisation= models.BooleanField()
    Wifi= models.BooleanField()
    Jacuzzi= models.BooleanField()
    Ascenseur= models.BooleanField()
    Photo1= models.ImageField()
    Photo2= models.ImageField()
    Photo3= models.ImageField()
    Presentation= models.TextField()


class voitures(models.Model):
    Type= models.CharField(max_length=255)
    Climatisation= models.BooleanField()
    Photo1= models.ImageField()
    Photo2= models.ImageField()
    Photo3= models.ImageField()
    Presentation= models.TextField()

class services(models.Model):
    Type= models.CharField(max_length=255)
    Photo1= models.ImageField()
    Photo2= models.ImageField()
    Photo3= models.ImageField()
    Presentation= models.TextField()


class res(models.Model):
    Nom = models.CharField(max_length=30)
    prénom = models.CharField(max_length=30)
    Adresse = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    Date_Arrivée = models.DateField(max_length=30)
    Date_Départ = models.DateField(max_length=30) 



   

