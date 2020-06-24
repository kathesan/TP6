

class Domino :

  def __init__(self, entier_1, entier_2):

    self.entier_1 = entier_1
    self.entier_2 = entier_2

  def afficher_points(self):

    print("face a : " , self.entier_1)
    print("face a : " , self.entier_2)

  def valeur(self):

    return (self.entier_1 + self.entier_2)


class CompteBancaire :

  def __init__(self, nom="Dupont", solde=1000):

    self.nom = nom
    self.solde = solde

  def depot(self, somme):

    self.solde = self.solde + some

  def retrait(self, somme):

    self.solde = self.solde - somme

  def affiche(self):

    print("Le solde bancaire de ", self.nom , " est de : " , self.solde)


d1 = Domino(2,6)

d2 = Domino(4,3)

print("total des points " , d1.valeur() + d2.valeur())

compte1 = CompteBancaire("Duchmol", 800)
compte1.retrait(300)
compte1.affiche()
compte2 = CompteBancaire()
compte2.affiche()





