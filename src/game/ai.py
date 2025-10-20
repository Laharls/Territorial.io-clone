class AI:
    def __init__(self, owner_name):
        """Initialise l'IA
        
        Args:
            owner_name: Nom du propriétaire (ex: "ai")
        """
        self.owner_name = owner_name
    
    def play_turn(self, game_map):
        """L'IA joue son tour
        
        Args:
            game_map: Objet Map contenant tous les territoires
        """
        # 1. Récupérer MES territoires
        mes_territoires = [t for t in game_map.territories if t.owner == self.owner_name]

        # 2. Pour chaque territoire
        for territory in mes_territoires:
            # 3. Si assez d'armées
            if territory.armies > 10:
                # 4. Récupérer voisins ennemis
                # 5. Trouver le plus faible
                # 6. Attaquer
                voisins_ennemis = [v for v in territory.neighbors if v.owner != "ai"]
                if len(voisins_ennemis) > 0:
                    cible = min(voisins_ennemis, key=lambda t: t.armies)

                    nb_troops = territory.send_troops(cible, percentage=0.5)
                    cible.receive_attack(nb_troops, self.owner_name, territory.color)