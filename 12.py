import os

llistaClasse = ["OSCAR BORRAS RIUTORT","MARC CALDAS GARRIDO","JAUME CARDONA ANDREU","IKER JAVIER DELICADO RUS","JUAN PABLO FUENTES DE VERA","ENEKO GOMEZ DIAZ","PAU GOMILA BARBER","IKER HERNANDEZ GARCIA","IVAN HORDIEIEV","ARIS KRYSAK TOMAS","BRAIS JORDAN MANENT MIRANDA","ANTONIO MARTINEZ MARTINEZ","JORDI MELIÁ CARRERAS","ALEJANDRA MOYA ZAMORA","IVAN MUÑOZ LEÓN","LUCAS PERELLÓ BAGUR","ADRIAN PEREZ CALDERON","YAGO PONS GARCIA BOENTE","DAVID SÁNCHEZ CABANILLAS","GUSTAVO TECCHIO NEIVA","BRUNO AIMÉ VACA MENDOZA","ALEJANDRO VALLECILLO VACA","SAAD ZAIDI ZAID"]
llistaProfe = ["JOSE ANTONIO DOMINGUEZ", "CLARA MARTIN", "PEP MALLE", "CARLOS MORENO", "DAVID LABIANO", "JOAN CARRERAS"]
fileContents = []
try:
    os.mkdir("/home/cicles/AO/Prova")
except:
    pass
os.chdir("/home/cicles/AO/Prova")
with open("Ex12.txt", "w") as file:
    for name in llistaClasse:
        file.write(name + "\n")
    file.close()
with open("Ex12.txt", "a") as file:
    for name in llistaProfe:
        file.write(name + "\n")
    file.close()

with open("Ex12.txt", "r") as file:
    # print(file.read())
    for i in file.readlines():
        fileContents.append(i.strip())
    file.close()
print(fileContents)
