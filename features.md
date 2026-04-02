# Features à implémenter

## Backend
- Application Flask (`1.pomodoro/app.py`)
  - factory `create_app(config=None)`
  - route `/` servant `index.html`
  - API facultatives pour la sauvegarde des paramètres ou l’historique

## Business logic
- `pomodoro.py`
  - durées par défaut des modes
  - transition entre modes (Pomodoro, pause courte, pause longue)
  - calcul de durée restante et d’avancement

## Interface utilisateur
- `templates/index.html`
  - affichage du timer
  - boutons démarrer / pause / réinitialiser
  - contrôles de sélection de mode
  - barre de progression et état courant

## Style
- `static/css/styles.css`
  - apparence et mise en page
  - responsive design

## Logique client
- `static/js/app.js`
  - initialisation du DOM
  - gestion des événements utilisateur
  - liaison entre UI, timer et stockage
- `static/js/timer.js`
  - démarrer / mettre en pause / réinitialiser
  - sélection de mode
  - formatage du temps
  - mise à jour chaque seconde
- `static/js/storage.js`
  - abstraction de `localStorage`
  - lecture/écriture des préférences

## Fonctionnalités utilisateur
- démarrer le timer
- mettre en pause
- réinitialiser
- changer de mode
- afficher le temps restant
- afficher la progression
- sauvegarder et recharger les paramètres

## Tests
- backend : tests pour `app.py` et `pomodoro.py`
- frontend : tests pour `static/js/timer.js` et `static/js/storage.js`
