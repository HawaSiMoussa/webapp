---
title: Hawa Si Moussa
parent: Individual Contributions
nav_order: 2
---

## Target grade
Meine Zielnote in diesem Modul liegt bei 1,3 oder    1,7.

## Personal Goals
Ich möchte verstehen wovon eine Web App abhängt und die einzelnen Schritte vollständig nachvollziehen, um somit in der Zukunft weitere Web-Apps entwickeln zu können. Zudem erhoffe ich mir viele Erfahrungen mit Python und HTML sammeln zu können. Am Ende des Kurses möchte ich eine erfolgreiche und für mich sinnvolle Web App erstellt
haben, die ich mit meinem später erweiterten Wissen und Ideen ausbauen kann.
Ich möchte einen großen nutzen in dieser web app sehen und selber von der erarbeitung profitieren. Außerdem möchte ich genauer lernen wie und wo ich design decisions einführen kann, vorallem da man sowas nicht in vielen Kursen lernt. Ich möchte mich so gut auskennen sodass ich KI nicht mehr um hilfe bitten muss bei bestimmten Fehlerbehebungen. 

## Eidesstattliche Erklärung

**[Hawa Si Moussa, Matrikelnr.: 77204183234]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

### Top-3 Contributions 


| # | My contribution | Why I am proud of it | Which challenge I overcame |
|---|---|---|---|
| 1 | Fehlertolerantes Suchsystem im Feed | Die Suche ist unabhängig von Groß- und Kleinschreibung. Das spart Usern viel Zeit und verhindert Verwirrung, wenn ein Titel nicht zu 100 % exakt eingetippt wird, dann wird die Anzeige trotzdessen gefunden und angezeigt. | Die Challenge die ich überstehen musste war vor allem, dass ich nicht nur auf Groß- und Kleinschreibung achten wollte, sondern auch darauf, dass Leerzeichen oder ein Buchstabe der fehlt die Suche auch nicht beeinträchtigen. Hierfür hatte ich allerdings noch keine Lösung bzw. nicht genügend Wissen gehabt. |
| 2 | Sicheres & benutzerfreundliches Authentifikations System | Das System gibt sofort präzises Feedback (z. B. wenn eine E-Mail bereits vergeben ist) und leitet neu registrierte User ohne nervigen Zweit-Login direkt zum HomeFeed weiter. Das spart Zeit und sorgt dafür, dass der User direkt die App entdecken kann. Somit wird der Prozess vereinfacht und beschleunigt. | Die logische Verknüpfung der Validierung und die Weiterleitung zum Feed hat mir sehr viele Probleme bereitet, denn um doppelten Eingabeaufwand zu vermeiden, durfte das Ganze nicht wieder zurück zum Login laufen. |
| 3 | Strikte HWR-Domain-Validierung | Nur Nutzer mit echten HWR-Mailendungen können Konten anlegen. Das schützt unser digitales Uni-Ökosystem vor externem Spam und Missbrauch. | Die fehlerfreie Prüfung von gleich drei verschiedenen HWR-Mail-Strukturen parallel im Backend. |



## Design Decisions that I led

1. [DD #03 – Besonderheiten beim Admin](../design-decisions/dd-01.md)
2. [DD #04 – Registrierung und Login Rückmeldung](../design-decisions/dd-02.md)
3. [DD #05 – Die Suche im Feed](../design-decisions/dd-03.md)
4. [DD #06 – Email HWR für das Login und die Registrierung](../design-decisions/dd-04.md) commit: 95c4d52334da081b8f7ecf445eab115efd5a1ada



## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
|[Login und Registrierung] Validierungs-Logik für HWR-E-Mail-Endungen und Feedback-Flashes im Registrierungsformular Login html sowie die email validation korrigiert login html erstellt für das design sowie den validator richtig gestellt mit den Endungen der hwr-mail nochmal | commit proof: https://github.com/HawaSiMoussa/webapp/commit/2e3a77d8026d431487da70e15e4a35b911275c4f , https://github.com/HawaSiMoussa/webapp/commit/cd6acdff75600d1a6c20cd2023410b069e3a2e80 , https://github.com/HawaSiMoussa/webapp/commit/c1586c7cfcba0548ea8b1e0bb9ae7e390cf6661d, https://github.com/HawaSiMoussa/webapp/commit/66872f114d3b56474d7a610cde5ba937d57d69c3 , https://github.com/HawaSiMoussa/webapp/commit/ea7dc47eadfb9ab733a6aebf46791bcff092c8c0 , https://github.com/HawaSiMoussa/webapp/commit/2ab4a2f6991ebcdf667eba4d47c4075a5aaeaa8f | ihre guide|
| [Suche] die Sucheingabe die ich im feed eingeführt habe sowie fetsgelegt dass eben auch wörter angezeigt werden die klein oder großgeschrieben wurden also nicht 100% identisch zum titel des posts | ommit prrof: https://github.com/HawaSiMoussa/webapp/commit/d4d9491f0ec9602d81516a65acaa14540ce5887f , https://github.com/HawaSiMoussa/webapp/commit/64ee9808850d5547e416bbe250c43168753376a4  | ihre Guide |
| [db migrate eingeführt] Einbau der migrate für die datenbank also isntralliert da ich davor probleme hatte | 7fc8fbc5d544b3aa0340846b3b136fba60f91b00 | hierfür habe ich ihren link im user interface unten für migrate genutzt|
| [Admin] Einen Admin entwickelt der einen überblick über alles hat und auch posts löschen kann  | https://github.com/HawaSiMoussa/webapp/commit/ed893ce385b12ea73599b876a2b504b97e9efa49 , https://github.com/HawaSiMoussa/webapp/commit/7fc8fbc5d544b3aa0340846b3b136fba60f91b00,https://github.com/HawaSiMoussa/webapp/commit/66872f114d3b56474d7a610cde5ba937d57d69c3 ,https://github.com/HawaSiMoussa/webapp/commit/e8b9bcfc8060b0e375f97df12a8c38d7d130be0e, https://github.com/HawaSiMoussa/webapp/commit/544aaf94c785cd7310c5ca3bdeb951ffbc05eb86 , https://github.com/HawaSiMoussa/webapp/commit/b00e2e74e8c1989d69b9d227c6c89c8361e3e99f,https://github.com/HawaSiMoussa/webapp/commit/3018e5f6b63703603489b7aa4a232caa946be35b  |ihre Guide |
| [Verbesserungen auch der teile meiner kommilitonen] Hier haben wir eine menge probleme verbessert und fehler behoben | https://github.com/HawaSiMoussa/webapp/commit/f01f9fa2462b00f812b3e922752fd87a24619f08 , https://github.com/HawaSiMoussa/webapp/commit/68b13c20883b3762707a0b2c5532652c12778007, https://github.com/HawaSiMoussa/webapp/commit/c0c1ae2e3e7ea66c6aec508e2607db2bd289f37f  | ihre guide und mit gemini die fehler verstanden |
| [app.py auskomentiert] Die app.py wurde komplett auskommentiert sowie nei bedarf verbessert  |  https://github.com/HawaSiMoussa/webapp/commit/00736e1676c318a62a2b72f719f99ea800198239 , https://github.com/HawaSiMoussa/webapp/commit/6c04b175d8e2fb2f17b5e7a7fe82c1551f671e45 | eigene dokumnetation und flask automatische kommentar hilfe |
| [Packages installiert für email und() und migrate]| https://github.com/HawaSiMoussa/webapp/commit/e1a7149a406a2fe4184ae6b46b5ab9a3312ed6ed|https://, https://github.com/HawaSiMoussa/webapp/commit/95c4d52334da081b8f7ecf445eab115efd5a1ada flask-migrate.readthedocs.io/en/latest/ das habe ich genutzt sowie ein email package installiert aber auch migrate installiert https://learn.microsoft.com/de-de/nuget/consume-packages/install-use-packages-visual-studio,https://github.com/HawaSiMoussa/webapp/commit/e1a7149a406a2fe4184ae6b46b5ab9a3312ed6ed |
| [Umfrage] Die Umfrage habe ich ebenfalls selber erstellt und in den uni gruppen verschickt + auswertung   |  siehe web page  |eigene umfrage erstellt|
Außerdem habe ich ebenso bei fehler behebungen meiner komilitonninen mit beigetragen wehslab ich sehr stolz bin da wir uns alle gegenseitig unterstützt haben| |
| [persona] Die Pertsona wurde ebenso von mir eigenständig erstellt.   |   | siehe read me |



## AI Directory (KI-Verzeichnis)

| # | KI-Tool | Einsatzzweck | Betroffene Bereiche commit | Anmerkungen, Vorgehensweise, Prompts |
| :-: | :--- | :--- | :--- | :--- |
| 01 | Gemini | git commit probleme beheben | beim pushen gab es oft konflikte manchmal auch da wir zu dritt gleichzeitig gearbeitet haben wehslab oft vieles nicht gepusht oder gepullt wurde | Gemini hat mir geholfen diese probleme zu lösen in dem ich z.b den merge vorgang stoppe etc. |
| 02 | Gemini | Logische Fehleranalyse (Debugging) bei Session-Abfragen | `app.py` (Route `/create_post`) | Behebung eines logischen Konflikts beim Versuch, Admin-Rechte (`is_admin`) aus dem regulären User-Filter auszuschließen . |
| 03 | Gemini | Fehleranalyse bei Datenbank-Abfragen (`scalar` vs. `scalars`) | `app.py` (Admin-Generierung beim App-Start) | Erklärung einer Fehlermeldung bezüglich Daten-Typen erhalten. Die KI diente als Hilfe, um den theoretischen Unterschied zwischen der Rückgabe eines Einzelobjekts (.scalar) und einer Liste (.scalars) zu verstehen und zu verstehen wieso der fehler kam bei der nutzung von scalars und nicht bei scalar |
| 04 | Gemini | Validierungs-Logik und Fehler-Handling | `app.py` (Routen `/register` und `/login`) | Hilfestellung beim Verständnis, wie Validierungsfehlern von Formularen denn oftmals hatte ich fehler wir z.B beim login und bei der registrierung denn vom aufbau her waren sie ähnlich aber doie regostrierung hat anfangs nicht geklappt |
| 05 | Chatgbt | bei der app.py in der stelle der Suche der fehler war die schreibweise von password und mehr schreibfehler auf die mich chatgbt hingewiesen hat   | Dokumentation  |  commit prove: e591fdf58a28dd2e01598e340a416488c14f1d63|


