from .models import Character, Equipement

def mettre_a_la_piscine(character):
    if character.etat == "reposé" and character.lieu.id_equip == "maison":
        piscine = Equipement.objects.get(id_equip="piscine")
        if piscine.is_free():
            piscine.nombre_actuel += 1
            piscine.save()
            character.lieu.nombre_actuel -= 1
            character.lieu.save()
            character.lieu = piscine
            character.etat = "fatigué"
            character.save()
            return True
    return False

def mettre_sur_un_velo(character):
    if character.etat == "fatigué" and character.lieu.id_equip == "piscine":
        velo = Equipement.objects.get(id_equip="vélo")
        if velo.is_free():
            velo.nombre_actuel += 1
            velo.save()
            character.lieu.nombre_actuel -= 1
            character.lieu.save()
            character.lieu = velo
            character.etat = "épuisé"
            character.save()
            return True
    return False

def mettre_sur_la_piste(character):
    if character.etat == "épuisé" and character.lieu.id_equip == "vélo":
        piste = Equipement.objects.get(id_equip="piste")
        if piste.is_free():
            piste.nombre_actuel += 1
            piste.save()
            character.lieu.nombre_actuel -= 1
            character.lieu.save()
            character.lieu = piste
            character.etat = "entraîné"
            character.save()
            return True
    return False

def mettre_dans_maison(character):
    if character.etat == "entraîné" and character.lieu.id_equip == "piste":
        maison = Equipement.objects.get(id_equip="maison")
        if maison.is_free():
            maison.nombre_actuel += 1
            maison.save()
            character.lieu.nombre_actuel -= 1
            character.lieu.save()
            character.lieu = maison
            character.etat = "reposé"
            character.save()
            return True
    return False
