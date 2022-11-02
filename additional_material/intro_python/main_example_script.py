# Nella parte iniziale del file si possono importare le librerie, di sistema o esterne
import os

# Possiamo anche importare funzione definite da noi in altri file!
from my_package.my_module import eleva_al_cubo


# Nello script possiamo definire funzioni che ci sono necessarie
def eleva_al_quadrato(x):
    return x * x


# E' sempre bene identificare la porzione di codice del main, 
# cioè la parte centrale del programma, quella che viene eseguita
if __name__ == "__main__":

    files = os.listdir(".")
    print("I file e le cartelle presenti nella cartella di lavoro sono: ")
    print(files)

    quantita = len(files)
    quadrato = eleva_al_quadrato(quantita)
    print(f"Il quadrato del numero di file e cartelle è: {quadrato}")

    cubo = eleva_al_cubo(quantita)
    print(f"Il cubo del numero di file e cartelle è: {cubo}")
