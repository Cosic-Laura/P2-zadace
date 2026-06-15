"""
Potrebno napisati regex koji vraca podudaranje ukoliko se unese string
koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo prezimena.
String mora sadržavati bar jedan broj između 0 i 5 i razmak.

"""
import re

regex = r"^([lL].*[0-5].*\s.*[ćĆ])$"

unos = input("unesite ime i prezime, uključujući neki broj i razmak: ")

result = re.search(regex,unos)
if result:
    print("Podudaranje pronađeno!")
else:
    print("Nema podudaranja.")
