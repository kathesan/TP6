

class Domino :

  def __init__(self, entier_1, entier_2):

    self.entier_1 = entier_1
    self.entier_2 = entier_2

  def afficher_points(self):

    print("face a : " , self.entier_1)
    print("face a : " , self.entier_2)

  def valeur(self):

    return (self.entier_1 + self.entier_2)

    


d1 = Domino(2,6)

d2 = Domino(4,3)

print("total des points : ", d1.valeur()+d2.valeur() )