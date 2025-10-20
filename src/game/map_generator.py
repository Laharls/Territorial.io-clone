from .game_map import Map

def generate_map(num_territories, width, height):
    """Génère une carte de jeu avec des territoires Voronoï
    
    Args:
        num_territories: Nombre de territoires à générer
        width: Largeur de la carte
        height: Hauteur de la carte
        
    Returns:
        Map: Objet Map contenant tous les territoires
    """
    
    map = Map(num_territories, width, height)
    return map