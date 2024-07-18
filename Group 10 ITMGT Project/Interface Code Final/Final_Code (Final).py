#!/usr/bin/env python
# coding: utf-8

# In[7]:


# super final code
import os
import pygame
import sys

# Function to get the image path
def get_image_path(file_name):
    return os.path.join('images', file_name)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Charge")
main_font = pygame.font.SysFont("Bungee Regular", 50)

# Define the Background sprite class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        self.rect1 = self.image.get_rect()
        self.rect2 = self.image.get_rect()
        self.rect1.topleft = (0, 0)
        self.rect2.topleft = (0, -screen_height)
        self.dy = 1  # Y-axis movement speed
    
    def update(self):
        self.rect1.y += self.dy
        self.rect2.y += self.dy

        if self.rect1.top >= HEIGHT:
            self.rect1.bottom = 0
        if self.rect2.top >= HEIGHT:
            self.rect2.bottom = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect1)
        screen.blit(self.image, self.rect2)

class Title(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Skill_List(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
# Define the Button sprite class
class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, x_pos, y_pos, text_input):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 100))
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(x_pos, y_pos))
    
    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            return True
        return False
    
    def change_color(self, position):
        if self.rect.collidepoint(position):
            self.text = main_font.render(self.text_input, True, "violet")
        else:
            self.text = main_font.render(self.text_input, True, "white")

class SkillIcon(pygame.sprite.Sprite):
    def __init__(self, name, image_path, x, y, width, height):
        super().__init__()
        self.name = name
        self.image_path = image_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.original_image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.clicked = False
        self.hovered = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            self.clicked = not self.clicked
            self.change_color()
            return True
        return False
    
    def change_color(self):
        if self.clicked:
            self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
            self.image.fill((0, 255, 0, 100), None, pygame.BLEND_RGBA_MULT)
        elif self.hovered:
            self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
            self.image.fill((255, 0, 0, 100), None, pygame.BLEND_RGBA_MULT)
        else:
            self.image = pygame.transform.scale(self.original_image, (self.width, self.height))

    def reset_color(self):
        self.clicked = False
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))

class Aura(SkillIcon):
    def __init__(self):
        super().__init__("Aura", get_image_path("Aura.png"), 350, 800, 100, 100)

class Shield(SkillIcon):
    def __init__(self):
        super().__init__("Shield", get_image_path("Shield.png"), 435, 800, 100, 100)

class Teleport(SkillIcon):
    def __init__(self):
        super().__init__("Teleport", get_image_path("Teleport.png"), 393, 880, 100, 100)

class Dranken(SkillIcon):
    def __init__(self):
        super().__init__("Dranken", get_image_path("Dranken.png"), 535, 800, 100, 100)

class Split_Dranken(SkillIcon):
    def __init__(self):
        super().__init__("Split Dranken", get_image_path("Split_Dranken.png"), 620, 800, 100, 100)

class Sniper(SkillIcon):
    def __init__(self):
        super().__init__("Sniper", get_image_path("Sniper.png"), 578, 880, 100, 100)

class Hex_Flame(SkillIcon):
    def __init__(self):
        super().__init__("Hex Flame", get_image_path("Hex_Flame.png"), 720, 800, 100, 100)

class Warshield(SkillIcon):
    def __init__(self):
        super().__init__("Warshield", get_image_path("Warshield.png"), 805, 800, 100, 100)

class Scut(SkillIcon):
    def __init__(self):
        super().__init__("Scut", get_image_path("Scut.png"), 763, 880, 100, 100)

class Shotgun(SkillIcon):
    def __init__(self):
        super().__init__("Shotgun", get_image_path("Shotgun.png"), 905, 800, 100, 100)

class Fireball(SkillIcon):
    def __init__(self):
        super().__init__("Fireball", get_image_path("Fireball.png"), 905, 880, 100, 100)

class Charge(SkillIcon):
    def __init__(self):
        super().__init__("Charge", get_image_path("Charge.png"), 1270, 800, 100, 100)

class Repair(SkillIcon):
    def __init__(self):
        super().__init__("Repair", get_image_path("Repair.png"), 1270, 880, 100, 100)

class Airbomb(SkillIcon):
    def __init__(self):
        super().__init__("Airbomb", get_image_path("Airbomb.png"), 990, 823, 120, 120)
        
class Airbomb_Strike(SkillIcon):
    def __init__(self):
        super().__init__("Airbomb Strike", get_image_path("Airbomb_Strike.png"), 1090, 785, 200, 200)

class Battery(SkillIcon):
    def __init__(self):
        super().__init__("BatteryIcon", get_image_path("Battery.png"), 1360, 570, 450, 450)  # Adjust the position and size as needed

class BatteryBar(SkillIcon):
    def __init__(self):
        super().__init__("BatteryBar", get_image_path("Battery_Bar.png"), 1495, 850, 180, 200)
    
    # Additional methods specific to BatteryBar can be added here

class SkillIconsBackground(pygame.sprite.Sprite):
    def __init__(self, name, image_path, x, y, width, height):
        super().__init__()  # Initialize the Sprite superclass
        self.name = name
        self.image_path = image_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def get_position(self):
        return self.x, self.y
    
    def get_dimensions(self):
        return self.width, self.height
    
    def __str__(self):
        return f"SkillIconsBackground: Position=({self.x}, {self.y}), Dimensions=({self.width}, {self.height})"

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Green_Table(SkillIconsBackground):
    def __init__(self):
        super().__init__("SkillIconsBackground", get_image_path("SkillBackground.png"), 300, 700, 1200, 400)

class Opponent(pygame.sprite.Sprite):
    def __init__(self, name, image_path, x, y, width, height):
        super().__init__()
        self.name = name
        self.image_path = image_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class TopOpponent(Opponent):
    def __init__(self):
        super().__init__("TopOpponent", get_image_path("Top_Opponent.png"), 710, 50, 600, 200)

class LeftOpponent(Opponent):
    def __init__(self):
        super().__init__("LeftOpponent", get_image_path("Left_Opponent.png"), 190, 150, 250, 400)

class RightOpponent(Opponent):
    def __init__(self):
        super().__init__("RightOpponent", get_image_path("Right_Opponent.png"), 1480, 150, 250, 400)

class Player(pygame.sprite.Sprite):
    def __init__(self, name, image_path, x, y, width, height):
        super().__init__()
        self.name = name
        self.image_path = image_path
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.original_image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.clicked = False
        self.hovered = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.clicked:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 5)  # Draw green outline if clicked

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.image = self.original_image.copy()
                self.image.fill((255, 0, 0, 100), None, pygame.BLEND_RGBA_MULT)
                self.hovered = True
        else:
            if self.hovered and not self.clicked:
                self.image = self.original_image.copy()
                self.hovered = False

    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            self.clicked = not self.clicked
            self.change_color()
            return True
        return False
    
    def change_color(self):
        if self.clicked:
            self.image = self.original_image.copy()
            self.image.fill((0, 255, 0, 100), None, pygame.BLEND_RGBA_MULT)
        elif self.hovered:
            self.image = self.original_image.copy()
            self.image.fill((255, 0, 0, 100), None, pygame.BLEND_RGBA_MULT)
        else:
            self.image = self.original_image.copy()

    def reset_color(self):
        self.clicked = False
        self.image = self.original_image.copy()

class Player_1(Player):
    def __init__(self):
        super().__init__("Player1", get_image_path("Player_1.png"), 900, 270, 200, 200)

class Player_2(Player):
    def __init__(self):
        super().__init__("Player2", get_image_path("Player_2.png"), 1100, 270, 200, 200)

class Player_3(Player):
    def __init__(self):
        super().__init__("Player3", get_image_path("Player_3.png"), 900, 470, 200, 200)

class Player_4(Player):
    def __init__(self):
        super().__init__("Player4", get_image_path("Player_4.png"), 1100, 470, 200, 200)
    
class UI:
    def __init__(self, monster, get_input):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WIDTH / 2 - 100
        self.top = HEIGHT / 2 + 50
        self.monster = monster
        self.get_input = get_input
        
        # Control
        self.state = 'general'
        self.selected_skill = None
        self.targets_to_select = 0
        self.selected_targets = []
        
        # Moves storage
        self.turn_moves = []
        self.targets = []
        self.player_charges = 1
        self.opponent1_charges = 1
        self.opponent2_charges = 1
        self.opponent3_charges = 1

    def input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()

        if self.state == 'general':
            if mouse_buttons[0]:  # If the left mouse button is clicked
                for skill_icon in skill_icon_group:
                    if skill_icon.check_for_input(mouse_pos):
                        self.selected_skill = skill_icon.name
                        target_type = TARGET_DATA.get(self.selected_skill)
                        if target_type == 'Single':
                            self.targets_to_select = 1
                        elif target_type == 'Double':
                            self.targets_to_select = 1
                        elif target_type == 'AOE':
                            self.targets_to_select = 3  # AOE targets all automatically
                        self.state = 'select_target'
                        break
        elif self.state == 'select_target':
            if mouse_buttons[0]:
                for player in [player_1, player_2, player_3, player_4]:
                    if player.rect.collidepoint(mouse_pos) and player not in self.selected_targets:
                        self.selected_targets.append(player)
                        player.clicked = True
                        player.change_color()
                        self.get_input(self.selected_skill, player.__class__.__name__)
                        if len(self.selected_targets) == self.targets_to_select:
                            self.finalize_selection()
                        break
            elif mouse_buttons[2]:  # Right-click to deselect skill
                self.reset_selection()

    def finalize_selection(self):
        self.turn_moves.append(self.selected_skill)
        self.targets.extend(self.selected_targets)
        for target in self.selected_targets:
            self.get_input(self.selected_skill, target.__class__.__name__)
        self.reset_selection()

    def reset_selection(self):
        self.state = 'general'
        self.selected_skill = None
        self.targets_to_select = 0
        self.selected_targets = []
        for skill_icon in skill_icon_group:
            skill_icon.reset_color()
        for player in [player_1, player_2, player_3, player_4]:
            player.reset_color()

    def deselect_last_target(self):
        if self.selected_targets:
            last_target = self.selected_targets.pop()
            last_target.reset_color()

    def update(self):
        self.input()
    
    def draw(self):
        if self.state == 'select_target' and self.selected_skill:
            target_type = TARGET_DATA.get(self.selected_skill)
            if target_type == 'Single':
                text_surface = self.font.render("Select a target to attack", True, (255, 255, 255))
            elif target_type == 'Double':
                text_surface = self.font.render("Select a target not to attack", True, (255, 255, 255))
            elif target_type == 'AOE':
                text_surface = self.font.render("AOE. All targets have been hit", True, (255, 255, 255))
            else:
                text_surface = self.font.render(f"{self.selected_skill} has been used", True, (255, 255, 255))
            screen.blit(text_surface, (self.left, self.top))

    def handle_escape_key(self, event):
        if event.key == pygame.K_ESCAPE and self.state == 'select_target':
            self.reset_selection()

# These are just to draw the image paths
# Background
background_image_path = get_image_path('Background.png')
background = Background(background_image_path, WIDTH, HEIGHT)

# Title
title_path = get_image_path('Title Page.png')
title = Title(title_path, 160, 115, 1600, 850)

skill_list_path = get_image_path('Skill_List.png')
skill_list = Skill_List(skill_list_path, 1600, 900)

# Skill Icons
aura = Aura()
shield = Shield()
teleport = Teleport()
dranken = Dranken()
split_dranken = Split_Dranken()
sniper = Sniper()
hex_flame = Hex_Flame()
warshield = Warshield()
scut = Scut()
shotgun = Shotgun()
fireball = Fireball()
charge = Charge()
repair = Repair()
airbomb = Airbomb()
airbomb_strike = Airbomb_Strike()
battery = Battery()
battery_bar = BatteryBar()

# Opponents
top_opponent = TopOpponent()
left_opponent = LeftOpponent()
right_opponent = RightOpponent()

# Icon Background
icon_background = Green_Table()

# Create button instances
button_path = get_image_path('Button.png')
play_game = Button(button_path, WIDTH // 2, HEIGHT // 2 - 60, "PLAY GAME")
game_moves = Button(button_path, WIDTH // 2, HEIGHT // 2 + 80, "HOW TO PLAY")
quit_game = Button(button_path, WIDTH // 2, HEIGHT // 2 + 230, "QUIT")
back = Button(button_path, WIDTH // 2, HEIGHT // 2 - 400, "BACK")

# Players
player_1 = Player_1()
player_2 = Player_2()
player_3 = Player_3()
player_4 = Player_4()

# Sprite group and additional sprites
background_group = pygame.sprite.Group(background)
title_group = pygame.sprite.Group(title)
main_menu_buttons = pygame.sprite.Group(play_game, game_moves, quit_game)
skill_icon_group = pygame.sprite.Group(aura, shield, teleport, dranken, split_dranken, sniper, hex_flame, warshield, scut, shotgun, fireball, charge, repair, airbomb, airbomb_strike, battery, battery_bar)
player_group = pygame.sprite.Group(player_1, player_2, player_3, player_4)
skill_icon_bg_group = pygame.sprite.Group(icon_background)
opponent_group = pygame.sprite.Group(top_opponent, left_opponent, right_opponent)
how_to_play_buttons = pygame.sprite.Group(back)
moves = pygame.sprite.Group(skill_list)


INTERACTION_DATA = {
    'Split Dranken': {
        'Shield': '-',
        'Aura': 'Kill',
        'Warshield': '-',
        'Teleport': 0.75,
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': '-',
        'Dranken': '-',
        'Sniper': '-',
        'Scut': '-',
        'Hex Flame': '-',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Dranken': {
        'Shield': '-',
        'Aura': 'Kill',
        'Warshield': '-',
        'Teleport': 0.5,
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': '-',
        'Sniper': '-',
        'Scut': '-',
        'Hex Flame': '-',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Sniper': {
        'Shield': '-',
        'Aura': 'Kill',
        'Warshield': '-',
        'Teleport': '-',
        'Charge': '-',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': '-',
        'Scut': '-',
        'Hex Flame': '-',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Scut': {
        'Shield': '-',
        'Aura': 'Gain 1 Ch',
        'Warshield': '-',
        'Teleport': 0.25,
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': '-',
        'Hex Flame': '-',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Hex Flame': {
        'Shield': 'Breaks',
        'Aura': 'Gain 1 Ch',
        'Warshield': '-',
        'Teleport': '-',
        'Charge': '-',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': 'Kill',
        'Hex Flame': '-',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Fireball': {
        'Shield': 'Kill',
        'Aura': 'Kill',
        'Warshield': '-',
        'Teleport': 0.125,
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': 'Kill',
        'Hex Flame': 'Kill',
        'Fireball': '-',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Shotgun': {
        'Shield': 'Kill',
        'Aura': 'Kill',
        'Warshield': 'Breaks',
        'Teleport': 0.5,
        'Charge': '-',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': 'Kill',
        'Hex Flame': 'Kill',
        'Fireball': 'Kill',
        'Shotgun': '-',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Airbomb': {
        'Shield': 'Kill',
        'Aura': 'Kill',
        'Warshield': 'Breaks',
        'Teleport': 'Kill',
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': 'Kill',
        'Hex Flame': 'Kill',
        'Fireball': 'Kill',
        'Shotgun': 'Kill',
        'Airbomb': '-',
        'Airbomb Strike': '-'
    },
    'Airbomb Strike': {
        'Shield': 'Kill',
        'Aura': 'Kill',
        'Warshield': 'Kill',
        'Teleport': 'Kill',
        'Charge': 'Kill',
        'Repair': 'Kill',
        'Split Dranken': 'Kill',
        'Dranken': 'Kill',
        'Sniper': 'Kill',
        'Scut': 'Kill',
        'Hex Flame': 'Kill',
        'Fireball': 'Kill',
        'Shotgun': 'Kill',
        'Airbomb': 'Kill',
        'Airbomb Strike': '-'
    }
}

RANDOM_DATA = {
    'Random1': ['Split Dranken', 'Dranken', 'Sniper'],
    'Random2': ['Scut', 'Hex Flame'],
    'Random3': ['Fireball', 'Shotgun'],
}

COST_DATA = {
    'Split Dranken': 1,
    'Dranken': 1,
    'Sniper': 1,
    'Scut': 2,
    'Hex Flame': 2,
    'Fireball': 3,
    'Shotgun': 3,
    'Airbomb': 4,
    'Airbomb Strike': 5,
    'Warshield': 2
}
TARGET_DATA = {
    "Split Dranken": 'Double',
    "Dranken": 'Single',
    "Sniper": 'Single',
    "Scut": 'AOE',
    "Hex Flame": 'AOE',
    "Fireball": 'Double',
    "Shotgun": 'Double',
    "Airbomb": 'AOE',
    "Airbomb Strike": 'AOE'
}

# Function to handle skill use
def use_skill(skill_name, target):
    print(f"Used {skill_name} on {target}")

# Create UI instance
ui = UI(None, use_skill)

class Game:
    def __init__(self):
        self.game_state = "main_menu"
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.game_state == "main_menu":
                    if play_game.check_for_input(pos):
                        self.game_state = "game_interface"
                    if game_moves.check_for_input(pos):
                        self.game_state = "how_to_play"
                    if quit_game.check_for_input(pos):
                        self.running = False
                elif self.game_state == "how_to_play":
                    if back.check_for_input(pos):
                        self.game_state = "main_menu"
                elif self.game_state == "game_interface":
                    ui.input()
            if event.type == pygame.KEYDOWN:
                ui.handle_escape_key(event)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        pos = pygame.mouse.get_pos()
        for button in main_menu_buttons:
            button.change_color(pos)
        for button in how_to_play_buttons:
            button.change_color(pos)
        if self.game_state == "game_interface":
            for skill_icon in skill_icon_group:
                skill_icon.hovered = skill_icon.rect.collidepoint(pos)
                skill_icon.change_color()
            for player in player_group:
                player.hovered = player.rect.collidepoint(pos)
                player.change_color()

    def draw(self):
        screen.fill((0, 0, 0))
        background_group.update()
        background.draw(screen)  # Manually draw the background

        if self.game_state == "main_menu":
            title_group.draw(screen)
            main_menu_buttons.update()
        elif self.game_state == "game_interface":
            skill_icon_bg_group.draw(screen)
            skill_icon_group.draw(screen)
            opponent_group.draw(screen)
            player_group.draw(screen)
            ui.draw()  # Manually call UI draw method here
        elif self.game_state == "how_to_play":
            moves.draw(screen)
            how_to_play_buttons.draw(screen)
            how_to_play_buttons.update()
        
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

# Start the game
game = Game()
game.run()

