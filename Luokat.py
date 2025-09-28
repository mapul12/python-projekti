class Ostos:
    def __init__(self,tuote,maara):
        self.tuote = tuote
        self.maara = maara

class Ostoslista:
    def __init__(self):
        self.lista = []

    def lisaaOstos(self):
        userinput = input("Anna ostos ja määrä (esim. Peruna 2): ").split(" ")
        ostos = Ostos(userinput[0], userinput[1])
        self.lista.append(ostos)

    def listaaOstokset(self):
        for index, line in enumerate(self.lista):
            print('[%i] %s %s'  % (index, line.tuote, line.maara))
        self.poistaOstos()

    def poistaOstos(self):
        poistoid = input("Syötä poistettavan nimikkeen id tai paina enter: ")
        self.lista.pop(int(poistoid))