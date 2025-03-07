l = ["casa", "cotxe", "teclat", "ordinador"]
def diccionariClaus(llista):
    dicc = {}
    for x,y in enumerate(llista):
        dicc[y] = x
    print(dicc)    
    
diccionariClaus(l)