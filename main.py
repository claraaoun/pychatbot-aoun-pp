import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def print_list(file_list):
    for file_name in file_list:
        print(file_name)

def extraction_nom(tab_fichiers):
    tab_nom=[]
    for noms in tab_fichiers:
        noms_sans_txt=noms.split(".")[0]
        nom=noms_sans_txt.split("_")[1]
        tab_nom.append(nom)

    return tab_nom


def associer_prenom_president(nom_complet):
    if nom_complet=="Chirac1" or nom_complet=="Chirac2":
        return "Jacques"
    if nom_complet=="Sarkozy":
        return"Nicolas"
    if nom_complet=="Giscard dEstaing":
        return"Valéry"
    if nom_complet=="Hollande":
        return"François"
    if nom_complet=="Macron":
        return"Emmanuel"
    if nom_complet=="Miterrand1" or "Miterrand2":
        return"François"


def afficher_noms_president(L):
    print(L)



def conversion_texte(L):
    cleaned_folder = "cleaned"
    for name in L:
        filename = "speeches/Nomination_" + name + ".txt"
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
        nv_content=""
        for i in content:
            if ord(i)>=65 and ord(i)<=90:
                i=chr(ord(i)+32)
            nv_content=nv_content+i
        nv_filename = os.path.join(cleaned_folder, "Nomination_" + name + "minuscule.txt")

        with open(nv_filename,'w', encoding="utf-8") as file:
            file.write(nv_content)

def supprimer_ponctuation(L):
    cleaned_folder = "cleaned"
    for name in L:
        filename = "cleaned/Nomination_" + name + "minuscule.txt"
        nv_filename = os.path.join(cleaned_folder, "Nomination_" + name+ "cleaned.txt")
        with open(filename, 'r', encoding="utf-8") as file:
            contenu = file.read()
            ponctuations = ".,'-+=?!"
            nv_contenu= ""

            for i, char in enumerate(contenu):
                if char == '\n' or char == '':
                    nv_contenu += ' '
                elif char in ponctuations and contenu[i+1] != ' ':
                    nv_contenu += ' '
                elif char in ponctuations:
                    nv_contenu += ' '
                else:
                    nv_contenu += char

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(nv_contenu)

def compter_mot(dossier, file):
    dictionnaire = {}
    path = dossier + "/" + file
    with open(path, "r", encoding="utf-8") as f:
        contenu = f.read()
        liste_mot = contenu.split(" ")
        for mot in liste_mot:
            if mot in dictionnaire.keys():
                dictionnaire[mot] += 1
            else:
                dictionnaire[mot] = 1
    return dictionnaire

def occurence(terme, dossier, document):
    occ = 0
    path = dossier + "/" + document
    with open(path, "r", encoding="utf-8") as f:
        contenu = f.read()
        liste_mot = contenu.split(" ")
        for mot in liste_mot:
            if mot == terme:
                occ += 1
        return occ

def tf(terme, dossier, document):
    occ = 0
    path = dossier + "/" + document
    with open(path, "r", encoding="utf-8") as f:
        contenu = f.read()
        liste_mot = contenu.split(" ")
        for mot in liste_mot:
            if mot == terme:
                occ += 1
        return occ / len(liste_mot)

def ensemble_mot(dossier, filenames):
    ensemble = set()
    for file in filenames:
        path = dossier + "/" + file
        with open(path, "r", encoding="utf-8") as f:
            contenu = f.read().split()
            for mot in contenu:
                ensemble.add(mot)
    return ensemble




# supprimer le mot vide
def supprimer_mot_vide(dictionnaire):
    dictionnaire.pop("")
def calculer_frequence():
    with open(nom_texte, 'r') as file:
        contenu = file.read()
        dictionnaire = compter_mot(contenu)

        total_mots = sum(dictionnaire.values())

        for mot, nombre_occurrences in dictionnaire.items():
            frequence = nombre_occurrences / total_mots
            print(f"Le mot '{mot}' a une fréquence de {frequence:.4f}")

        return

