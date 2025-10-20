from .territory import Territory
from scipy.spatial import Voronoi
import random

class Map:
    def __init__(self, num_territories, width, height):
        self.num_territories = num_territories
        self.width = width
        self.height = height
        self.territories = []
        self.voronoi = None

        self._generate()

    def _generate(self):
        """Génère la carte complète"""
        # Étape 1 : Générer les points
        all_points, num_real = self._generate_points()
        
        # Étape 2 : Créer le Voronoï
        self.voronoi = Voronoi(all_points)
        
        # Étape 3 : Créer les Territory (TODO)
        for i in range(num_real):
            center = tuple(all_points[i])
            region_idx = self.voronoi.point_region[i]
            region = self.voronoi.regions[region_idx]

            if -1 in region or len(region) == 0:
                continue

            polygon_points = [self.voronoi.vertices[idx] for idx in region]
    
            # 3. Déterminer owner et color
            if i == 0:
                owner = "player"
                color = (50, 150, 255)
            elif i < 2:
                owner = "ai"
                color = (255, 50, 50)
            else:
                owner = "neutral"
                color = (180, 180, 180)
        
        # Étape 4 : Calculer les voisinages (TODO)
            territory = Territory(center, polygon_points, owner, color)
            self.territories.append(territory)

        # Étape 5 : Calculer les voisinages
        for p1, p2 in self.voronoi.ridge_points:
            # Vérifier que les deux points sont dans les territoires réels
            if p1 < len(self.territories) and p2 < len(self.territories):
                # Ajouter la relation de voisinage
                self.territories[p1].neighbors.append(self.territories[p2])
                self.territories[p2].neighbors.append(self.territories[p1])

    def _generate_points(self):
        # 1. Générer les points réels
        margin = 50
        real_points = []
        for _ in range(self.num_territories):
            x = random.randint(margin, self.width - margin)
            y = random.randint(margin, self.height - margin)

            real_points.append([x, y])
            
        # 2. Générer les points fantômes
        border_margin = 300
        border_points = []
        step = 100

        for x in range(-border_margin, self.width + border_margin, step):
            border_points.append([x, -border_margin])
            border_points.append([x, self.height + border_margin])

        for y in range(-border_margin, self.height + border_margin, step):
            border_points.append([-border_margin, y])
            border_points.append([self.width + border_margin, y])
        
        # 3. Combiner
        all_points = real_points + border_points
        
        return all_points, len(real_points)