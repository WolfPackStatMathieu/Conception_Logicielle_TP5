def is_vegan(ingredients):
    is_vegan = True
    for ingredient in ingredients:
        if "vegan" in ingredient:
            if ingredient["vegan"] != "yes":
                is_vegan = False
    return is_vegan

from functools import reduce
requetes = [{'cle':'valeur1', 'class':'A','is_vegan':True},{'cle':'valeur2', 'class':'A','is_vegan':True},{'cle':'valeur3', 'class':'B','is_vegan':False}]
is_vegan_reduce = lambda accumulateur,element_itere : accumulateur == accumulateur & element_itere['is_vegan']
resultat = reduce(is_vegan_reduce,requetes,True) # False

## En contexte on peut les enchainer !
class_is_a = lambda requete : requete['class'] == 'A'
resultat_avec_filtre = reduce(is_vegan_reduce,filter(class_is_a,requetes),True) # True
