#pylint: disable=invalid-name
"""Se desabilita Pylint por requerimiento para el nombre del programa"""
import time
import math
from tabulate import tabulate

readfile = input()
start = time.time()
with open(readfile, encoding="utf-8") as file:
    fil = file.readlines()

ListaValores = []

for line in fil:
    ListaValores.append(line[:-1])

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

print("ORIGINAL TOTAL VALUES: ", len(ListaValores))
print("TOTAL REMOVED VALUES: ", len(ListaValores) - len(ListaLimpia))

filas = len(ListaLimpia)
columnas = 3
matrix = [[0] * columnas for _ in range(filas)]

def bin2dec(n):
    """Metodo para volver de binario a decimal"""
    num = n
    dec_value = 0

    base = 1
    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value

def dec2bin(number: int):
    """Metodo para volver de decimal a binario"""
    ans = ""
    negativo = False
    if number == 0:
        return 0
    if number < 0:
        number = abs(number)
        negativo = True
    while number:
        ans += str(number&1)
        number = number >> 1

    ans = ans[::-1]
    if negativo is True:
        contador = len(ans)
        mascara = '111111111111'
        mask = list(mascara)
        for k in range(contador):
            offset = 12 - contador + k
            if ans[k] == '1':
                mask[offset] = '0'
            if ans[k] == '0':
                mask[offset] = '1'

        mascara = "".join(mask)
        binario = int(mascara)
        decimal = bin2dec(binario) + 1
        newBin = dec2bin(decimal)
        negativo = False
        ans = newBin
    return ans

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def dec2hex(decimal):
    """Metodo para volver de decimal a hexadecimal"""
    hexadecimal = ''
    if decimal == 0:
        return 0
    if decimal < 0:
        decimal = abs(decimal)
        decimal = 4294967296 - decimal
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

for a in range(filas):
    deci = ListaLimpia[a]
    matrix[a][0] = deci
    tobinary = dec2bin(deci)
    matrix[a][1] = tobinary
    tohexa = dec2hex(deci)
    matrix[a][2] = tohexa

TablaDatos = tabulate(matrix,headers=['DECIMAL','BINARY','HEXADECIMAL'])
print(TablaDatos)

with open("ConversionResults.txt", "w", encoding="utf-8") as writefile:
    L1 = ["FILE NAME: ", readfile, "\n"]
    writefile.writelines(L1)

    datos = str(TablaDatos)
    L6 = [datos, '\n']
    writefile.writelines(L6)

    end = time.time()
    timee = end - start
    tiempo = str(timee)
    L7 = ["TIME: ", tiempo, "\n"]
    writefile.writelines(L7)

    writefile.close()

print("TIME: ", end - start, " SEG")
