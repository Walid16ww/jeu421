import random

class De:
    def __init__(self):
        self.valeur = None
        
    def lancer(self):
        self.valeur = random.randint(1,6)
    
    def __str__(self):
        return str(self.valeur)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.des = [De(), De(), De()]
        self.points = 0
        
    def jouer(self):
        for de in self.des:
            de.lancer()
            
    def afficher_des(self):
        return (self.nom, "a lancé :", ", ".join(str(de) for de in self.des))
        
    def compter_points(self):
        self.points = 0
        for de in self.des:
            if de.valeur == 4 and de.valeur ==2 and de.valeur == 1:
                self.points += -10
            elif de.valeur == 1 and de.valeur == 1:
                self.points += 7
            elif (de.valeur == 1 and de.valeur == 1 and de.valeur == 6) or ( de.valeur == 6 and de.valeur == 6 and de.valeur == 6):
                self.points += 6
            elif (de.valeur == 1 and de.valeur == 1 and de.valeur == 5) or ( de.valeur == 5 and de.valeur == 5 and de.valeur == 5):
                self.points += 5
            elif (de.valeur == 1 and de.valeur == 1 and de.valeur == 4) or ( de.valeur == 4 and de.valeur == 4 and de.valeur == 4):
                self.points += 4
            elif (de.valeur == 1 and de.valeur == 1 and de.valeur == 3) or ( de.valeur == 3 and de.valeur == 3 and de.valeur == 3):
                self.points += 3
            elif (de.valeur == 1 and de.valeur == 1 and de.valeur == 2) or ( de.valeur == 2 and de.valeur == 2 and de.valeur == 2):
                self.points += 2
            elif (de.valeur == 1 and de.valeur == 2 and de.valeur == 3) or ( de.valeur == 4 and de.valeur == 5 and de.valeur == 6):
                self.points += 2
            else:
                self.points += 1 
                
    def __str__(self):
        return self.nom

class Partie:
    def __init__(self, joueurs):
        self.joueurs = joueurs
        self.tour = 1
        
    def jouer_tour(self):
        print("Tour", self.tour)
        for joueur in self.joueurs:
            joueur.jouer()
            joueur.afficher_des()
            joueur.compter_points()
            print(joueur, "a", joueur.points, "points ce tour.")
        perdant_tour = max(self.joueurs, key=lambda j: j.points)
        self.tour += 1
        return perdant_tour
        
    def jouer(self):
        perdant = None
        while perdant == None or perdant.points < 21:
            perdant = self.jouer_tour()
        print(perdant, "a perdu la partie !")
        
    
j1 = Joueur("Moi")
j2 = Joueur("Toi")
partie = Partie([j1, j2])