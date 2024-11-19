from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement
 
# Create your views here.
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'playground/character_list.html', {'characters': characters})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    form=MoveForm()
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
        ancien_lieu.disponibilite = "libre"
        ancien_lieu.save()
        form.save()
        nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
        nouveau_lieu.disponibilite = "occupé"
        nouveau_lieu.save()
        return redirect('character_detail', id_character=id_character)
    else:
        form = MoveForm()
        return render(request,
                  'playground/character_detail.html',
                  {'character': character, 'form': form})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    form = MoveForm(request.POST or None, instance=character)  # Associer le formulaire avec l'instance du personnage
    if form.is_valid():
        # Récupérer l'ancien lieu du personnage
        ancien_lieu = character.lieu
        ancien_lieu.disponibilite = "libre"
        ancien_lieu.save()
        
        # Sauver le formulaire et mettre à jour le nouveau lieu
        form.save()
        
        # Mettre à jour la disponibilité du nouveau lieu
        nouveau_lieu = character.lieu  # Après l'enregistrement du formulaire, le `lieu` du personnage est déjà mis à jour
        nouveau_lieu.disponibilite = "occupé"
        nouveau_lieu.save()

        return redirect('character_detail', id_character=id_character)

    return render(request, 'playground/character_detail.html', {'character': character, 'form': form})
