# Pomodoro Timer Web App Architecture

## Overview

This project uses Flask as a minimal backend to serve a static web application.
The timer logic is handled in client-side JavaScript, while Flask provides the HTML entry point and can be extended later for settings persistence or history APIs.

## Recommended Structure

```
1.pomodoro/
├── app.py
├── pomodoro.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── styles.css
    └── js/
        ├── app.js
        ├── timer.js
        ├── storage.js
        └── tests/
            ├── timer.test.js
            └── storage.test.js
```

## Components

- `app.py`
  - Flask application entry point
  - Contains `create_app(config=None)` factory for testable setup
  - Serves `index.html` and optional API endpoints

- `pomodoro.py`
  - Encapsulates business logic for Pomodoro durations, mode transitions, and progress calculation
  - Keeps backend logic separate from HTTP routing

- `templates/index.html`
  - Defines the page structure and UI layout
  - Contains the timer card, buttons, and mode controls

- `static/css/styles.css`
  - Defines visual style, layout, responsiveness, and theme

- `static/js/app.js`
  - Handles DOM interactions and user events
  - Connects UI elements to timer and storage logic

- `static/js/timer.js`
  - Contains pure timer functions:
    - start, pause, reset
    - mode selection
    - duration formatting
    - progress calculation
  - Designed for easy unit testing

- `static/js/storage.js`
  - Abstracts persistence operations such as `localStorage`
  - Provides a mockable interface for client-side tests

## Data Flow

1. Browser requests `/`
2. Flask serves `index.html`
3. `app.js` initializes the UI and loads saved settings
4. User interacts with controls: start, pause, reset, mode change
5. `timer.js` updates remaining time and progress each second
6. `storage.js` persists preferences locally

## Testing Strategy

- Backend
  - Use `pytest` against `app.py` and `pomodoro.py`
  - Validate routes and optional settings APIs

- Frontend
  - Unit test pure functions in `static/js/timer.js`
  - Test storage abstraction in `static/js/storage.js`
  - Keep DOM interactions minimal and isolated in `app.js`

## Design Benefits

- Clean separation between server, business logic, UI, and persistence
- Client-side timer provides responsive behavior without server latency
- Modular JS enables straightforward unit testing
- Flask remains lightweight and extensible for future features
