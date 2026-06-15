"""

Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada.
"""

def tekst_unazad(tekst):
    if len(tekst) == 0:
        return
    tekst_unazad(tekst[1:])
    print(tekst[0], end="")
#end="" znaci da ce se taj tekst iispisati u jednom redu umjesto da se ispisuje svako slovo u novi red
#print("Tekst napisan unazad: ")
#tekst_unazad("Marko voli jabuke")
