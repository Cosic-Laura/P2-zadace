"""
Napraviti generator funkcije za ispis
svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.

"""

def parni(par):
    brojac = 0
    while brojac < par:
        if brojac % 2 == 0:
            yield brojac
        brojac += 1

def neparni(par):
    brojac = 0
    while brojac < par:
        if brojac % 2 != 0:
            yield brojac
        brojac += 1

generator_parni = parni(10)
generator_neparni = neparni(10)

for broj in generator_neparni:
    print("Neparni brojevi: ",broj)

print("Parni broj: ",next(generator_parni))
print("Parni broj: ",next(generator_parni))
print("Parni broj: ",next(generator_parni))
print("Parni broj: ",next(generator_parni))
print("Parni broj: ",next(generator_parni))
