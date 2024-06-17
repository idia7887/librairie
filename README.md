# Objectif : Créer une application de gestion de bibliothèque qui permet:
# d'ajouter des livres,
# de rechercher des livres,
# de prêter des livres
# de retourner des livres
# installation de l'environnement virtuel venv avec la commande
# python -m venv venv
# activation de l'environnement avec la commande 
 # creation du fichier requirement 
 # installation de pytest  pip install pytest 
 # test unitaires fichier book
 ### Documentation pour les Tests Unitaires de la Classe `Book` avec `pytest`

# Introduction
Ce document décrit les tests unitaires pour la classe `Book` en utilisant le framework de test `pytest`. La classe `Book` est définie avec les attributs `title` et `author`, et une méthode `__str__` qui renvoie une représentation textuelle du livre.

# Structure du Projet

```
project/
│
├── book.py
├── test_book.py
└── README.md
```

- `book.py` : Contient la définition de la classe `Book`.
- `test_book.py` : Contient les tests unitaires pour la classe `Book`.

# Code de la Classe `Book` (`book.py`)

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
```
# Description des Tests

1. Test d'Initialisation (`test_book_initialization`)** :
   - Objectif : Vérifier que les attributs `title` et `author` sont correctement initialisés.
   - Procédure : 
     - Créer une instance de `Book` avec le titre "The Great Gatsby" et l'auteur "F. Scott Fitzgerald".
     - Utiliser des assertions pour vérifier que `book.title` et `book.author` sont correctement assignés.

2. Test de la Méthode `__str__` (`test_book_str`) :
   - **Objectif** : Vérifier que la méthode `__str__` renvoie la chaîne de caractères attendue.
   - **Procédure** :
     - Créer une instance de `Book` avec le titre "1984" et l'auteur "George Orwell".
     - Utiliser une assertion pour vérifier que la méthode `__str__` renvoie "1984 by George Orwell".

#### Conclusion

Les tests unitaires permettent de s'assurer que la classe `Book` fonctionne comme prévu en vérifiant l'initialisation des attributs et la méthode `__str__`. L'exécution des tests avec `pytest` garantit que les fonctionnalités de base de la classe sont correctes et aide à détecter les régressions lors des modifications futures.

# pour le fichier library 
/votre_projet/
    library.py
    test_library.py

Explication des Tests

Fixtures :

library(): Crée une instance de Library pour être utilisée dans les tests.
book(): Crée une instance de Book pour être utilisée dans les tests.

Tests :

test_add_book(library, book): Vérifie si un livre est correctement ajouté à la bibliothèque.
test_remove_book(library, book): Vérifie si un livre est correctement retiré de la bibliothèque.
test_remove_book_not_in_library(library, book): Vérifie que la suppression d'un livre non présent dans la bibliothèque lève une exception ValueError.
test_find_book_by_title(library, book): Vérifie si un livre peut être trouvé par son titre.
test_find_book_by_title_not_found(library): Vérifie que la recherche d'un livre non existant retourne None.
test_list_books(library, book): Vérifie si la liste des livres est correctement retournée.
test_list_books_empty(library): Vérifie que la liste des livres est vide lorsque aucun livre n'est ajouté.
Exécution des Tests
Pour exécuter les tests, exécutez la commande suivante dans le terminal à partir du répertoire contenant test_library.py :

pytest test_library.py


