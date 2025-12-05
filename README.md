Inlämningsuppgift: DevOps Pipeline med testning av fullstack-applikation

Detta är min inlämning i DevSecOps kursen. Jag har gjort ett enkelt API med Flask där man kan skapa, läsa, ändra och ta bort uppgifter. Jag har också lagt till tester med pytest och ett workflow med GitHub Actions som kör testerna automatiskt.

All data sparas i en fil som heter tasks.json.
För att köra programmet kör man bara app.py. Man kan också testa API:et med Postman. Jag har sparat alla anrop i en collection som ligger med i projektet. Jag har testat GET, POST, PUT och DELETE.

Jag har också lagt till ett test_yml i .github mappen så att tester körs varje gång man pushar till GitHub.

Testerna ligger i test_app.py och testar alla fyra endpoints.

Jag har använt requirements.txt för att installera alla paket som flask och pytest.

Allt fungerar och är klart.