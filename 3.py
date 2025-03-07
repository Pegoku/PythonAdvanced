l = ["maria", "pepe", "juan", "luis", "jose"]

def comencaPer(llista, lletra):
    print(list(filter(lambda x: x[0] == lletra, llista)))
    
comencaPer(l, "j")
