
'''
Ostoslista -ohjelmisto

käyttäjä syöttää ostettavia asioita ja niiden määriä
määrittelyn jälkeen, käyttäjä voi poistaa ostoslistalta ostettuja asioita, esim indeksin perusteella
ostoslistan rivit ovat olioita
ohjelmisto toimii käyttäjänsyötteen perusteella
listan ollessa tyhjä, ohjelma palaa ensimmäiseen vaiheeseen, jossa käyttäjä voi kirjoittaa mitä ostaa ja kuinka poaljob
Luokkien eriyttäminen omaan tiedostoon.

'''

from Luokat import Ostoslista

ostokset = Ostoslista()

userinput = ""
while userinput != "lopeta":
    print("(1) Lisää tuote\n(2) Listaa tuotteet\n(3) Lopeta")
    userinput = input("Komento:")
    if(userinput == "1"):
        ostokset.lisaaOstos()
    elif(userinput == "2"):
        ostokset.listaaOstokset()
    elif(userinput == "3"):
        exit()


