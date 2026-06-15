"""
Definirati dvije funkcije koje kao parametar primaju ime
ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom,
a druga standardnim načinom.
Zatim definiraj treću funkciju
koja kao parametar prima naziv funkcije za ispis dobrodošlice
i poziva je tako što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije.


"""
def prva(ime): #prva obična funkcija
    return f"Pozdrav {ime}!"


lambda_naziv = lambda ime: f"Dobrodošao {ime}!" #funkcija preko lambde

def treća(imena):#treća funkcija koja prima neku od onih dviju, te ime
    moje_ime = "Laura"
    rezultat = imena(moje_ime)
    print(rezultat)


print("Dobrodošlica: ")
treća(lambda_naziv)
print("Pozdrav: ")
treća(prva)

