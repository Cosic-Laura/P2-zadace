"""Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.

Istražiti greedy i non-greedy quantifiers.
"""


import re

rezultat = None

regex1 = r"^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$" #^[a-z]+  - ova strelica znači da tekst počinje sa ___, + označava više slova, da nije samo jedno od slova unutar te [].


#\. - kosa crta označava da se doslovno misli na znak neki \x, da poslije nečega mora pisati x , ____x____

#@fpmoz\.sum\.ba$ - stavimo izvan [] zagrada, jer se one odnose na "jedno od ovih slova..", a ovako označavamo nešto što mora stajati tu.


while not rezultat:
    txt = input("Unesi e-mail:")

    rezultat = re.search(regex1,txt)
print("Uspješno ste unijeli e-mail: ",rezultat.group())


rezultat2 = None

regex2 = r"^[a-z]+\.[a-z]+\d*@sum\.ba$"

while not rezultat2:
    eduid = input("Unesite eduid:")

    rezultat2 = re.search(regex2,eduid)
print("Uspješno ste unijeli eduid: ",rezultat2.group())
