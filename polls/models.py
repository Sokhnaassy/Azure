from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Syndrome(models.Model):
    code_envoyé = models.CharField(max_length=20,validators=[RegexValidator(r'^[01]*$', 'Entrez des 0 et des 1 uniquement.')])
    code_reçu = models.CharField(max_length=20,validators=[RegexValidator(r'^[01]*$', 'Entrez des 0 et des 1 uniquement.')])
    valeur_syndrome = models.IntegerField(editable=False)
    état = models.TextField(max_length=20,editable=False)
 
    def save(self, *args, **kwargs):
        self.valeur_syndrome =bin(int(self.code_envoyé, 2) ^ int(self.code_reçu, 2))[2:]
        if (self.valeur_syndrome == '0'):
            self.état="Erreurs non détectées"
        elif(self.valeur_syndrome == '1'):
            self.état="Erreurs détectées"
        else:
            self.état="Indéfini"
       

        super(Syndrome, self).save(*args, **kwargs)

    #Génération du polynome de Goppa
  
        
class Modulo(models.Model):
    modulo = models.IntegerField()
    def save(self, *args, **kwargs):

        super(Modulo, self).save(*args, **kwargs)

    #Génération du polynome de Goppa
  
