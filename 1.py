l = "Hola Aixo es una frase"

def contarLen(frase):
    lenFrase = list(map(len, frase.split()))
    print(lenFrase)
    
    lenFrase2 = [len(x) for x in frase.split()]
    print(lenFrase2)
    
contarLen(l)