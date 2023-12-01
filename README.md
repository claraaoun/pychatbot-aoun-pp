# pychatbot-aoun-pp
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
tab=list_of_files("speeches-20231128",".txt")
print(tab)
def extraction_nom(tab_fichiers):
    tab_nom=[]
    for noms in tab_fichiers:
        noms_sans_txt=noms.split(".")[0]
        nom=noms_sans_txt.split("_")[1]
        tab_nom.append(nom)

    return tab_nom
resultat=extraction_nom(tab)
print(resultat)

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


def afficher_noms_president():
    L_noms=["Chirac","Giscard dEstaing","Hollande","Macron","Miterrand","Sarkozy"]
    print(L_noms)

afficher_noms_president()

def conversion_texte(nom_texte):
    cleaned_folder = "cleaned"

    filename = "speeches-20231128/Nomination_" + nom_texte + ".txt"
    with open(filename, 'r') as file:
        content = file.read()
    nv_content=""
    for i in content:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
        nv_content=nv_content+i
    nv_filename = os.path.join(cleaned_folder, "Nomination_" + nom_texte + "minuscule.txt")

    with open(nv_filename,'w') as file:
        file.write(nv_content)

def supprimer_ponctuation(nom_texte):
    cleaned_folder = "cleaned"

    filename = "cleaned/Nomination_" + nom_texte + "minuscule.txt"
    nv_filename = os.path.join(cleaned_folder, "Nomination_" + nom_texte + "cleaned.txt")
    with open(filename, 'r') as file:
        contenu = file.read()
    ponctuations = " .,'-+=?!"
    nv_contenu= ""
    for i, char in enumerate(contenu):
        if char in ponctuations and contenu[i+1] != ' ':
            nv_contenu += ' '
        else:
            nv_contenu += char

    with open(filename, 'w') as file:
        file.write(nv_contenu)

def compter_mot(contenu):
    dictionnaire = {}
    liste_mot = contenu.split(" ")
    for mot in liste_mot:
        if mot in dictionnaire:
            dictionnaire[mot] += 1
        else:
            dictionnaire[mot] = 1
    print(dictionnaire)

        filename = "cleaned/Nomination_" + nom_texte + "minuscule.txt"
    with open(filename, 'r') as file:
        contenu = file.read()

compter_mot(contenu)


