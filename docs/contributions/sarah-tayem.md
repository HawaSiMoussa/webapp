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

1. [# DD-07: Verbesserung des Header-Designs](design-decisions/dd-06.md)
2. [# DD-08: Verwendung von Mailto statt Flask-Mail ](/design-decisions/dd-09.md)
3. [# DD-9: Views eines Posts tracken](/design-decisions/dd-10.md)
3. [# DD-10:Kein separates Nachrichtensystem für das Fundbüro](/design-decisions/dd-11.md)

## My Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
|---|---|---|---|
| 1 | **Mail-to-Funktion im Feed:** User können bequem auf das Mail-Icon klicken und schon wird eine vorgefertigte E-Mail erzeugt, die nur noch abgeschickt werden muss. | Die Usability wird dadurch stark unterstrichen, da der User nicht erst selber eine Nachricht verfassen und nicht erst die Empfängeradresse raussuchen muss. | Leider hatte ich viele Fehler, dass die E-Mail-Adresse des Empfängers nicht richtig in die Mailvorlage übertragen wurde. Ich habe beim Datenabruf manchmal vergessen, dass zwischen den Dateien eine konkrete Verknüpfung herrscht. |
| 2 | **Profilbearbeitungsfunktion:** Der User kann seine Profildaten (außer die E-Mail) selbstständig korrigieren. | Diese Contribution verbessert ebenfalls die Usability stark, da Nutzer falsch angegebene Daten einfach korrigieren können, was im Alltag oft passiert. | Hier war die Koordination schwierig. Ich musste koordinieren, dass Daten aus dem User-Modell aufgerufen, geändert und dann erfolgreich in der Datenbank aktualisiert werden. |
| 3 | **Bootstrap Icons:** Verwendung von echten Icons im Profil, beim Bearbeiten und im Feed statt der ursprünglichen Emojis. | Icons stärken die User Experience. Zudem wirkt die Seite professioneller, moderner und ist für das Auge deutlich angenehmer. | Ich musste mich zunächst mit der Einbindung von Bootstrap Icons vertraut machen und passende Icons auswählen, die die Benutzeroberfläche sinnvoll unterstützen. |

---

## Contributions 

| Contribution | Proof, e.g., git commits | Sources used |
| :--- | :--- | :--- |
| Entwicklung und Erweiterung der Datenbankstruktur für Benutzer- und Postdaten | Data model, commit: `5e5e8080ed932f63c9c4537b9a0af9fd65e7f6ab` | Vorlesungsfolien, Kursmaterial |
| Implementierung des Feeds (Home-Ansicht) inklusive Anzeige aller Posts (`home.html` und Route home) | commit: `ab60ee7886dfefd6e361a6d27cd55835fd84a8c6`, commit: `3e3db0e5055842671c48928e40733c14f174b560` | Vorlesungsmaterialien (Notebook); Für Flask-Mail: https://codingnomads.com/send-emails-with-python-flask-mail, https://pythonbasics.org/flask-mail/, https://flask-mail.readthedocs.io/en/latest/, https://learnmodernpython.com/flask-python-flask-mail-sending-emails-made-simple/, KI (ChatGPT) |

## Quellen, die für das Verständnis genutz wurden

Für Jinja:
Websites:
https://flask.palletsprojects.com/en/stable/tutorial/templates/,
https://jinja.palletsprojects.com/en/stable/templates/#html-escaping,
https://www.iditect.com/faq/python/how-to-get-current-url-in-jinja2flask.html

## AI Directory

## AI Directory

[You must maintain a comprehensive AI Directory, as per [FB1 Regulations on Generative AI Use](../assets/pdf/FB1_KI_Regelung_DE_ENG.pdf). "Catch-all" disclosure (like "AI Tool used for bugfixing") is generally not sufficient. You may list an *AI Tool* multiple times, e.g., if you have used it for different purposes / in different parts of your project. Any use of Agentic AI is **forbidden**.]

| #   | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| 01| ChatGPT    | Debugging  |  Zb. „bei dem code gibts fehler mit der einrückung, wo ist der Fehler?“
„Das wird mir an Fehlermeldungen in der Konsole ausgegeben, was ist genau der Fehler?“
„Warum sehe werden meine Bootstrap-Icons nicht angezeigt?“
                             | :--                         |
| 02 |ChatGPT     |   Branch: FlaskMailTest: mail.py             |    „Wie schätz du den Aufwand ein, wenn man Flask Mail in eine Web-App implementiert statt der Mail-To Funktion mit HTML“
„Wie genau funktioniert Flask-Mail und welche Nachteile hat es?“
                             |                             |
| 03  | ChatGPT     |                |                                 |                             |
| ... |         |                |                                 |                             |