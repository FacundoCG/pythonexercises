def inversa (cadena): #Forma 1
    longitud = (len(cadena)-1)
    n_cadena = str()
    for i in range(longitud,-1,-1):
        n_cadena += cadena[i]

    return n_cadena

#inversa('facu')

def inversa2 (cadena): #Forma 2
    longitud = -(len(cadena)-1)
    n_cadena = str()
    for i in range(longitud,1):
        i = abs(i) #Abs hace positivo al numero
        n_cadena += cadena[i]

    return n_cadena

#inversa2('juan')

def inversa3 (cadena):  #Forma 3
    return cadena[::-1]

print(inversa3('Hola'))

def es_palindromo (cadena): 
    inverso = inversa(cadena)

    if inverso == cadena:
        return True

    else:
        return False

#print(es_palindromo('facu'))

def comparacion_listas(lista1,lista2):
    for i in lista1:
        if i in lista2:
            return True
        else:
            continue
    return False

#print(comparacion_listas([1,4],[2,3]))

def comparacion_listas2(lista1,lista2):
    for ele in lista1:
        for ele2 in lista2:
            if ele==ele2:
                return True
    return False

#print(comparacion_listas2([1,2,3,4],[6,7,9]))

def caractern (c, n):
    return c*n

##print(caractern('l',6))

def histograma(lista1):
    for i in lista1:
        print("*"*i)

#histograma([4,2,3])