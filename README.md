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


