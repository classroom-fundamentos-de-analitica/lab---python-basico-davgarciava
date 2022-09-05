"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def pregunta_01():
    sum=0
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            sum+= int(row[1])
    return sum


def pregunta_02():
    columna = []
    letras=[]
    apariciones = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
                columna.append(row[0])
                if(not row[0] in letras):
                    letras.append(row[0])
    letras.sort()
    for letra in letras:
        apariciones.append((letra, columna.count(letra)))

    return apariciones

def pregunta_03():
    letras=[]
    conteo = []
    suma=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not row[0] in letras):
                letras.append(row[0])
                conteo.append(int(row[1]))
            else:
                conteo[letras.index(row[0])]+=int(row[1])
    for letra in letras:
        suma.append((letra,conteo[letras.index(letra)]))
    suma.sort(reverse=False)
    return suma

def pregunta_04():
    
    meses=[]
    columna = []
    apariciones = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            mes = row[2].split("-")[1]
            columna.append(mes)
            if(not mes in meses):
                meses.append(mes)
    meses.sort()
    for mes in meses:
        apariciones.append((mes, columna.count(mes)))
    return apariciones

def pregunta_05():
    letras=[]
    colMax = []
    colMin = []
    maximos = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not row[0] in letras):
                letras.append(row[0])
                colMax.append(int(row[1]))
                colMin.append(int(row[1]))
            else:
                if(colMax[letras.index(row[0])]<int(row[1])):
                    colMax[letras.index(row[0])]=int(row[1])
                if(colMin[letras.index(row[0])]>int(row[1])):
                    colMin[letras.index(row[0])]=int(row[1])
    for letra in letras:
        maximos.append((letra,colMax[letras.index(letra)],colMin[letras.index(letra)]))
    maximos.sort(reverse=False)
    return maximos

def pregunta_06():
    letras=[]
    colMax = []
    colMin = []
    dic = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for cod in row[4].split(','):
                letra = cod.split(':')[0]
                codigo = cod.split(':')[1]
                if(not letra in letras):
                    letras.append(letra)
                    colMax.append(int(codigo))
                    colMin.append(int(codigo))
                else:
                    if(colMax[letras.index(letra)]<int(codigo)):
                        colMax[letras.index(letra)]=int(codigo)
                    if(colMin[letras.index(letra)]>int(codigo)):
                        colMin[letras.index(letra)]=int(codigo)
    for letra in letras:
        dic.append((letra,colMin[letras.index(letra)],colMax[letras.index(letra)]))
    dic.sort(reverse=False)
    return dic

def pregunta_07():

    numeros = []
    letras = []
    reg = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in numeros):
                numeros.append(int(row[1]))
                letras.append([row[0]])
            else:
                letras[numeros.index(int(row[1]))].append(row[0])
    for numero in numeros:
        reg.append((numero,letras[numeros.index(numero)]))
    reg.sort(reverse=False)
    return reg

def pregunta_08():
    numeros = []
    letras = []
    reg = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            if(not int(row[1]) in numeros):
                numeros.append(int(row[1]))
                letras.append([row[0]])
            else:
                if(not row[0] in letras[numeros.index(int(row[1]))]):
                    letras[numeros.index(int(row[1]))].append(row[0])

    for numero in numeros:
        order = letras[numeros.index(numero)]
        order.sort()
        reg.append((numero,order))
    reg.sort(reverse=False)
    return reg

def pregunta_09():
    columna = []
    letras = []
    dictionarie = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for cod in row[4].split(','):
                letra = cod.split(':')[0]
                columna.append(letra)
                if( not letra in letras):
                    letras.append(letra)
    letras.sort()
    for letra in letras:
        dictionarie.update({letra: columna.count(letra)})
    return dictionarie

def pregunta_10():
    letras=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            col4 = row[3].split(",")
            col4 = len(col4)
            col5 = row[4].split(",")
            col5 = len(col5)
            letras.append((row[0], col4, col5))
    return letras
print(pregunta_10())

def pregunta_11():
    letras={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for letra in row[3].split(","):
                if(not letra in letras.keys()):
                    letras.update({letra: int(row[1])})
                else:
                    letras[letra] += int(row[1])
    dicc = sorted(letras.items())
    return dict(dicc)


def pregunta_12():
    letras={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            letra=row[0]
            for codigo in row[4].split(","):
                numero = int(codigo.split(":")[1])
                if(not letra in letras.keys()):
                    letras.update({letra: numero})
                else:
                    letras[letra] += numero
    dicc = sorted(letras.items())
    return dict(dicc)
print(pregunta_12())
