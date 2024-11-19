from django.db import models

class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    capacite_max = models.IntegerField(default=1)
    nombre_actuel = models.IntegerField(default=0)

    def __str__(self):
        return self.id_equip

    def is_free(self):
        return self.nombre_actuel < self.capacite_max

    def update_nombre_actuel(self):
        self.nombre_actuel = Character.objects.filter(lieu=self).count()
        self.save()

 
class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character