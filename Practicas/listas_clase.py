#Funcion buscar
def buscar_lista(lista,buscar):
    if buscar in lista:
        return "Encontrado"
    else:
        return "No encontrado"

print(buscar_lista([1,2,3], 2))    

#funcion eliminar
def eliminar_lista(lista,buscar):
    if buscar in lista:
        lista.remove(buscar)
        return "eliminado", lista
    else:
        return "no esta en la lista"
print(eliminar_lista([1,2,3], 2))    


#funcion de eliminar duplicados
def num_duplicados(lista):
    corregido = list(set(lista)) #set() elimina duplicados
    return corregido
print(num_duplicados([1,2,2,2,3,3,3,3,4]))

def num_dupl(lista):
    corregido = []
    for n in lista:
        if n not in corregido:
            corregido.append(n)
    return corregido
print(num_dupl([1,2,2,2,3,3,3,3,4]))
