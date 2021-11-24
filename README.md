# LITReview
 
# Projet OC n°9 
# Introduction: Il s'agit d'une application qui permet aux utilisateurs de demander des critiques, créer des critiques et les modifier, répondre aux demandes de critiques, suivre et arrêter de suivre d'autres utilisateurs

L'application dispose d'une base de données qui permet la création d'utilisateurs et la sauvegarde des actions initiées par les utilisateurs

Lancez un terminal

Récupérez l'ensemble du projet :

`git clone https://github.com/atarax-dev/LITReview.git`

Placez-vous dans le répertoire qui contient le fichier manage.py

Pour pouvoir lancer le programme, créez un environnement virtuel:

`python -m venv venv`

Activez l'environnement :

`source venv/Scripts/activate` (sous windows)

`source venv/bin/activate` (sous Mac ou linux)

Installez les packages requis à l'aide de la commande suivante:

`pip install -r requirements.txt` 

# Utilisation 

Toujours depuis le répertoire qui contient manage.py dans le terminal, exécutez le programme:

`python manage.py runserver`

Puis ouvrez votre navigateur et allez sur la page suivante : http://127.0.0.1:8000/