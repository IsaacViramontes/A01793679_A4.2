#pylint: disable=invalid-name
"""Se desabilita Pylint por requerimiento para el nombre del programa"""
import time
from tabulate import tabulate

readfile = input()
start = time.time()

with open(readfile, encoding="utf-8") as file:
    fil = file.readlines()

ListaPalabras = []

for line in fil:
    ListaPalabras.append(line[:-1])

ListaPalabras.sort()

def remover_nan(s):
    """Removes invalid data in list"""
    if not s:
        print("INVALID DATA REMOVED: ", s)
        return float("nan")
    try:
        f = str(s)
        return f
    except ValueError:
        print("INVALID DATA REMOVED: ", s)
        return float("nan")

ListaNaN = list(map(remover_nan, ListaPalabras))
ListaLimpia = ListaNaN
ListaLimpia.sort()

print("ORIGINAL TOTAL VALUES: ", len(ListaPalabras))
print("TOTAL REMOVED VALUES: ", len(ListaPalabras) - len(ListaLimpia))

CantidadPalabras = len(ListaLimpia)

contador = 0
for k in range(CantidadPalabras):
    if ListaLimpia[k] == ListaLimpia[0]:
        contador = contador + 1

PalabrasUnicas = [[ListaLimpia[0],contador]]

for a in range(CantidadPalabras):
    palabra_evaluar = ListaLimpia[a]
    CantidadPalabrasUnicas = len(PalabrasUnicas)
    for b in range(CantidadPalabrasUnicas):
        if palabra_evaluar == PalabrasUnicas[-1][0]:
            continue
        contador_frecuencia = 1
        c = a
        for c in range(CantidadPalabras):
            if palabra_evaluar == ListaLimpia[-1]:
                PalabrasUnicas.append([palabra_evaluar,contador_frecuencia])
                break
            if palabra_evaluar == ListaLimpia[a+contador_frecuencia]:
                contador_frecuencia = contador_frecuencia + 1
            else:
                PalabrasUnicas.append([palabra_evaluar,contador_frecuencia])
                break

TablaDatos = tabulate(PalabrasUnicas,headers=['PALABRA','FRECUENCIA'])
print(TablaDatos)
print('TOTAL WORDS: ', len(ListaLimpia))
print('UNIQUE WORDS: ', len(PalabrasUnicas))

with open("WordCountResults.txt", "w", encoding="utf-8") as writefile:
    L1 = ["FILE NAME: ", readfile, "\n"]
    writefile.writelines(L1)

    datos = str(TablaDatos)
    L2 = [datos, '\n']
    writefile.writelines(L2)

    totalwords = str(len(ListaLimpia))
    L3 = ["UNIQUE WORDS: ", totalwords, "\n"]
    writefile.writelines(L3)

    unique = str(len(PalabrasUnicas))
    L4 = ["UNIQUE WORDS: ", unique, "\n"]
    writefile.writelines(L4)

    end = time.time()
    timee = end - start
    tiempo = str(timee)
    L5 = ["TIME: ", tiempo, "\n"]
    writefile.writelines(L5)

    writefile.close()

print("TIME: ", end - start, " SEG")
