---
title: Hawa Si Moussa
parent: Individual Contributions
nav_order: 2
---

## Target grade
Meine Zielnote liegt bei 1,3 oder 1,7.

## Personal Goals
Ich möchte verstehen wovon eine Web App abhängt und die einzelnen Schritte vollständig nachvollziehen, um somit in der Zukunft weitere Web-Apps entwickeln zu können. Zudem erhoffe ich mir viele Erfahrungen mit Python und HTML sammeln zu können. Am Ende des Kurses möchte ich eine erfolgreiche und für mich sinnvolle Web App erstellt
haben, die ich mit meinem später erweiterten Wissen und Ideen ausbauen kann.
Ich möchte einen großen nutzen in dieser web app sehen

## Eidesstattliche Erklärung

**[Hawa Si Moussa, Matrikelnr.: 77204183234]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
|---|---|---|---|
| 1 | Fehlertolerantes Suchsystem im Feed | Die Suche ist unabhängig von Groß- und Kleinschreibung. Das spart Usern viel Zeit und verhindert Verwirrung, wenn ein Titel nicht zu 100 % exakt eingetippt wird. | 
| 2 | Sicheres & benutzerfreundliches Auth-System | Das System gibt sofort präzises Feedback (z. B. wenn eine E-Mail bereits vergeben ist) und leitet neu registrierte User ohne nervigen Zweit-Login direkt zum Home-Feed weiter. | Die logische Verknüpfung der Validierung mit automatischen Sessions, um doppelten Eingabeaufwand zu vermeiden. |
| 3 | Strikte HWR-Domain-Validierung | Nur Nutzer mit echten HWR-Mailendungen können Konten anlegen. Das schützt unser digitales Uni-Ökosystem vor externem Spam und Missbrauch. | Die fehlerfreie Prüfung von gleich drei verschiedenen HWR-Mail-Strukturen parallel im Backend. | Außerdem habe ich ebenso bei fehler behebungen meiner komilitonninen mit beigetragen wehslab ich sehr stolz bin da wir uns alle gegenseitig unterstützt haben|

## Design Decisions that I led

1. [DD #01 – Besonderheiten beim Admin](../design-decisions/dd-01.md)
2. [DD #02 – Registrierung und Login Rückmeldung](../design-decisions/dd-02.md)
3. [DD #03 – Die Suche im Feed](../design-decisions/dd-03.md)
4. [DD #04 – Email HWR für das Login und die Registrierung](../design-decisions/dd-04.md) commit: 95c4d52334da081b8f7ecf445eab115efd5a1ada



## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Login html sowie die email validation korrigiert   | login html erstellt für das design sowie den validator richtig getsellt mit den endungen der hwr-mail nochmal | commit proof: e591fdf58a28dd2e01598e340a416488c14f1d63 |
| [Auth] Validierungs-Logik für HWR-E-Mail-Endungen und Feedback-Flashes im Registrierungsformular |  | Flask Flash-Messages Guide |
| [Security] Einbau der automatischen Admin-User-Generierung beim App-Start |  | Flask-SQLAlchemy Context Docs |
| [UI/UX] Entwicklung der HTML-Templates für Login, Registrierung und den Lösch-Button im Home-Feed |  | Bootstrap 5 Components |
| [Database] Definition der Tabellen-Beziehungen (`Campus`, `StandardUser`, `Fundbuero`, `Post`) |  | SQLAlchemy Relationships |
| [Backend] Erstellung der Route `/delete_post` zum permanenten Entfernen von Einträgen aus der DB |  | Flask Route Documentation |
| [Backend] Integration von Passwort-Mindestlängen (8 Zeichen) inklusive Fehlerausgabe |  | WTForms Validators Documentation |
| Packages installiert für email und() und migrate  |  | https://flask-migrate.readthedocs.io/en/latest/ das habe ich genutzt sowie ein email package installiert aber auch migrate installiert https://learn.microsoft.com/de-de/nuget/consume-packages/install-use-packages-visual-studio|

## AI Directory (KI-Verzeichnis)

| # | KI-Tool | Einsatzzweck | Betroffene Bereiche commit | Anmerkungen, Vorgehensweise, Prompts |
| :-: | :--- | :--- | :--- | :--- |
| 01 | Gemini | git commit probleme beheben | beim pushen gab es oft konflikte manchmal auch da wir zu dritt gleichzeitig gearbeitet haben wehslab oft vieles nicht gepusht oder gepullt wurde | Gemini hat mir geholfen diese probleme zu lösen in dem ich z.b den merge vorgang stoppe etc. |
| 02 | Gemini | Logische Fehleranalyse (Debugging) bei Session-Abfragen | `app.py` (Route `/create_post`) | Behebung eines logischen Konflikts beim Versuch, Admin-Rechte (`is_admin`) aus dem regulären User-Filter auszuschließen . |
| 03 | Gemini | Fehleranalyse bei Datenbank-Abfragen (`scalar` vs. `scalars`) | `app.py` (Admin-Generierung beim App-Start) | Erklärung einer Fehlermeldung bezüglich Daten-Typen erhalten. Die KI diente als Hilfe, um den theoretischen Unterschied zwischen der Rückgabe eines Einzelobjekts (.scalar) und einer Liste (.scalars) zu verstehen und zu verstehen wieso der fehler kam bei der nutzung von scalars und nicht bei scalar |
| 04 | Gemini | Validierungs-Logik und Fehler-Handling | `app.py` (Routen `/register` und `/login`) | Hilfestellung beim Verständnis, wie Validierungsfehlern von Formularen denn oftmals hatte ich fehler wir z.B beim login und bei der registrierung denn vom aufbau her waren sie ähnlich aber doie regostrierung hat anfangs nicht geklappt |
| 05 | Chatgbt | bei der app.py in der stelle der Suche der fehler war die schreibweise von password und mehr schreibfehler auf die mich chatgbt hingewiesen hat   | Dokumentation  |  commit prove: e591fdf58a28dd2e01598e340a416488c14f1d63|


