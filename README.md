# Inlämningsuppgift – DevOps Pipeline med testning av fullstack-applikation

Det här är min inlämning i kursen DevSecOps. Jag har byggt en enkel fullstack-applikation med en backend i Flask och en frontend i HTML och JavaScript. Man kan lägga till, läsa, ändra och ta bort uppgifter (CRUD).

## Funktioner

- API med GET, POST, PUT och DELETE  
- Alla uppgifter sparas i en fil som heter `tasks.json`  
- Enkel användargränssnitt där man kan hantera sina uppgifter  
- Testning med Pytest (för backend)  
- Testning med Playwright (för frontend)  
- Automatiska tester via GitHub Actions när man pushar  

## Så här kör man projektet

För att köra projektet:

1. Installera alla paket:  
   `pip install -r requirements.txt`

2. Starta backend:  
   `python app.py`

3. Öppna frontend i webbläsaren:  
   Öppna `frontend/index.html`

## Tester

### Backend – Pytest

- Testerna finns i `tests/test_app.py`
- De testar att alla API-anrop fungerar som de ska

### Frontend – Playwright

- Testerna finns i `tests-frontend/frontend.spec.js`
- De testar att sidan laddas, att man kan lägga till uppgifter, markera dem som klara, ta bort dem och att tomma uppgifter inte läggs till
- Kör testerna med:  
  `npx playwright test`

## GitHub Actions

Jag har gjort ett workflow i `.github/workflows/test.yml` som kör backend-testerna automatiskt när man pushar till GitHub.

## Postman

Jag har också gjort en Postman Collection (filen heter `Taskmaster API.postman_collection.json`) där alla API-anrop finns sparade. Den innehåller GET, POST, PUT och DELETE.

## Sammanfattning

Allt funkar som det ska. Backend och frontend körs lokalt, testerna fungerar och pipelines är på plats. Jag har testat med både Postman och automatiska tester.
