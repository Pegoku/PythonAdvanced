try:
    with open('text.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("No s'ha trobat el fitxer")