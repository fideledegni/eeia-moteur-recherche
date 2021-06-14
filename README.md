# École d'Été en IA: projet moteur de recherche

## Avant de commencer

**Pour Python :**

Installer avec pip tous les packages du fichier `requirements.txt` avec la commande : `pip install -r requirements.txt`

Si vous utilisez de nouveaux packages Python, faire `pip freeze > requirements.txt` pour mettre à jour les dépendances

**Pour Node :**

Faire `npm install` pour installer les dépendances node


## Build en local

Faire : `npm run build`


## Build avant push sur github (pour la prod)
Faire : `npm run build-production`


## Pour lancer le serveur local:

Faire : `python manage.py runserver`


## S'il y a eu des modifications aux models

Faire `python manage.py makemigrations` pour ajoute les nouveaux models si nouvelles créations

Faire `python manage.py migrate` pour appliquer les changements sur la base

