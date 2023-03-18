def sorozatszamitas(lista, kezdoertek, fv):
    eredmeny = kezdoertek
    for elem in lista:
        eredmeny = fv(eredmeny, elem)
    return eredmeny


def eldontes(lista, feltetel):
    for elem in lista:
        if feltetel(elem):
            return True
    return False


def kivalasztas(lista, feltetel):
    for elem in lista:
        if feltetel(elem):
            return elem
    return None


def linearis_kereses(lista, keresett_elem):
    for i in range(len(lista)):
        if lista[i] == keresett_elem:
            return i
    return -1


def megszamolas(lista, feltetel):
    szamlalo = 0
    for elem in lista:
        if feltetel(elem):
            szamlalo += 1
    return szamlalo


def maximumkivalasztas(lista):
    max_index = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[max_index]:
            max_index = i
    return max_index


def minimumkivalasztas(lista):
    min_index = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[min_index]:
            min_index = i
    return min_index
