---
title: Sarah Tayem
parent: Individual Contributions
nav_order: 2
---
## Target grade
Meine Zielnote in diesem Kurs liegt ebenfalls zwischen 1,3 und 1,7.

## Personal Goals
Ich selber hab nicht viel Wissen über WebApps genau und habe nur ein paar mal davon gehört, deshalb möchte ich mithilfe dieses Kurses, wenn mich jemand fragt "Was genau ist eine webApp, wie funktioniert sie und was unetrscheidet sie von einer normalen App?" Mit Leichtigkeit und Richtigkeit beantworten können. Ich möchte auch stolz auf mein erarbeites Projekt sein und, wie ich es auch bei restlichen Projekten in anderen Kursen tat, immer wieder was neues bezüglich des arbeiten in Projekten lernen (Projektmanagement). Ich möchte auch Python erlernen, ohne dass ich ständig eine KI fragen stellen muss. Mein Ziel ist es Python so zu erlernen, dass ich die Syntaxt völlig verstehe und Fehler in fremden Codes z.B. erkennen kann. Ich denke diese Kenntnisse sind besonders hilfreich für meine Zukunft, da ich nicht jemand sein möchte der nur "weiß", sondern sich auch auskennt.

## Eidesstattliche Erklärung

**[Sarah Tayem, Matrikelnr.: 77209886771]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.


## Design Decisions that I led

1. [# DD-07: Verbesserung des Header-Designs](../design-decisions/dd-07.md)
2. [# DD-08: Verwendung von Mailto statt Flask-Mail ](../design-decisions/dd-08.md)
3. [# DD-9: Views eines Posts tracken](../design-decisions/dd-09.md)
3. [# DD-10:Keine differenzierung zwischen Fundbüro und Standarduser](../design-decisions/dd-10.md)

## My Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
|---|---|---|---|
| 1 | **Mail-to-Funktion im Feed:** User können bequem auf das Mail-Icon klicken und schon wird eine vorgefertigte E-Mail erzeugt, die nur noch abgeschickt werden muss. | Die Usability wird dadurch stark unterstrichen, da der User nicht erst selber eine Nachricht verfassen und nicht erst die Empfängeradresse raussuchen muss. | Leider hatte ich viele Fehler, dass die E-Mail-Adresse des Empfängers nicht richtig in die Mailvorlage übertragen wurde. Ich habe beim Datenabruf manchmal vergessen, dass zwischen den Dateien eine konkrete Verknüpfung herrscht. |
| 2 | **Profilbearbeitungsfunktion:** Der User kann seine Profildaten (außer die E-Mail) selbstständig korrigieren. | Diese Contribution verbessert ebenfalls die Usability stark, da Nutzer falsch angegebene Daten einfach korrigieren können, was im Alltag oft passiert. | Hier war die Koordination schwierig. Ich musste koordinieren, dass Daten aus dem User-Modell aufgerufen, geändert und dann erfolgreich in der Datenbank aktualisiert werden. |
| 3 | **Bootstrap Icons:** Verwendung von echten Icons im Profil, beim Bearbeiten und im Feed statt der ursprünglichen Emojis. | Icons stärken die User Experience. Zudem wirkt die Seite professioneller, moderner und ist für das Auge deutlich angenehmer. | Ich musste mich zunächst mit der Einbindung von Bootstrap Icons vertraut machen und passende Icons auswählen, die die Benutzeroberfläche sinnvoll unterstützen. |

## Contributions 

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Entwicklung und Erweiterung der Datenbankstruktur für Benutzer- und Postdaten | The Data Model, z.B. commits: [Add code to db.py and create model.py for database setup](https://github.com/HawaSiMoussa/webapp/commit/d6b47c5b6c042b0acb617cdc82a20a5684526194),[add database models to db.py](https://github.com/HawaSiMoussa/webapp/commit/5e5e8080ed932f63c9c4537b9a0af9fd65e7f6ab), [correct db.py, add test user to db (testing functionality of the feed using the db)](https://github.com/HawaSiMoussa/webapp/commit/98918647c45b2b3de3bc71503314c9fb809d684d)|Vorlesungsfolien, Kursmaterial |
| Implementierung des Feeds (Home-Ansicht) inklusive Anzeige aller Posts (home.html und Route home) |z.B. commits: [home html, app.py und model.py](https://github.com/HawaSiMoussa/webapp/commit/3a99926362460106e0e2ef897c9e9862f23d3737), [icons added](https://github.com/HawaSiMoussa/webapp/commit/a98ec2ab5195641b2b290d08bc0e5a6a1f3e25d9), [Add email field to posts and update mailto link in home template](https://github.com/HawaSiMoussa/webapp/commit/3f30832ecd6a4c17dccb61a6f34942699a6ce79c), [update html and app.py (add new functions and posts)](https://github.com/HawaSiMoussa/webapp/commit/ab60ee7886dfefd6e361a6d27cd55835fd84a8c6), [add standardtext for mail and if statement to menage post visibility according too user campus](https://github.com/HawaSiMoussa/webapp/commit/c3138903e19d83a2c5693146d516086cf8cba04c)| Volresungsmaterialien (Notebook), Für Mail- Funktion: Vorwissen und die Website: https://www.w3schools.in/html/send-emails-with-html-email-links, Für Flask-Mail:Websites: https://codingnomads.com/send-emails-with-python-flask-mail, https://pythonbasics.org/flask-mail/,https://flask-mail.readthedocs.io/en/latest/, https://learnmodernpython.com/flask-python-flask-mail-sending-emails-made-simple/, KI (ChatGPT)|
| Entwicklung der Profilseite mit Anzeige der Benutzerdaten und aktiven Posts |Branch Sarah2--Profile , z.B. commits:[add profile.html: show user profile infos](https://github.com/HawaSiMoussa/webapp/commit/802cfee19b56101d7e8fb64aeed13b77e356de16), |Vorlesungsdateien(Notebook),[add profile route to app.py](https://github.com/HawaSiMoussa/webapp/commit/104c38961d01a9a40cd865ff25cb572d3fc4d2e8)|
| Implementierung der Funktion „Profil bearbeiten“ zur Änderung von Benutzer- und Kontaktdaten, eigenen Post ansehen und schließen| Branch: Sarah2--Profile, z.B. commits: [add edit profile template](https://github.com/HawaSiMoussa/webapp/commit/b9a96bc4f9e91b0f06ba07ecebe431591e412f72), [add edit profile route](https://github.com/HawaSiMoussa/webapp/commit/e251dfff5b6e4eaa9a5e9560470936d327f0b30c), [add "mein aktiver Post" to the profile page](https://github.com/HawaSiMoussa/webapp/commit/702cbac278f8c74b2103f9073dc26bafcba8ba6d), [add close post functionality (close post route) and show only open post (where command in profile route added)](https://github.com/HawaSiMoussa/webapp/commit/f4f03b255ad9f6c1c61f8fb78422ebd55ba75dbb),[add pencil next to profile instead of next to each profile data field](https://github.com/HawaSiMoussa/webapp/commit/b3e4ca4c1dd09d6957c301537977a01fbeb6ea76)| Vorlesungsdateien(Notebook) |
| Implementierung der Funktion „Post bearbeiten“ für bestehende Fund- und Verlustmeldungen| [add edit post functionality based on create post](https://github.com/HawaSiMoussa/webapp/commit/35fa3004ea28856a0e810a2f302bf2db4eae3715) | Vorlesungsdateien(Notebook) |
| Gestaltung und Implementierung der Navigation Bar in base.html |  z.B. commits:[Add navigation bar, app.py corrected, bootstrap imports in html file](https://github.com/HawaSiMoussa/webapp/commit/cff9c23d38521ed2232b3f9ecfd5e965e540a992),[Refactor templates: remove index.html and integrate navbar into base.html](https://github.com/HawaSiMoussa/webapp/commit/b15c4b9405cb44f8404da4c8833fe40ac9a3d047), [link the profile and contact html to nav bar](https://github.com/HawaSiMoussa/webapp/commit/db36b3132536ed93f4e86a686c395bf4272c76b3)| Bootstrap Website:https://getbootstrap.com/docs/4.0/components/navbar/ + Vorlesungsdateien(Notebook) |
| Überarbeitung des Layouts mit Logo, Titel und Slogan im Header | [crop Logo image to remove title+ motto from image](https://github.com/HawaSiMoussa/webapp/commit/f557c0c766e0e228d205966e56590df7a29f32f0),[add app title + slogan to the base.html](https://github.com/HawaSiMoussa/webapp/commit/45ba4b8e675016ad566370c93cb70ec14db2a7c1)| Bootstrap Documentation |
| Entwicklung eines JSON-Endpunkts zur Bereitstellung von Post-Daten über die API| [Add user session check in home route and implement json API for posts](https://github.com/HawaSiMoussa/webapp/commit/627b8650e2a9eeaf95374831837944d863f4fbd6)| Vorlesungsmaterialien,Website: https://www.geeksforgeeks.org/python/how-to-return-a-json-response-from-a-flask-api/|

## Quellen, die für das Verständnis genutz wurden

Für Jinja:
Websites:
https://flask.palletsprojects.com/en/stable/tutorial/templates/,
https://jinja.palletsprojects.com/en/stable/templates/#html-escaping,
https://www.iditect.com/faq/python/how-to-get-current-url-in-jinja2flask.html



## Quellen für Bootstap Klassen und Icons
(https://bootstrapshuffle.com/classes)
(https://icons.getbootstrap.com/)
## AI Directory

| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | ChatGPT | Fehlerbehebungen | `app.py`, `home.html`, `edit_profile.html`, `db.py` | Zb. „bei dem code gibts fehler mit der einrückung, wo ist der Fehler?“, "Fehlt ein import?", „Das wird mir an Fehlermeldungen in der Konsole ausgegeben, was ist genau der Fehler?“, „Warum sehe werden meine Bootstrap-Icons nicht angezeigt?“ oder es wurde ein Screenshot von den Jinja2 Exceptions gegeben |
| 02 | ChatGPT | Unterstützung bei Git- und GitHub-Problemen, vor Allem Merge Konflikten | Git Repository | Ein Screenshot vom Screen und Prompts wie: "Wie gehe ich jetzt mimt dem Merge Konflikt um, ohne etwas zu verlieren?" "Kannst du mir erklären was ich genau machen muss bei einem Merge Konflikt?", "Warum funktioniert gerade das committen gerade nicht" , "Wie mache ich ein Commit rückgängig?"|
| 03 | ChatGPT | Für Verständnis über Flask-Mail sowie Einschätzung über den Aufwand |  Branch: FlaskMailTest: `mail.py` | „Wie schätz du den Aufwand ein, wenn man Flask Mail in eine Web-App implementiert statt der Mail-To Funktion mit HTML“„Wie genau funktioniert Flask-Mail und welche Nachteile hat es?“  |
| 04 | ChatGPT | Testdaten erstellen | `lostandfound.sqlite` | "Gib mit bitte 5 Beispielpost nach diesem Schema" + Screenshot von unserem Formular|
|05|ChatGPT| Hilfe bei der UI mit Bootstrap | `home.html`, `profile.html`, `base.html`, `create_post.html` | "Welche Bootstrap-Klassen gibt es für Buttons und Container?“
| 06| ChatGPT | Vor dem Erfahren über Bootstrap Icons nutze ich Emojis für die Icons| `home.html`| "Bitte gebe mir ein Emoji für eine Navigation bar, wo drei striche unterienander sind also, wie du hier im Scribble siehst", "Ich brauche ein Emoji für die Mail Funktion, also ein Brief Emoji und auch ein Auge für die Views|



