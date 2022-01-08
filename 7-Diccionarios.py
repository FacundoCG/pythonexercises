diccionariopaises={"Argentina":"Buenos Aires","Brasil":"Brasilia", "Uruguay":"Montevideo"}
diccionariopaises['Argentina']
#----------------------------------------------------------------------------

diccionariopaises["China"]="Beijing"
print(diccionariopaises)
#----------------------------------------------------------------------------

diccionariopaises["China"]="Hong Kong" #Cambio el valor
#----------------------------------------------------------------------------

del diccionariopaises['Brasil'] #Borro la clave junto a su valor
#----------------------------------------------------------------------------

lista=['Facu','Juan','José']
diccionarion = {lista[0]:'Yo', lista[1]:'amigo', lista[2]:'pariente'} #Incorporo elementos de una lista al diccionario
print(diccionarion)
#----------------------------------------------------------------------------

print(diccionarion['Juan'])
#----------------------------------------------------------------------------

dict = {'hola':'chau', 1:'yo', 'numeros': [1,2,3,4,5]} #Incorporo una lista al diccionario
dict['numeros']
#----------------------------------------------------------------------------

dictionary = {'nose':'chau', 'y':5, 'dictionario':{'fue':1}} #Un diccionario adentro de otro
dictionary['dictionario']
#----------------------------------------------------------------------------

dictionary.keys() #Imprime las claves
#----------------------------------------------------------------------------

dictionary.values() #Imprime los valores de las claves
#----------------------------------------------------------------------------

len(dictionary) #Imprime el numero de parejas que componen al diccionario
#----------------------------------------------------------------------------

dic = {} 
n = int(input('Longitud del diccionario'))

for i in range(n):
    l = input('Digite un valor para el diccionario')
    dic[i] = l

print(dic)

dic.pop() #Borro el último elemento