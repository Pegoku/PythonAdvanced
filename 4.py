l1 = ["sub","supra"]
l2 = ["campió", "campiona"]

def combinaLlistes(llista1, llista2):
    llista = list(zip(llista1, llista2))
    print([x[0] + "-" + x[1] for x in llista])

combinaLlistes(l1, l2)