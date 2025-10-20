import pygame
import math

class AttackAnimation:
    """Gère l'animation d'une attaque entre deux territoires"""
    
    def __init__(self, from_territory, to_territory, nb_troops):
        """
        Args:
            from_territory: Territoire source
            to_territory: Territoire cible
            nb_troops: Nombre de troupes envoyées
        """
        self.from_territory = from_territory
        self.to_territory = to_territory
        self.nb_troops = nb_troops
        
        # Calcul des centres des territoires
        self.start_x, self.start_y = self._get_center(from_territory)
        self.end_x, self.end_y = self._get_center(to_territory)
        
        # Animation
        self.progress = 0.0  # 0.0 à 1.0
        self.speed = 0.02    # Vitesse d'animation (2% par frame = ~50 frames = 0.8sec)
        self.finished = False
        
        # Couleur de la flèche (couleur du propriétaire)
        self.color = from_territory.color
    
    def _get_center(self, territory):
        """Calcule le centre d'un territoire"""
        points = territory.polygon_points
        center_x = sum(p[0] for p in points) / len(points)
        center_y = sum(p[1] for p in points) / len(points)
        return center_x, center_y
    
    def update(self):
        """Met à jour l'animation (appelé chaque frame)"""
        self.progress += self.speed
        if self.progress >= 1.0:
            self.progress = 1.0
            self.finished = True
    
    def draw(self, screen):
        """Dessine la flèche animée"""
        # Position actuelle de la flèche (interpolation linéaire)
        current_x = self.start_x + (self.end_x - self.start_x) * self.progress
        current_y = self.start_y + (self.end_y - self.start_y) * self.progress
        
        # Dessiner la ligne
        pygame.draw.line(screen, self.color, 
                        (self.start_x, self.start_y),
                        (current_x, current_y), 4)
        
        # Dessiner la pointe de la flèche (triangle)
        if self.progress > 0.1:  # Ne dessine la pointe qu'après 10% du trajet
            arrow_size = 15
            angle = math.atan2(self.end_y - self.start_y, self.end_x - self.start_x)
            
            # Points du triangle (pointe de flèche)
            tip_x = current_x
            tip_y = current_y
            
            left_x = tip_x - arrow_size * math.cos(angle - math.pi/6)
            left_y = tip_y - arrow_size * math.sin(angle - math.pi/6)
            
            right_x = tip_x - arrow_size * math.cos(angle + math.pi/6)
            right_y = tip_y - arrow_size * math.sin(angle + math.pi/6)
            
            pygame.draw.polygon(screen, self.color,
                              [(tip_x, tip_y), (left_x, left_y), (right_x, right_y)])
        
        # Afficher le nombre de troupes
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.nb_troops), True, (255, 255, 255))
        # Fond noir pour contraste
        text_rect = text.get_rect(center=(current_x, current_y - 20))
        bg_rect = text_rect.inflate(10, 5)
        pygame.draw.rect(screen, (0, 0, 0), bg_rect)
        pygame.draw.rect(screen, self.color, bg_rect, 2)
        screen.blit(text, text_rect)
    
    def execute_attack(self):
        """Exécute l'attaque réelle quand l'animation est terminée"""
        if self.finished:
            self.to_territory.receive_attack(self.from_territory, self.nb_troops)