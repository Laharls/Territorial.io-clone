# Territorial.io Clone

Un jeu de stratégie inspiré de [Territorial.io](https://territorial.io/), développé en Python avec Pygame dans le cadre d'un projet académique.

## 📋 Description

Ce projet est un clone simplifié du jeu de conquête territoriale Territorial.io. Le joueur doit conquérir des territoires en affrontant des adversaires contrôlés par une IA basique. Le jeu propose une génération procédurale de carte et une interface graphique interactive.

## ✨ Fonctionnalités

- **Génération procédurale de carte** : Utilisation d'un algorithme de diagramme de Voronoï pour créer des territoires aléatoires
- **Détection de clics précise** : Implémentation du ray casting pour identifier le territoire cliqué
- **Intelligence artificielle** : IA basique pour les adversaires contrôlés par l'ordinateur
- **Interface graphique** : Interface complète développée avec Pygame
- **Gameplay stratégique** : Mécanique de conquête de territoires inspirée du jeu original

## 🛠️ Technologies utilisées

- **Python 3**
- **Pygame** : Pour l'interface graphique et la gestion des événements
- **Algorithmes géométriques** : Diagramme de Voronoï, ray casting
- **IA simple** : Logique de décision pour les adversaires

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Clonez le repository :
```bash
git clone https://github.com/Laharls/Territorial.io-clone.git
cd Territorial.io-clone
```

2. Installez les dépendances :
```bash
pip install pygame
```

3. Lancez le jeu :
```bash
python main.py
```

## 🎮 Comment jouer

1. Au lancement, une carte avec plusieurs territoires est générée aléatoirement
2. Cliquez sur un territoire adjacent pour tenter de le conquérir
3. Gérez vos troupes et votre stratégie pour dominer l'ensemble de la carte
4. Affrontez les adversaires IA qui tentent également de conquérir des territoires

## 📐 Architecture technique

### Génération de carte (Diagramme de Voronoï)
La carte est générée en plaçant des points aléatoires et en créant des régions où chaque pixel appartient au point le plus proche, formant ainsi des territoires naturels.

### Détection de territoires (Ray Casting)
L'algorithme de ray casting est utilisé pour déterminer précisément quel territoire a été cliqué par le joueur, même avec des formes complexes.

### IA des adversaires
Les adversaires utilisent une IA basique qui évalue les territoires adjacents et prend des décisions de conquête selon des critères simples (nombre de troupes, position stratégique).

## 📚 Contexte académique

Ce projet a été développé dans le cadre d'un cours de programmation Python pour mettre en pratique :
- Les structures de données complexes
- Les algorithmes géométriques
- La programmation orientée objet
- Le développement d'interfaces graphiques avec Pygame
- L'implémentation d'IA basique

## 🔮 Améliorations possibles

- [ ] Ajout de différents niveaux de difficulté pour l'IA
- [ ] Multijoueur local ou en réseau
- [ ] Système de sauvegarde de parties
- [ ] Graphismes plus élaborés et animations
- [ ] Sons et musique
- [ ] Système de progression et de statistiques
