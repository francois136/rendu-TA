from django.core.management.base import BaseCommand
from blog.models import Equipement

class Command(BaseCommand):
    help = 'Initialise le nombre actuel d\'utilisateurs pour chaque équipement'

    def handle(self, *args, **kwargs):
        equipements = Equipement.objects.all()
        for equipement in equipements:
            equipement.update_nombre_actuel()
        self.stdout.write(self.style.SUCCESS('Successfully initialized nombre_actuel for all equipments'))
