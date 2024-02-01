#pylint: disable=invalid-name
"""Se desabilita Pylint por requerimiento para el nombre del programa"""
import time
import math

readfile = input()
start = time.time()
with open(readfile, encoding="utf-8") as file:
    fil = file.readlines()

ListaValores = []
SUMA_TOTAL = 0

for line in fil:
    ListaValores.append(line[:-1])

ListaValores.sort()

def remover_strings(s):
    """Removes invalid data in list"""
    if not s:
        print("INVALID DATA REMOVED: ", s)
        return float("nan")
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        print("INVALID DATA REMOVED: ", s)
        return float("nan")

ListaSinStrings = list(map(remover_strings, ListaValores))
ListaLimpia = [n for n in ListaSinStrings if math.isnan(n) is not True]

ListaLimpia.sort()

print("ORIGINAL TOTAL VALUES: ", len(ListaValores))
print("TOTAL REMOVED VALUES: ", len(ListaValores) - len(ListaLimpia))


CantidadValores = len(ListaLimpia)
for v in range(CantidadValores):
    SUMA_TOTAL = SUMA_TOTAL + ListaLimpia[v]

mean = SUMA_TOTAL/CantidadValores

MEDIAN = 0
num = (CantidadValores/2) - 1

if CantidadValores % 2 == 0:
    num = int(num)
    num1 = ListaLimpia[num]
    num2 = ListaLimpia[num+1]
    MEDIAN = (num1 + num2) / 2
else:
    num3 = int(num+0.5)
    MEDIAN = ListaLimpia[num3]

def moda(array):
    """Deteccion de moda en la lista"""
    most = max(map(array.count, array)) if array else None
    mset = set(filter(lambda x: array.count(x) == most, array))
    return mset if set(array) - mset else "NO MODE"

mode = moda(ListaLimpia)

std = (sum((x-mean)**2 for x in ListaLimpia) / CantidadValores)**0.5

var = sum((xi - mean) ** 2 for xi in ListaLimpia) / CantidadValores


print("COUNT: ", CantidadValores)
print("MEAN: ", mean)
print("MEDIAN: ", MEDIAN)
print("MODE: ", mode)
print("SD: ", std)
print("VAR: ", var)

with open("StatisticsResults.txt", "w", encoding="utf-8") as writefile:
    L1 = ["FILE NAME: ", readfile, "\n"]
    writefile.writelines(L1)

    original = str(len(ListaValores))
    L2 = ["ORIGINAL TOTAL VALUES: ", original, "\n"]
    writefile.writelines(L2)

    conteo = str(CantidadValores)
    L3 = ["COUNT: ", conteo, "\n"]
    writefile.writelines(L3)

    promedio = str(mean)
    L4 = ["MEAN: ", promedio, "\n"]
    writefile.writelines(L4)

    mediana = str(MEDIAN)
    L5 = ["MEDIAN: ", mediana, "\n"]
    writefile.writelines(L5)

    modas = str(mode)
    L6 = ["MODE: ", modas, "\n"]
    writefile.writelines(L6)

    desviacion = str(std)
    L7 = ["SD: ", desviacion, "\n"]
    writefile.writelines(L7)

    variacion = str(var)
    L8 = ["VAR: ", variacion, "\n"]
    writefile.writelines(L8)

    end = time.time()
    timee = end - start
    tiempo = str(timee)
    L7 = ["TIME: ", tiempo, "\n"]
    writefile.writelines(L7)

    writefile.close()

print("TIME: ", end - start, " SEG")
