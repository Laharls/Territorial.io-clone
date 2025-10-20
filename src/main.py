import pygame
from game.ai import AI
from game.map_generator import generate_map
from ui.renderer import Renderer

WIDTH = 1200
HEIGHT = 800
NUM_TERRITORIES = 25

def check_game_over(game_map):
    """Vérifie si quelqu'un a gagné
    
    Returns:
        str: "player" si joueur gagne, "ai" si IA gagne, None si jeu continue
    """
    player_territories = 0
    ai_territories = 0

    for territory in game_map.territories:
        if territory.owner == "player":
            player_territories += 1
        elif territory.owner == "ai":
            ai_territories += 1

    if player_territories == 0:
        return "ai"
    elif ai_territories == 0:
        return "player"
    else:
        return None


def main():
    # Initialisation
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    # Créer les objets
    game_map = generate_map(NUM_TERRITORIES, WIDTH, HEIGHT)
    renderer = Renderer(screen)

    bot = AI("ai")

    selected_territory = None
    ai_cooldown = 0
    attack_percentage = 0.5
    
    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Clic détecté à {mouse_pos}")
                
                clicked_territory = None

                for territory in game_map.territories:
                    if territory.contains_point(mouse_pos[0], mouse_pos[1]):
                        clicked_territory = territory
                        break

                if clicked_territory:
                    print(f"Territoire cliqué ! Propriétaire : {clicked_territory.owner}")

                    if selected_territory is None:
                        if clicked_territory.owner == "player":
                            selected_territory = clicked_territory
                            print("✅ Territoire sélectionné !")
                        else:
                            print("❌ Ce territoire ne vous appartient pas")
                    else:
                        print("Entrer dans la boucle else")
                        if selected_territory.can_attack(clicked_territory):
                            nb_troops = selected_territory.send_troops(clicked_territory, percentage=attack_percentage)
                            print(f"🚀 Envoi de {nb_troops} troupes !")

                            clicked_territory.receive_attack(nb_troops, selected_territory.owner, selected_territory.color)

                            selected_territory = None
                        else:
                            print("❌ Impossible d'attaquer ce territoire (pas voisin ou pas assez d'armées)")
                            selected_territory = None
                            if clicked_territory.owner == "player":
                                selected_territory = clicked_territory
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    attack_percentage = 0.25
                elif event.key == pygame.K_2:
                    attack_percentage = 0.5
                elif event.key == pygame.K_3:
                    attack_percentage = 0.75
                elif event.key == pygame.K_4:
                    attack_percentage = 1.0
        
        # Mettre à jour
        for territory in game_map.territories:
            territory.grow()
        
        ai_cooldown += 1
        if ai_cooldown >= 120:
            ai_cooldown = 0
            bot.play_turn(game_map)

        # Vérifier si quelqu'un a gagné
        winner = check_game_over(game_map)
        if winner:
            running = False

        # Dessiner
        renderer.draw_map(game_map, selected_territory, attack_percentage)
        pygame.display.flip()
        
    clock.tick(60)
    
    # ========== ÉCRAN DE FIN ==========
    if winner:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        font_big = pygame.font.Font(None, 74)
        font_small = pygame.font.Font(None, 36)
        
        if winner == "player":
            text_main = font_big.render("VICTOIRE !", True, (0, 255, 0))
            text_sub = font_small.render("Vous avez conquis tous les territoires !", True, (255, 255, 255))
        else:
            text_main = font_big.render("DEFAITE", True, (255, 0, 0))
            text_sub = font_small.render("L'IA a conquis tous vos territoires", True, (255, 255, 255))
        
        text_quit = font_small.render("Fermez la fenetre pour quitter", True, (200, 200, 200))
        
        screen.blit(text_main, (WIDTH//2 - text_main.get_width()//2, HEIGHT//2 - 100))
        screen.blit(text_sub, (WIDTH//2 - text_sub.get_width()//2, HEIGHT//2))
        screen.blit(text_quit, (WIDTH//2 - text_quit.get_width()//2, HEIGHT//2 + 80))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
    
    pygame.quit()

if __name__ == "__main__":
    main()