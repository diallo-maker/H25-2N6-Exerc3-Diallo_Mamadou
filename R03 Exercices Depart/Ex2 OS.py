import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{os.getcwd()}")



# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{os.environ.get('USERPROFILE')}")



# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
os.chdir("C:/Users/1856207\Documents")
print(f"Q3{os.getcwd()}")


# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'


os.chdir("C:/Users/1856207/Documents")
print(f"Q4{os.listdir()}")

# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
os.chdir('C:/Users/1856207/Documents')
os.makedirs('OS-ExercQ5', exist_ok=True)
print(f"Q5{os.listdir()}")





# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'

os.chdir('C:/Users/1856207/Documents')
os.makedirs('OS-ExercQ6/Subdir1', exist_ok=True)
print(f"Q6{os.listdir()}")



#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire

os.rename('Subdir1', 'Sous_repertoire')
print(f"Q6{os.listdir()}")



# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'

os.remove('Subdir1')
os.rmdir('OS-ExercQ6')
print(f"Q6{os.listdir()}")





