# Plan d’implémentation Pomodoro

## 1. Préparer la structure du projet
- Créer le dossier `1.pomodoro/` si nécessaire
- Ajouter les fichiers suivants :
  - `app.py`
  - `pomodoro.py`
  - `templates/index.html`
  - `static/css/styles.css`
  - `static/js/app.js`
  - `static/js/timer.js`
  - `static/js/storage.js`

## 2. Backend minimal
- Implémenter `create_app(config=None)` dans `1.pomodoro/app.py`
- Ajouter une route `/` qui sert `index.html`
- Vérifier que le serveur Flask démarre correctement

## 3. Maquette HTML
- Créer `templates/index.html`
- Inclure :
  - le titre de l’application
  - l’affichage du minuteur
  - les boutons `Démarrer` / `Réinitialiser`
  - la zone de la barre circulaire de progression
  - la section de résumé `今日の進捗`

## 4. Logique métier Pomodoro
- Implémenter `pomodoro.py`
  - définir les durées par défaut des modes
  - gérer les modes `travail`, `pause courte`, `pause longue`
  - calculer le temps restant
  - calculer le pourcentage de progression
- Garder la logique testable indépendamment du front

## 5. Timer client pur
- Créer `static/js/timer.js`
  - fonctions `start()`, `pause()`, `reset()`
  - mise à jour chaque seconde
  - format `MM:SS`
  - calcul de la portion de cercle remplie
- Gérer les états : arrêt, pause, en cours

## 6. Liaison UI / timer
- Créer `static/js/app.js`
  - récupérer les éléments du DOM
  - initialiser l’interface
  - lier les événements des boutons au timer
  - mettre à jour l’affichage du temps et du cercle
  - afficher le mode et l’état courant

## 7. Persistance locale
- Créer `static/js/storage.js`
  - lecture/écriture dans `localStorage`
  - sauvegarde du mode courant et des préférences
  - chargement des données au démarrage

## 8. Style et rendu visuel
- Créer `static/css/styles.css`
  - apparence principale et mise en page
  - fond dégradé violet et card blanche
  - boutons arrondis
  - rendu responsive

## 9. Synthèse des progrès
- Ajouter la section de suivi des progrès :
  - nombre de sessions terminées
  - temps de concentration total
- Mettre à jour ces valeurs à la fin de chaque cycle

## 10. Tests
- Backend : tester `app.py` et `pomodoro.py`
- Frontend : tester `static/js/timer.js` et `static/js/storage.js`
- Vérifier la cohérence de l’interface et des transitions

## 11. Améliorations
- Ajouter des transitions CSS si nécessaire
- Ajouter des notifications sonores ou visuelles
- Ajouter une API d’historique côté backend si besoin
