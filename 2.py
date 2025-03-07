from functools import reduce

l = [1,2,5,6,4]

def Pasar_a_Numero(llista):
    llista2 = reduce(lambda x,y: x*10+y, llista)
    print(llista2)

Pasar_a_Numero(l)