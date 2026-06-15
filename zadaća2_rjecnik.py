"""Koristeći listu imena iz prethodnog zadatka
svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)
"""

import random

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen", "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana", "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip", "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko", "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

ocjene = [] #spremljene sve ocjene u ovoj listi

rezultat = {} #prazan rjecnik

for ime in imena: #s ovom for petljom prolazimo kroz svako ime u "imena"
    ocjena = random.randint(1,5)
    ocjene.append(ocjena)
    rezultat[ime] = ocjena #kad stavimo rjecnik[ono for "" in ""], prolazimo kroz svako ime
                            #u ovom slucaju i uz njega dodajemo neku vrijednost

jedinice = 0 #za svaku ocjenu pravimo tkz. brojac gdje ce se spremit broj ocjene
dvojke = 0
trojke = 0
cetvorke = 0
petice = 0

for broj in ocjene: #petljom cemo proci kroz listu u kojem su spremljene ocjene
                    #svaki put kad petlja pronaðe ocjenu dodat ce se +1 u brojac za pronaðenu ocjenu.
    if broj == 1:
        jedinice += 1
    elif broj == 2:
        dvojke += 1
    elif broj == 3:
        trojke += 1
    elif broj == 4:
        cetvorke += 1
    elif broj == 5:
        petice += 1

        #pravimo rjecnik jer je trazeno u zadatku, gdje ce biti spremljen broj ocjena
broj_ocjena = {
    1: jedinice,
    2: dvojke,
    3: trojke,
    4: cetvorke,
    5: petice
}
#racunamo prolaznost, zbroj prolaznih ocjena podijelimo s ukupnim brojem ocjena
prolazne_ocjene = dvojke + trojke + cetvorke + petice
ukupno = len(ocjene)
postotak = prolazne_ocjene/ukupno
print("Studenti imaju ocjene: ",rezultat)
print("Broj svake te ocjene je: ",broj_ocjena)
print("Postotak prolaznosti je: ",postotak * 100,"%") #da bi dobili posto od nekog broja koji je decimalan mnozimo s 100 i onda pod stringom stavimo pored znak postotka %
