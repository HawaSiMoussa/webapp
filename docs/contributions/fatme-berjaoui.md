---
title: Fatme Berjaoui
parent: Individual Contributions
nav_order: 1
---

## Target grade
Mein Ziel ist es, eine Note von 1,3 oder 1,7 zu erreichen. 

## Personal Goals
Während der Erstellung der Web-App möchte ich sehr viel über das Programmieren mit Python lernen, vor allem da diese Sprache neu für mich ist. Am Ende des Kurses möchte ich zu den einen sicheren Umgang mit HTML, Git, GitHub sowie Python erreichen. Das aller wichtigste ist allerdings das ich die neu erlernten Kenntnisse mit meinen bisherigen Erfahrungen verbinden möchte, um in der Zukunft noch mehr 
Projekte umsetzen zu können. 

## Eidesstattliche Erklärung

**[Fatme Berjaoui, Matrikelnr.: 77209887107]**

Ich erkläre an Eides statt:

Diese Arbeit habe ich selbständig und eigenhändig erstellt. Die den benutzten Quellen wörtlich oder inhaltlich entnommenen Stellen habe ich als solche kenntlich gemacht. Diese Erklärung gilt für jeglichen als Projektergebnis eingereichten Inhalt, einschließlich Quellcode, Texte und Illustrationen.

Mir ist bewusst, dass die wörtliche oder nahezu wörtliche Wiedergabe von fremden Inhalten - einschließlich KI-generierte Inhalte - ohne Quellenangabe als Täuschungsversuch gewertet wird und zu einer Beurteilung der Arbeit mit "nicht ausreichend" führt.

Mir ist weiterhin bewusst, dass ich, sofern ich zur Erstellung dieser Arbeit KI-basierte Hilfsmittel verwendet habe, die Verantwortung für eventuell durch die KI generierte fehlerhafte oder verzerrte Inhalte, fehlerhafte Referenzen, Verstöße gegen das Datenschutz- und Urheberrecht oder Plagiate trage.

## Top-3 Contributions

| # | My contribution | Why I am proud of it | Which challenge I overcame |
| :-- | :-- | :-- | :-- |
| 1 | Unterstützung bei der Product Discovery (Scribbles, Value Proposition Canvas) | Ich bin stolz darauf, weil diese Ideen und Entwürfe die Grundlage für unsere spätere Web-App geschaffen haben. | So realistsich, wie möglich bleiben und größtenteils aus Sicht des Users agieren. |
| 2 | Entwicklung der Registrierungs- und Post-Erstellungsformulare | Diese Funktionen sind ein zentraler Bestandteil unserer Anwendung und werden von jedem Nutzer verwendet. | Ich musste mich zuerst in Flask-WTF, Validatoren und die Verbindung zur Datenbank einarbeiten. |
| 3 | Gestaltung des User Interfaces mit Bootstrap und CSS | Mir war wichtig, dass die Anwendung übersichtlich aussieht und einfach zu bedienen ist. | Die einzelnen Styles heraussuchen |

## Design Decisions that I led

1. [DD #00 – Zeichenlimit für Beschreibungen](../design-decisions/dd-00.md)
2. [DD #01 – Verlustdatum darf nicht in der Zukunft liegen](../design-decisions/dd-01.md)
3. [DD #02 – Eine aktive Suchanzeige pro Nutzer](../design-decisions/dd-02.md)

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Neugestaltung und Überarbeitung der Scribbles für die Anwendung | - | Vorlesungsfolien zu Product Discovery und UI-Konzeption |
| Erstellung der Web-Page| [AddDD](https://github.com/HawaSiMoussa/webapp/commit/452ff44db46f22873e7009220a58023effcd0f4f), [ProductDiscovery](https://github.com/HawaSiMoussa/webapp/commit/d4dd662b9d7ae156d4d30cb67298ac2ae560829d)| - |
| Erstellung des Value Proposition Canvas | - | Value Proposition Canvas Methode, Vorlesungsfolien Product Discovery |
| Eigenständiges Design des LostAndFound-Logos | - | Eigene Gestaltung |
| Entwicklung des Registrierungsformulars (inkl. contact.html) | [KlasseContactForm](https://github.com/HawaSiMoussa/webapp/commit/b1b0bc4d31e365eda89225e9eda09a9ab82c1037), [App.route](https://github.com/HawaSiMoussa/webapp/commit/5fd428cb25c31330c3c0487f313936fec8568c41) | Flask-WTF Documentation, WTForms Documentation, Vorlesungsunterlagen zu HTML Forms |
| Implementierung der Funktion „Post erstellen“ mit Datenbankspeicherung (inkl. create_post.html) | [AddCreatePostHtml](https://github.com/HawaSiMoussa/webapp/commit/0e88b051bef0b53955151903648149e9346474c4), [ConnectApp.pyWithDatabase](https://github.com/HawaSiMoussa/webapp/commit/59e6a8dd89f93e1256455cd4469e8aa3449d1def) | Flask Documentation, SQLAlchemy Documentation, Vorlesungsunterlagen zu Flask Routing und Datenbanken |
| Automatisches Setzen des Meldedatums auf das aktuelle Tagesdatum |   [MeldedatumAppearingAtTheFrontOfThePost](https://github.com/HawaSiMoussa/webapp/commit/5f9b4cfb9d5cdfe38954f772e774c691e72eb271), [AddMeldedatumAndVerfallsdatum](https://github.com/HawaSiMoussa/webapp/commit/199b3879823dcbb038c5ad5d57486b76fcdbf72d) | Python datetime Documentation, Python Grundlagen (Funktionen und Datumsverarbeitung) |
| Entwicklung des Profilbereichs und Anpassungen der Benutzeroberfläche (inkl. Erstellen einer base.html) | [AddEverywhereLogo](https://github.com/HawaSiMoussa/webapp/commit/b5d2acb59c4f1972831851d0837ffc2343845ac4), [ExtendBase.html](https://github.com/HawaSiMoussa/webapp/commit/c888b907f6ad8bf9bdbbbfe116d7472316af25c2), [AddCSS](https://github.com/HawaSiMoussa/webapp/commit/cadfc6319b7cf94564039174f9182485949ab001), [base.html](https://github.com/HawaSiMoussa/webapp/commit/5115fad4054ee64360137aac6a5e25acea3d693d) | Bootstrap Documentation, HTML & CSS Vorlesungsunterlagen, Template-Vererbung mit Jinja2 |
| Implementierung der Info-Tooltips bei Verlustdatum und Verlustort | [AddTooltip](https://github.com/HawaSiMoussa/webapp/commit/505f62e963b8d45f8692aca1ad9e99392be14be6),  [InsertSmallInfo](https://github.com/HawaSiMoussa/webapp/commit/52a7672daa7eaef1e2a0a9133f34c1a199052b1c) | Bootstrap Documentation, HTML Attribute und Benutzerführung (Usability) |
| Zuständig für forms.py | [CreateForms.py](https://github.com/HawaSiMoussa/webapp/commit/140eb154cc82d669c668b2ac7ce85e10923f9d8a), [InsertInApp.py](https://github.com/HawaSiMoussa/webapp/commit/c756626909e05db8bb1a2d1bd8783843eb4c511a) | Bootstrap Documentation, HTML & CSS Vorlesungsunterlagen, Template-Vererbung mit Jinja2 |
| Unterstützung bei Merge-Konflikten und Wiederherstellung verlorener Codebestandteile |  [FixIssues](https://github.com/HawaSiMoussa/webapp/commit/ebacfd89b19a75226b37a06d2751b92e95aede01), [FixIssues3](https://github.com/HawaSiMoussa/webapp/commit/dffb2bc26a2aba338fcf3dcf6755c1119e8cefdd) | - |

## AI Directory
| # | AI Tool | Purpose of Use | Affected Sections (Code + Docs) | Remarks, Procedure, Prompts |
| :-- | :-- | :-- | :-- | :-- |
| 01 | ChatGPT | Verständnis von Hawas Code, da mein Kontaktformular mit ihrem Code verknüpft war | `contact.html`, `forms.py`, `app.py` | "Erklär mir diesen Code einfach und verständlich für dumme", ich habe hier Hawas user-id gebraucht und musste daher verstehen wie diese eingebettet wurde |
| 02 | ChatGPT | Unterstützung bei Git- und GitHub-Problemen (Es kam mehrfach vor, dass unsere SQLite-Datei mit unseren Posts nach Commits leer war) | Git Repository | Hier wurde einfach ein Screenshot geschickt von den Fehlern ohne weiteren Text |
| 03 | ChatGPT | Unterstützung bei der Erstellung und Strukturierung der `base.html` | `base.html`, HTML-Templates | Half die Grundlagen der Template-Vererbung in Jinja2 zu verstehen |
| 04 | ChatGPT | Unterstützung bei der Auswahl einer passenden Farbpalette | `style.css`, `color.css` | Ich hatte eine spezifische Vision für die Farben, damit diese miteinander harmonisieren und hab dann nur nach der Nummer dieser Farbe gefragt|