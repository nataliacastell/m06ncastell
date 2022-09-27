from ast import Return


class Producte:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price

    def getGuany(self):
        return self.cost-self.price

class Beguda:
    def __init__(self, nom):
        self.nom = nom


def getDetail(self):
    return self.nom


class Refresc(Producte, Beguda):
    def __init__(self, nom, brand, alcohol, cost, price):
        self.nom = nom
        self.brand = brand
        self.alcohol = alcohol
        self.cost = cost
        self.price = price

    def getDetaill(self, text=""):
        return f"{super().getDetail()} de la marca {self.brand} te un preu de {self.cost} amb el que guanyem {super().getGuany()}          "


class Main (Refresc, Producte, Beguda):
    opc = Refresc("Coca.Cola", "Coca.cola", 1.2, 3, 2)
    x = opc.getDetaill()
    print(x)
