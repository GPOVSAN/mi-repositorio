# ingreso = input("ingrese palabras")

# def totalElementos(ingreso) :

#     count = 0
#     for element in ingreso:
#         count += 1
#     return count

# print("The total number of elements in the list: ", totalElementos(ingreso))

# listaPalabras = ingreso.split()

# frecuenciaPalab = []
# for i in listaPalabras:
#     frecuenciaPalab.append(listaPalabras.count(i))

# print("Cadena\n" + ingreso +"\n")
# print("Lista\n" + str(listaPalabras) + "\n")

# print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))


#ingreso = "barco casa barco perro lote lote perro perro naranja tomate "


ingreso = input("Ingrese la palabra: ")
listaPalabras = ingreso.split()

contador_a = {i: listaPalabras.count(i) for i in listaPalabras}
new_list = list(contador_a.items())

contador_b = []
for y in new_list:
    contador_b.append(y[1])
    
print(len(listaPalabras) ,"\n", *contador_b, sep= " ")