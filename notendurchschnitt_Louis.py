# Notenschnitt

"""
Schreibe ein Programm, das 20 Zeugnisnoten (1.0 bis 6.0) in Zehntel-Noten
(z.B. 4.3) zufällig erzeugt.

Verwende diese 20 Noten, um damit den relevanten Durchschnitt
nach folgendem Verfahren zu berechnen:
- streiche die beste und die schlechteste Note (statistische Ausreißer),
- ermittel den Durchschnitt der verbleibenden Noten
- runde zur nächsten halben Note (1, 1.5, 2, ..., 4.5, 5, 5.5, 6).
"""
import numpy as np
from random import uniform

def runde_halbe_note(note):
    return round(note * 2) / 2

zeugnisse = 20
notensumme = 0

for _ in range(zeugnisse):
    zeugnisnote = round(uniform(1, 6), 1)
    while (zeugnisnote > 1.2 and zeugnisnote < 5.7): 
        zeugnisnote = runde_halbe_note(zeugnisnote)  # Runden auf halbe Noten
        notensumme += zeugnisnote

durchschnitt = notensumme / zeugnisse
durchschnitt_gerundet = runde_halbe_note(durchschnitt)

print(f"Durchschnitt: {durchschnitt_gerundet}")