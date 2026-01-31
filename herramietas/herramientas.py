def largo_strings(dicc_strings: dict) -> list:
    lista_largos = []
    for string in dicc_strings:
        lista_largos.append(len(string))
    return lista_largos

def alargar_string(string: str, cant: int):
    if cant <= 0:
        return string
    else:
        for i in range(cant):
            string += "_"
        return string

def alargar_strings(strings, largo: int):
    strings_igualados = []
    for string in strings:
        if len(string) <= largo:
            cant = largo - len(string)
            nuevo_string = alargar_string(string, cant)
            strings_igualados.append(nuevo_string)
    return strings_igualados

def max_strings_matriz(matriz):
    max_largo_matriz = 0
    for fila in matriz:
        if max(largo_strings(fila)) > max_largo_matriz:
            max_largo_matriz = max(largo_strings(fila))
    return max_largo_matriz

def igualar_strings_matriz(matriz):
    max_largo_matriz = max_strings_matriz(matriz)
    for fila in matriz:
        matriz[matriz.index(fila)] = alargar_strings(fila, max_largo_matriz)
    return matriz


#matriz_strings = [["hola", "holaa", "holaaa", "holaaaa", "hola"], 
#                  ["hol", "ha", "holaaa", "holaaaa", "hola"], 
#                  ["hoa", "holaa", "holaaa", "hola", "holaaaaaaa"], 
#                  ["hla", "a", "holaaa", "holaaaa", "hola"]]


#for fila in matriz_strings:
#    print(largo_strings(fila))

#print(max_strings_matriz(matriz_strings))

#for fila in igualar_strings_matriz(matriz_strings):
#    print(fila)