l = [5,3,6,1,4,5]

def coincidirIndex(llista):
    for x,y in enumerate(llista):
        if x == y:
            print(x)

coincidirIndex(l)
    