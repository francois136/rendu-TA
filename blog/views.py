from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement
from .controle import mettre_a_la_piscine, mettre_sur_un_velo, mettre_sur_la_piste, mettre_dans_maison
from django.contrib import messages

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'playground/character_list.html', {'characters': characters})

def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    form = MoveForm(request.POST or None, instance=character)
    if request.method == "POST" and form.is_valid():
        action_performed = False
        action = request.POST.get('action')
        if action == "piscine":
            action_performed = mettre_a_la_piscine(character)
        elif action == "velo":
            action_performed = mettre_sur_un_velo(character)
        elif action == "piste":
            action_performed = mettre_sur_la_piste(character)
        elif action == "maison":
            action_performed = mettre_dans_maison(character)
        
        if action_performed:
            messages.success(request, "Action effectuée")
        else:
            messages.error(request, "Action impossible")
        return redirect('character_detail', id_character=id_character)
    return render(request, 'playground/character_detail.html', {'character': character, 'form': form})
