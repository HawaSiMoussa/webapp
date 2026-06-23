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
|---|---|---|---|
| 1 | Erstellung der Product-Discovery-Artefakte (Scribbles, Value Proposition Canvas) | Diese Artefakte bildeten die Grundlage für die spätere Umsetzung der Anwendung. | Die Bedürfnisse der Nutzer zu identifizieren und in konkrete Funktionen zu übersetzen. |
| 2 | Entwicklung der Registrierungs- und Post-Erstellungsformulare | Diese Funktionen gehören zu den wichtigsten Bestandteilen der Plattform. | Einarbeitung in Flask-WTF, Formularvalidierung und Datenbankanbindung. |
| 3 | Gestaltung des User Interfaces mit Bootstrap und CSS | Das Design verbessert die Benutzerfreundlichkeit der Anwendung. | Bootstrap-Komponenten mit eigenem CSS zu kombinieren und ein einheitliches Layout zu erstellen. |

## Design Decisions that I led

1. [DD #00 – Zeichenlimit für Beschreibungen](../design-decisions/dd-00.md)
2. [DD #01 – Verlustdatum darf nicht in der Zukunft liegen](../design-decisions/dd-01.md)
3. [DD #02 – Eine aktive Suchanzeige pro Nutzer](../design-decisions/dd-02.md)

## Contributions

| Contribution | Proof, e.g., git commits | Sources used |
| :-- | :-- | :-- |
| Neugestaltung und Überarbeitung der Scribbles für die Anwendung | - | Vorlesungsfolien, Kursmaterial |
| Erstellung des Value Proposition Canvas | - | Value Proposition Canvas Methode |
| Eigenständiges Design des LostAndFound-Logos | - | Eigene Gestaltung |
| Entwicklung des Registrierungsformulars inklusive Validierung der Eingaben | [RegisterForm](LINK) | Flask-WTF Documentation |
| Implementierung der Funktion „Post erstellen“ inklusive Formular und Datenbankspeicherung | [AddFehlermeldung](https://github.com/HawaSiMoussa/webapp/commit/bc836f29be543f61a1f057eadec24d964b015c76) | Flask Documentation, SQLAlchemy Documentation |
| Automatisches Setzen des Meldedatums auf das aktuelle Tagesdatum | [MeldedatumAppearingAtTheFrontOfThePost](https://github.com/HawaSiMoussa/webapp/commit/5f9b4cfb9d5cdfe38954f772e774c691e72eb271), [AddMeldedatumAndVerfallsdatum](https://github.com/HawaSiMoussa/webapp/commit/199b3879823dcbb038c5ad5d57486b76fcdbf72d) | Python datetime Documentation |
| Entwicklung des Profilbereichs und Anpassungen der Benutzeroberfläche (inkl. Erstellen einer base.html) | [AddEverywhereLogo](https://github.com/HawaSiMoussa/webapp/commit/b5d2acb59c4f1972831851d0837ffc2343845ac4), [ExtendBase.html](https://github.com/HawaSiMoussa/webapp/commit/c888b907f6ad8bf9bdbbbfe116d7472316af25c2), [AddCSS](https://github.com/HawaSiMoussa/webapp/commit/cadfc6319b7cf94564039174f9182485949ab001) | Bootstrap Documentation |
| Implementierung der Info-Tooltips bei Verlustdatum und Verlustort | [AddTooltip](https://github.com/HawaSiMoussa/webapp/commit/505f62e963b8d45f8692aca1ad9e99392be14be6), [InsertSmallInfo](https://github.com/HawaSiMoussa/webapp/commit/52a7672daa7eaef1e2a0a9133f34c1a199052b1c) | Bootstrap Documentation |
| Unterstützung bei Merge-Konflikten und Wiederherstellung verlorener Codebestandteile | [FixIssues](https://github.com/HawaSiMoussa/webapp/commit/ebacfd89b19a75226b37a06d2751b92e95aede01) | - |