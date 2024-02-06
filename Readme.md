# Projet d'Indexation de Documents Web

Ce projet implémente la création d'indices non positionnels et positionnels à partir d'un ensemble de documents web récupérés et stockés au format JSON. Il utilise le stemming pour améliorer la pertinence de l'indexation et génère des statistiques descriptives sur le jeu de données.

## Structure du Projet

Le projet est organisé en plusieurs modules pour faciliter la maintenance et l'évolutivité du code :

- `crawler_data_reader.py` : Module pour lire les données JSON.
- `tokenizer.py` : Module pour tokeniser les textes des documents.
- `advanced_data_processing.py` : Module pour appliquer des traitements avancés comme le stemming.
- `index_builder.py` : Module pour construire les indices non positionnels et positionnels.
- `statistics_generator.py` : Module pour générer des statistiques sur les documents.
- `file_writer.py` : Module pour écrire les résultats dans des fichiers JSON.
- `main.py` : Script principal qui orchestre l'exécution du projet.

## Dépendances

Ce projet nécessite Python 3 et les paquets suivants :

- `nltk` pour le stemming.

Assurez-vous d'avoir installé toutes les dépendances nécessaires :

```bash
pip install nltk
```

## Exécution du Projet

Pour exécuter le projet, naviguez dans le répertoire du projet et lancez le script `main.py` :

```bash
python main.py
```

Avant d'exécuter le script, assurez-vous de configurer le chemin vers votre fichier JSON contenant les données du crawler dans `main.py`.

## Résultats

L'exécution du script génère plusieurs fichiers JSON :

- `title.non_pos_index.json` : L'index non positionnel.
- `mon_stemmer.title.non_pos_index.json` : L'index non positionnel avec application du stemming.
- `title.pos_index.json` : L'index positionnel.
- `metadata.json` : Les statistiques descriptives sur les documents.

## Personnalisation

Vous pouvez personnaliser le traitement en modifiant les fonctions dans les différents modules, par exemple en changeant le stemmer utilisé ou en ajustant la manière dont les tokens sont générés.

```
