---
title: DD-09
parent: Design Decisions
---

{: .no_toc }
# DD-09: Views eines Posts tracken

## Meta

Status
:  Implementiert

Updated
: 20.07.2026

## Problem Statement

 Gerade bei Fundsachen können die Views für einen Post-Owner relevant sein: Ein Nutzer, dessen Post viele Aufrufe hat, aber trotzdem keine Rückmeldung bekommt, weiß zumindest, dass die Anzeige sichtbar war.
 Bleibt die Aufrufzahl dagegen niedrig, könnte das ein Hinweis sein, den Post zu überarbeiten (z. B. Titel oder Beschreibung anpassen) oder den Verlustort/Ablaufzeitraum zu prüfen. Ohne diese Rückmeldung bleibt für den Nutzer unklar, ob sein Beitrag überhaupt Reichweite hat.

## Decision

Die Funktion wurde  umgesetzt:  Jeder Post hat ein `views`-Feld, das bei jedem Aufruf der Detailseite eines Posts um 1 erhöht wird.


## Regarded Options

## Option 1: View-Counter pro Beitrag

*Vorteil:*
- Mehr Feedback für Nutzer
- Höhere Transparenz über die Reichweite eines Beitrags

*Nachteil:*
- Zusätzliche Datenbanklogik notwendig
- Zusätzlicher Aufwand für Tracking und Speicherung
- Weiterleitung auf eine extra Website für die Post-Detail--> User verlässt den Feed (notwendig für Logik um die views zu zählen)

## Option 2: Keine View-Anzeige: Details per Togglebar anzeigen (gewählt)

Vorteil:
- Weniger Aufwand
- Fokus auf Kernfunktionen
- Statt, dass man auf eine Postdeatils Seite weitergeleitet wird kann man (wie ursprünglich) per togglebar die details auf- und zuklappen

## Reasoning
Ursprünglich aus Zeitgründen zunächst nicht priorisiert. Im weiteren Verlauf wurde die Funktion doch umgesetzt, da davon ausgegangen wurde, dass Nutzer grundsätzlich neugierig sind, wie oft ihr eigener Beitrag bereits angesehen wurde: Ähnlich wie bei Aufrufzahlen in anderen bekannten Plattformen (z. B. Kleinanzeigen-Apps, Vinted).
Die Umsetzung erforderte eine eigene Detailseite pro Post (`post_detail`), da der bisherige Collapse-Mechanismus (Auf-/Zuklappen ohne Server-Request) es technisch nicht ermöglicht hätte, einen Seitenaufruf serverseitig zu zählen.