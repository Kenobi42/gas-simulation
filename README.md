# gas-simulation
Une simulation physique (avec animation en temps réel) du comportement de particules d'hydrogène dans un système fermé.
Chaque particule existe comme "item" indépendant, mais sa réalité physique est encodé sur un automate cellulaire 2D qui assure les interactions entre particules.

Actuellement le code est composé de :
-Particules ayant une position et une vitesse aléatoire
-Collisions élastiques entre particules et bordures du système

Améliorations à venir :
-Collisions élastiques entre plusieurs particules
-Ajout d'énergie au système
-Vérification de la distribution en vitesse de Botzmann
