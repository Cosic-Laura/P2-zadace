"""Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.

Napraviti novi rječnik gdje će se po bodovnom rangu
upisivati broj ostvarenih ocjena. 

Nedovoljan
0-49%

Dovoljan
50-65%

Dobar
65-80%

Vrlodobar
80-90%

Izvrstan
90-100%
"""



studenti = [
    ("Ana", "Horvat", 78),
    ("Ivan", "Kovačić", 45),
    ("Marija", "Babić", 92),
    ("Petar", "Zovko", 65),
    ("Lucija", "Marić", 84)
]

ocjene = {
    "Nedovoljan": 0,
    "Dovoljan": 0,
    "Dobar": 0,
    "Vrlo dobar": 0,
    "Izvrstan": 0
}

sortirano = []

for ime,prezime,bodovi in studenti:
    if bodovi < 50:
        ocjene["Nedovoljan"] += 1
        ocjena = "Nedovoljan"
    elif bodovi < 65:
        ocjene["Dovoljan"] += 1
        ocjena = "Dovoljan"
    elif bodovi < 80:
        ocjene["Dobar"] += 1
        ocjena = "Dobar"
    elif bodovi < 90:
        ocjene["Vrlo dobar"] += 1
        ocjena = "Vrlo dobar"
    else:
        ocjene["Izvrstan"] += 1
        ocjena = "Izvrstan"
    sortirano.append((prezime,ime,bodovi,ocjena))
print("Rjecnik s ocjenama",ocjene)



print("Sortirano po prezimenima: ",sortirano)
