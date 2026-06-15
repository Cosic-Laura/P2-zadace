"""
Funkciju iz prethodne zadaće učitati kao funkciju modula u novi program
i pozvati je nakon traženja unosa od korisnika.
"""

from rekurzija_zadaca import tekst_unazad

unos = input("Unesite tekst: ")



print("Rezultat unazad glasi: ", end="")
tekst_unazad(unos)

