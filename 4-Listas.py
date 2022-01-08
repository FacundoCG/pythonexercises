milista=['A','B','C']

print(milista[:])

print(milista[2])

print(milista[-3])

print(milista[0:2])

print(milista[:2])

print(milista[1:])

milista.append('D') #Agrega el elemento al final

milista.insert(0, 'Z') #Yo elijo donde agregar al elemento

milista.extend(['E','F','G']) #Agrego varios elementos a la lista

milista

print(milista.index('F')) #Me da el indice del elemento que busco

print('J' in milista) #La función in nos dice si el elemento se encuentra en la lista.

milista.remove('Z') #Eliminar elementos

milista.pop() #Elimina el último elemento de la lista

print(milista[:]) 

lista1=['FACU','YO', 5]
lista2=['TÚ', 3]

lista3=lista1 + lista2 #Se concatenan las listas
print(lista3[:])
#----------------------------------------------------------------------------

lista3=lista3*3 #El asterico repite la lista.
print(lista3[:])
#----------------------------------------------------------------------------

lista4 = [lista1, lista2, lista3] #Anido las listas
print(lista4[:])
print(lista4[1])

#----------------------------------------------------------------------------
lis = [3,11,9,7,5]
lis.sort() #Con la función sort se ordena los elementos de una lista
print(lis) 