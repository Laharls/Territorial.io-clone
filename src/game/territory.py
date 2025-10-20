from shapely.geometry import Point, Polygon

class Territory:
    def __init__(self, center, polygon_points, owner="neutral",color=(180, 180, 180), neighbors=None, armies=20):
        self.center = center
        self.polygon_points = polygon_points
        self.owner = owner
        self.color = color
        self.armies = armies

        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    
    def grow(self):
        if self.owner != "neutral":
            self.armies += 1/60
    
    def can_attack(self, attacked_territory):
        """Vérifie si on peut attaquer un territoire
    
        Args:
            attacked_territory: Objet Territory à attaquer
            
        Returns:
            bool: True si l'attaque est possible, False sinon
        """
        return (attacked_territory in self.neighbors and 
            self.armies >= 2)

    def send_troops(self, target, percentage=0.5):
        """Envoie des troupes vers un territoire voisin
    
        Args:
            target: Territory à attaquer
            percentage: Pourcentage des armées à envoyer (0.0 à 1.0)
            
        Returns:
            int: Nombre de troupes envoyées (0 si impossible)
        """
        # 1. Vérifier si possible d'attaquer
        if not self.can_attack(target):
            return 0 # Pas d'attaque possible
        # 2. Calculer le nombre de troupes
        nb_troops = max(1, int(self.armies * percentage))
        # 3. Diminuer self.armies
        self.armies -= nb_troops
        # 4. Retourner le nombre envoyé
        return nb_troops
    
    def contains_point(self, x, y):
        point = Point(x, y)
        polygon = Polygon(self.polygon_points)
        return polygon.contains(point)
    
    def receive_attack(self, nb_troops, attacker_owner, attacker_color):
        """Reçoit une attaque de troupes ennemies
        
        Args:
            nb_troops: Nombre de troupes attaquantes
            attacker_owner: Propriétaire de l'attaquant
            attacker_color: Couleur de l'attaquant
        """
        if self.owner == attacker_owner:
            self.armies += nb_troops
            return
        else:
            if nb_troops > self.armies:
                self.owner = attacker_owner
                self.color = attacker_color
                self.armies = nb_troops - self.armies
                return
            elif nb_troops == self.armies:
                self.owner = "neutral"
                self.color = (180, 180, 180)
                self.armies = 0
                return
            else:
                self.armies -= nb_troops
                if self.armies <= 0:
                    self.owner = "neutral"
                    self.color = (180, 180, 180)
                    self.armies = 0
                return