import pygame

class Renderer:
    def __init__(self, screen):
        """Initialise le renderer
        
        Args:
            screen: Surface Pygame où dessiner
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 24)  # Police pour les textes
    
    def draw_territory(self, territory):
        """Dessine un territoire (polygone + armées)
        
        Args:
            territory: Objet Territory à dessiner
        """
        # 1. Dessiner le polygone rempli
        pygame.draw.polygon(self.screen, territory.color, territory.polygon_points)
        
        # 2. Dessiner le contour noir
        pygame.draw.polygon(self.screen, (0, 0, 0), territory.polygon_points, 2)
        
        # 3. Afficher le nombre d'armées au centre
        armies_text = str(int(territory.armies))
        text_surface = self.font.render(armies_text, True, (255, 255, 255))  # Texte blanc
        text_rect = text_surface.get_rect(center=territory.center)
        self.screen.blit(text_surface, text_rect)
    
    def draw_map(self, game_map, selected_territory=None, attack_percentage=0.5):
        """Dessine toute la carte"""
        # 1. Effacer l'écran
        self.screen.fill((0, 128, 255))
        
        # 2. Dessiner tous les territoires
        for territory in game_map.territories:
            self.draw_territory(territory)  # ← D'abord dessiner normalement
            
            if territory == selected_territory:  # ← PUIS ajouter le contour spécial
                pygame.draw.polygon(self.screen, (255, 255, 0), territory.polygon_points, 3)
        
        # Afficher le pourcentage d'attaque
        font = pygame.font.Font(None, 32)
        text = font.render(f"Attaque: {int(attack_percentage * 100)}%", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        # Afficher les touches disponibles
        font_small = pygame.font.Font(None, 24)
        text_help = font_small.render("Touches: 1=25%  2=50%  3=75%  4=100%", True, (200, 200, 200))
        self.screen.blit(text_help, (10, 45))