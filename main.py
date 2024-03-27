from Classes import *
from Functions import *

pygame.init()
WIDHT, HEIGHT = 1000, 800
pygame.display.set_caption("Platformer")
window = pygame.display.set_mode((WIDHT, HEIGHT))
image = pygame.image.load("Python-Platformer/assets/Other/background.png")
image = pygame.transform.scale(image, (1000, 800))
pygame.mixer.init()
pygame.mixer.music.set_endevent(30)
pygame.mixer.music.load("Python-Platformer/assets/Music/soundtrack.mp3")
coin_sound = pygame.mixer.Sound("Python-Platformer/assets/Music/coin.mp3")
coin_sound.set_volume(3.0)
heart_sound = pygame.mixer.Sound("Python-Platformer/assets/Music/heart.mp3")
heart_sound.set_volume(5)
death_sound = pygame.mixer.Sound("Python-Platformer/assets/Music/death.mp3")
death_sound.set_volume(50)
victory_sound = pygame.mixer.Sound("Python-Platformer/assets/Music/victory.mp3")
victory_sound.set_volume(4)
TEXT_FONT_1 = pygame.font.SysFont("Goudy Stout", 50)
TEXT_FONT_2 = pygame.font.SysFont("MV Boli", 30)
TIMER_FONT = pygame.font.SysFont("Goudy Stout", 20)


def lvl1_objects():
    start_checkpoint = StartPoint(-10 * block_size - 10, HEIGHT - 6 * block_size - 64 - 65, 64, 64)
    end_point = EndPoint(18 * block_size - 15, HEIGHT - 6 * block_size - 64 - 65, 64, 64)
    checkpoint = CheckPoint(1 * block_size - 20, HEIGHT - 2 * block_size - 30, 64, 64)
    player = Player(-10 * block_size + 20, HEIGHT - 7 * block_size - 64, 50, 50)
    fire_traps = [Fire(3 * block_size + 30, HEIGHT - block_size - 64, 16, 32),
                  Fire(4 * block_size + 25, HEIGHT - block_size - 64, 16, 32),
                  Fire(-3 * block_size + 30, HEIGHT - 2 * block_size - 64, 16, 32),
                  Fire(-9 * block_size + 30, HEIGHT - 6 * block_size - 64, 16, 32),
                  Fire(-4 * block_size + 30, HEIGHT - 5 * block_size - 64, 16, 32),
                  Fire(-5 * block_size + 65, HEIGHT - 2 * block_size - 64, 16, 32),
                  Fire(14 * block_size + 35, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(16 * block_size + 10, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(16 * block_size + 60, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(17 * block_size + 10, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(17 * block_size + 60, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(18 * block_size + 10, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(18 * block_size + 60, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(19 * block_size + 10, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(19 * block_size + 60, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(0 * block_size + 10, HEIGHT - 2 * block_size - 64, 16, 32),
                  Fire(-1 * block_size + 10, HEIGHT - 3 * block_size - 64, 16, 32)]

    hearts_to_collect = [Heart(1 * block_size + 10, HEIGHT - 7 * block_size - 64, 50, 50),
                         Heart(6 * block_size + 10, HEIGHT - 1 * block_size - 64, 50, 50)]

    coins = [Coin(-6 * block_size, HEIGHT - 2 * block_size, 50, 50),
             Coin(-2 * block_size, HEIGHT - 8 * block_size, 50, 50),
             Coin(2 * block_size, HEIGHT - 3 * block_size, 50, 50),
             Coin(8 * block_size, HEIGHT - 2 * block_size, 50, 50),
             Coin(3 * block_size, HEIGHT - 8 * block_size - 10, 50, 50),
             Coin(11 * block_size, HEIGHT - 7 * block_size, 50, 50),
             Coin(14 * block_size, HEIGHT - 6 * block_size, 50, 50),
             Coin(13 * block_size, HEIGHT - 2 * block_size, 50, 50),
             Coin(-3 * block_size, HEIGHT - 4 * block_size, 50, 50)]

    saw_traps = [Saw(0 * block_size + 20, HEIGHT - 5 * block_size - 64 - 30, 38, 38),
                 Saw(-6 * block_size, HEIGHT - 7 * block_size - 64, 38, 38),
                 Saw(-8 * block_size + 60, HEIGHT - 7 * block_size - 64 - 65, 38, 38),
                 Saw(3 * block_size + 20, HEIGHT - 5 * block_size - 64, 38, 38),
                 Saw(9 * block_size + 20, HEIGHT - 5 * block_size - 64 - 20, 38, 38),
                 Saw(8 * block_size + 20, HEIGHT - 6 * block_size - 64 - 20, 38, 38),
                 Saw(7 * block_size + 20, HEIGHT - 7 * block_size - 64 - 20, 38, 38),
                 Saw(11 * block_size - 50, HEIGHT - 3 * block_size - 64 - 85, 38, 38),
                 Saw(11 * block_size, HEIGHT - 7 * block_size - 64 - 50, 38, 38),
                 Saw(13 * block_size, HEIGHT - 2 * block_size - 64 - 35, 38, 38),
                 Saw(17 * block_size - 40, HEIGHT - 4 * block_size - 64 - 70, 38, 38),
                 Saw(19 * block_size - 40, HEIGHT - 2 * block_size - 64 - 70, 38, 38)]

    left_boundary = [Block(block_size * (-WIDTH // block_size), HEIGHT - block_size * i, block_size) for i in
                     range(0, (HEIGHT // block_size) + 3)]
    right_boundary = [Block(block_size * (2 * WIDTH // block_size), HEIGHT - block_size * i, block_size) for i in
                      range(0, (HEIGHT // block_size) + 3)]
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
    grass_blocks = [Block(2 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(block_size * 5, HEIGHT - block_size * 4, block_size),
                    Block(block_size * 6, HEIGHT - block_size * 3, block_size),
                    Block(block_size * 7, HEIGHT - block_size * 2, block_size),
                    Block(0, HEIGHT - block_size * 2, block_size),
                    Block(-block_size, HEIGHT - block_size * 2, block_size),
                    Block(-block_size, HEIGHT - block_size * 3, block_size),
                    Block(block_size, HEIGHT - block_size * 5 - 40, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(-4 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(-4 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-4 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-4 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-5 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-3 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-3 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 10, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-10 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-9 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-9 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-10 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-5 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(block_size, HEIGHT - block_size * 6 - 40, block_size),
                    Block(5 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(6 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(7 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(8 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(3 * block_size, HEIGHT - block_size * 7 - 30, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 10, block_size),
                    Block(12 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(12 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(12 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(11 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(13 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(13 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(13 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(13 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(11 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(12 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(13 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(14 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(15 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(17 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(18 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(17 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(17 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(17 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(17 * block_size, HEIGHT - block_size * 9, block_size)]

    return start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, saw_traps, \
        left_boundary, right_boundary, floor, grass_blocks


def lvl2_objects():
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, WIDTH * 3 // block_size)]
    left_boundary = [Block(block_size * (-WIDTH // block_size), HEIGHT - block_size * i, block_size) for i in
                     range(0, (HEIGHT // block_size) + 3)]
    right_boundary = [Block(block_size * (3 * WIDTH // block_size), HEIGHT - block_size * i, block_size) for i in
                      range(0, (HEIGHT // block_size) + 3)]
    player = Player(-10 * block_size + 20, HEIGHT - 1 * block_size - 64, 50, 50)
    start_checkpoint = StartPoint(-10 * block_size - 10, HEIGHT - 1 * block_size - 64 - 65, 64, 64)
    end_point = EndPoint(30 * block_size - 15, HEIGHT - 3 * block_size - 64 - 65, 64, 64)
    checkpoint = CheckPoint(14 * block_size - 20, HEIGHT - 8 * block_size - 30, 64, 64)

    fire_traps = [Fire(-10 * block_size + 70, HEIGHT - 4 * block_size - 64, 16, 32),
                  Fire(11 * block_size + 77, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(12 * block_size + 77, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(13 * block_size + 77, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(14 * block_size + 77, HEIGHT - 1 * block_size - 64, 16, 32),
                  Fire(23 * block_size + 63, HEIGHT - 5 * block_size - 64, 16, 32),
                  Fire(27 * block_size, HEIGHT - 5 * block_size - 64, 16, 32)]

    hearts_to_collect = [Heart(1 * block_size + 10, HEIGHT - 7 * block_size - 64, 50, 50),
                         Heart(22 * block_size - 40, HEIGHT - 3 * block_size - 64, 50, 50)]

    coins = [Coin(-10 * block_size - 15, HEIGHT - 4 * block_size - 80, 50, 50),
             Coin(-5 * block_size, HEIGHT - 6 * block_size - 30, 50, 50),
             Coin(-2 * block_size, HEIGHT - 8 * block_size - 30, 50, 50),
             Coin(3 * block_size, HEIGHT - 6 * block_size - 30, 50, 50),
             Coin(9 * block_size, HEIGHT - 6 * block_size, 50, 50),
             Coin(16 * block_size, HEIGHT - 2 * block_size, 50, 50),
             Coin(19 * block_size, HEIGHT - 8 * block_size, 50, 50),
             Coin(25 * block_size, HEIGHT - 4 * block_size, 50, 50),
             Coin(29 * block_size, HEIGHT - 4 * block_size, 50, 50)]

    saw_traps = [Saw(-4 * block_size, HEIGHT - block_size - 38, 38, 38),
                 Saw(-4 * block_size + 50, HEIGHT - block_size - 83, 38, 38),
                 Saw(-4 * block_size, HEIGHT - block_size - 128, 38, 38),
                 Saw(-4 * block_size + 50, HEIGHT - block_size - 173, 38, 38),
                 Saw(-4 * block_size, HEIGHT - block_size - 218, 38, 38),
                 Saw(4 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(5 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(7 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(8 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(15 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(14 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(13 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(12 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(11 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(17 * block_size + 60, HEIGHT - block_size - 20, 38, 38),
                 Saw(17 * block_size + 60, HEIGHT - block_size - 20 - 76, 38, 38),
                 Saw(17 * block_size + 60, HEIGHT - block_size - 20 - 76 - 76, 38, 38),
                 Saw(17 * block_size + 60, HEIGHT - block_size - 20 - 76 - 76 - 76, 38, 38),
                 Saw(18 * block_size + 60, HEIGHT - 4 * block_size - 20, 38, 38),
                 Saw(18 * block_size + 60, HEIGHT - 4 * block_size - 20 - 76, 38, 38),
                 Saw(18 * block_size + 60, HEIGHT - 4 * block_size - 20 - 76 - 76, 38, 38),
                 Saw(18 * block_size + 60, HEIGHT - 4 * block_size - 20 - 76 - 76 - 76, 38, 38),
                 Saw(24 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(26 * block_size + 10, HEIGHT - block_size - 20, 38, 38),
                 Saw(28 * block_size + 10, HEIGHT - block_size - 20, 38, 38)]

    grass_blocks = [Block(-8 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-9 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-9 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-8 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-7 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-10 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-10 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-6 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(-1 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(-5 * block_size, HEIGHT - block_size * 5 - 40, block_size),
                    Block(-2 * block_size, HEIGHT - block_size * 7 - 40, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(0 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(2 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(1 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(3 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(3 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(3 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(3 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(6 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(6 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(6 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(6 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(9 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(10 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(14 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(15 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(15 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(15 * block_size, HEIGHT - block_size * 8, block_size),
                    Block(15 * block_size, HEIGHT - block_size * 9, block_size),
                    Block(18 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(18 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(18 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 6, block_size),
                    Block(19 * block_size, HEIGHT - block_size * 7, block_size),
                    Block(20 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(20 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(20 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(20 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(21 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(21 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(22 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(22 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(23 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(23 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(23 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(23 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(25 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(25 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(27 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(27 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(27 * block_size, HEIGHT - block_size * 4, block_size),
                    Block(27 * block_size, HEIGHT - block_size * 5, block_size),
                    Block(29 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(29 * block_size, HEIGHT - block_size * 3, block_size),
                    Block(30 * block_size, HEIGHT - block_size * 2, block_size),
                    Block(30 * block_size, HEIGHT - block_size * 3, block_size)]

    return start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, saw_traps, \
        left_boundary, right_boundary, floor, grass_blocks


def main(window):
    level = "Menu"

    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    menu_button = Button(960, 10, 21, 22, "Menu", "Minimize")
    pause_button = Button(335, 230, 21, 22, "Pause")
    play_button = Button(405, 230, 21, 22, "Play")
    restart_button = Button(475, 230, 21, 22, "Restart")
    again_button = Button(545, 230, 21, 22, "Again")
    volume_button = Button(615, 230, 21, 22, "NoVolume", "Volume")
    menu_text_button = Button(335, 300, 330, 150, "MenuText", None, 330, 150)
    quit_text_button = Button(335, 480, 330, 150, "QuitText", None, 330, 150)

    menu_play_text_button = Button(335, 200, 330, 150, "PlayText", None, 330, 150)
    menu_quit_text_button = Button(335, 380, 330, 150, "QuitText", None, 330, 150)
    lvl01_button = Button(335, 200, 19, 17, "01", None, 50, 50, "Levels")
    lvl02_button = Button(405, 200, 19, 17, "02", None, 50, 50, "Levels")
    lvl03_button = Button(475, 200, 19, 17, "03", None, 50, 50, "Levels")
    lvl04_button = Button(545, 200, 19, 17, "04", None, 50, 50, "Levels")
    lvl05_button = Button(615, 200, 19, 17, "05", None, 50, 50, "Levels")
    lvl_buttons = [lvl01_button, lvl02_button, lvl03_button, lvl04_button, lvl05_button]

    buttons = [pause_button, play_button, restart_button, again_button, volume_button,
               menu_text_button, quit_text_button]

    heart_image = Heart(0, 0, 50, 50)

    coin_image = Coin(0, 0, 50, 50)

    scroll_area_width = 300
    game_paused = False
    pause_timer = time.time()
    Event = None
    volume = True
    pygame.mixer.music.play()

    run = True
    while run:

        if level == "Menu":
            window.blit(image, (0, 0))
            if not menu_play_text_button.pressed:
                window.blit(menu_play_text_button.image, (menu_play_text_button.rect.x, menu_play_text_button.rect.y))
            else:
                for button in lvl_buttons:
                    window.blit(button.image, (button.rect.x, button.rect.y))

            window.blit(menu_quit_text_button.image, (menu_quit_text_button.rect.x, menu_quit_text_button.rect.y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_quit_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                        run = False
                        break
                    elif not menu_play_text_button.pressed:
                        if menu_play_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                            menu_play_text_button.pressed = True
                    elif menu_play_text_button.pressed:
                        if lvl01_button.rect.collidepoint((pygame.mouse.get_pos())):
                            level = 1
                            start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, saw_traps, left_boundary, \
                                right_boundary, floor, grass_Blocks = lvl1_objects()
                            start_checkpoint.on()
                            for fire in fire_traps:
                                fire.on()
                            for coin in coins:
                                coin.on()
                            for saw in saw_traps:
                                saw.on()

                            dont_collide = ["start"]
                            message = 1
                            timer = time.time()
                            start_timer = time.time()
                            offset_x = - 12 * block_size

                            objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                       *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]
                        if lvl02_button.rect.collidepoint((pygame.mouse.get_pos())):
                            level = 2
                            start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, saw_traps, left_boundary, \
                                right_boundary, floor, grass_Blocks = lvl2_objects()
                            start_checkpoint.on()
                            for fire in fire_traps:
                                fire.on()
                            for coin in coins:
                                coin.on()
                            for saw in saw_traps:
                                saw.on()

                            dont_collide = ["start"]
                            message = 1
                            timer = time.time()
                            start_timer = time.time()
                            offset_x = - 12 * block_size

                            objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                       *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

            pygame.display.update()

        if level == 1:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if menu_button.pressed and not game_paused:
                            menu_button.off()
                            menu_button.pressed = False
                            continue
                        if not menu_button.pressed:
                            menu_button.on()
                            menu_button.pressed = True
                    if menu_button.pressed:
                        if pause_button.rect.collidepoint(pygame.mouse.get_pos()):
                            game_paused = True
                            pause_timer = time.time()
                            pygame.display.update()
                        elif play_button.rect.collidepoint(pygame.mouse.get_pos()) and game_paused:
                            game_paused = False
                            start_timer = start_timer + (time.time() - pause_timer)
                            pygame.display.update()
                        elif restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                            if checkpoint.reached:
                                player.rect.x = checkpoint.rect.x + 20
                                player.rect.y = checkpoint.rect.y - 1 * block_size
                                offset_x = -block_size
                                player.lives = 2
                                player.hit = False
                                message = 1
                                timer = time.time()
                                start_timer = time.time()
                                time.sleep(0.5)
                            else:
                                player.rect.x = -10 * block_size + 20
                                player.rect.y = HEIGHT - 7 * block_size
                                offset_x = - 12 * block_size
                                player.lives = 3
                                player.hit = False
                                message = 1
                                timer = time.time()
                                start_timer = time.time()
                                time.sleep(0.5)

                            menu_button.off()
                            menu_button.pressed = False
                        elif again_button.rect.collidepoint((pygame.mouse.get_pos())):
                            menu_button.pressed = False
                            hearts_to_collect = [Heart(1 * block_size + 10, HEIGHT - 7 * block_size - 64, 50, 50),
                                                 Heart(6 * block_size + 10, HEIGHT - 1 * block_size - 64, 50, 50)]
                            coins = [Coin(-6 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                     Coin(-2 * block_size, HEIGHT - 8 * block_size, 50, 50),
                                     Coin(2 * block_size, HEIGHT - 3 * block_size, 50, 50),
                                     Coin(8 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                     Coin(3 * block_size, HEIGHT - 8 * block_size - 10, 50, 50),
                                     Coin(11 * block_size, HEIGHT - 7 * block_size, 50, 50),
                                     Coin(14 * block_size, HEIGHT - 6 * block_size, 50, 50),
                                     Coin(13 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                     Coin(-3 * block_size, HEIGHT - 4 * block_size, 50, 50)]
                            checkpoint.off()
                            objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                       *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

                            dont_collide = ["start"]
                            player.rect.x = -10 * block_size + 20
                            player.rect.y = HEIGHT - 7 * block_size
                            offset_x = - 12 * block_size
                            player.lives = 3
                            player.coins = 0
                            player.hit = False
                            message = 1
                            timer = time.time()
                            start_timer = time.time()

                            for heart in hearts_to_collect:
                                heart.loop()

                            for coin in coins:
                                coin.on()
                                coin.loop()
                            pygame.display.update()
                            time.sleep(0.5)

                        elif volume_button.rect.collidepoint((pygame.mouse.get_pos())):
                            if volume:
                                volume_button.on()
                                pygame.mixer.music.pause()
                                coin_sound.set_volume(0)
                                heart_sound.set_volume(0)
                                death_sound.set_volume(0)
                                victory_sound.set_volume(0)
                                hit_sound.set_volume(0)
                                volume = False

                            else:
                                volume_button.off()
                                pygame.mixer.music.unpause()
                                coin_sound.set_volume(3.0)
                                heart_sound.set_volume(5)
                                death_sound.set_volume(50)
                                victory_sound.set_volume(4)
                                hit_sound.set_volume(0.6)
                                volume = True

                        elif menu_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                            level = "Menu"
                            menu_play_text_button.pressed = False

                        elif quit_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                            run = False
                            break

                if event.type == 30:
                    pygame.mixer.music.play()

            if game_paused:
                continue

            player.loop(FPS)
            start_checkpoint.loop()
            checkpoint.loop()
            end_point.loop()
            menu_button.loop()
            volume_button.loop()
            volume_button.image = pygame.transform.scale(volume_button.image, (50, 50))
            volume_button.rect = volume_button.image.get_rect(topleft=(volume_button.rect.x, volume_button.rect.y))
            volume_button.mask = pygame.mask.from_surface(volume_button.image)

            for saw in saw_traps:
                saw.loop()
            for fire in fire_traps:
                fire.loop()
            for heart in hearts_to_collect:
                heart.loop()
            for coin in coins:
                coin.loop()

            if handle_move(player, objects, dont_collide, None, None) == "checkpoint":
                checkpoint.on()
                dont_collide.append("checkpoint")

            if handle_move(player, objects, dont_collide, None, None) == "end_point":
                if player.coins < 9:
                    message = 2
                    timer = time.time()
                    continue
                if player.coins == 9:
                    message = 3
                    victory_sound.play()
                    timer = time.time()
                    end_point.on()
                    dont_collide.append("end_point")

            for heart in hearts_to_collect:
                if handle_move(player, objects, dont_collide, heart, None):
                    hearts_to_collect.remove(heart)
                    player.lives += 1
                    heart_sound.play()
                    objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                               *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

            for coin in coins:
                if handle_move(player, objects, dont_collide, None, coin):
                    coin_sound.play()
                    coins.remove(coin)
                    player.coin_colected()
                    objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                               *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

            draw(window, background, bg_image, player, objects, offset_x, player.lives, heart_image, player.coins,
                 coin_image, start_timer)

            window.blit(menu_button.image, (960, 10))
            if menu_button.pressed:
                draw_menu(window, buttons)
            pygame.display.update()

            if time.time() - start_timer > 60:
                player.lives = 0
                message = 5

            if message != 0:
                if message == 1:
                    draw_message(window, "Colecteaza toate cele 9 monede pentru a termina nivelul!", 90, 140)
                elif message == 2:
                    draw_message(window, "Nu ai obtinut monedele necesare!", 200, 140)
                elif message == 3:
                    draw_message(window, "AI CASTIGAT!!!", 430, 140)
                elif message == 4:
                    draw_message(window, "AI MURIT!!!", 440, 140)
                elif message == 5:
                    draw_message(window, "A EXPIRAT TIMPUL, INCEARCA DIN NOU!", 200, 140)
                if time.time() - timer > 3:
                    if message == 3:
                        if level == 1:
                            level = 2
                            menu_button.pressed = False
                            menu_play_text_button.pressed = False
                            start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, saw_traps, left_boundary, \
                                right_boundary, floor, grass_Blocks = lvl2_objects()
                            start_checkpoint.on()
                            for fire in fire_traps:
                                fire.on()
                            for coin in coins:
                                coin.on()
                                coin.loop()
                            for saw in saw_traps:
                                saw.on()
                            for heart in hearts_to_collect:
                                heart.loop()
                            dont_collide = ["start"]
                            message = 1
                            timer = time.time()
                            start_timer = time.time()
                            objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                       *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]
                            checkpoint.off()
                            offset_x = - 12 * block_size
                            pygame.display.update()
                            time.sleep(0.5)

                        elif level == 2:
                            level = "Menu"
                            message = 1
                            menu_button.pressed = False
                            menu_play_text_button.pressed = False
                            pygame.display.update()

                    message = 0

            if player.lives == 0:
                if checkpoint.reached:
                    player.rect.x = checkpoint.rect.x + 20
                    player.rect.y = checkpoint.rect.y - 1 * block_size
                    offset_x = -block_size
                    player.lives = 2
                    player.hit = False
                    if message == 0:
                        message = 4
                    timer = time.time()
                    start_timer = time.time()
                    death_sound.play()
                    time.sleep(0.5)

                else:
                    player.rect.x = -10 * block_size + 20
                    player.rect.y = HEIGHT - 7 * block_size
                    offset_x = - 12 * block_size
                    player.lives = 3
                    player.hit = False
                    if message == 0:
                        message = 4
                    timer = time.time()
                    start_timer = time.time()
                    death_sound.play()
                    time.sleep(0.5)

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                    (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel

        if level == 2:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player.jump_count < 2:
                        player.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if menu_button.pressed and not game_paused:
                            menu_button.off()
                            menu_button.pressed = False
                            continue
                        if not menu_button.pressed:
                            menu_button.on()
                            menu_button.pressed = True
                    if menu_button.pressed:
                        if pause_button.rect.collidepoint(pygame.mouse.get_pos()):
                            game_paused = True
                            pause_timer = time.time()
                            pygame.display.update()
                        elif play_button.rect.collidepoint(pygame.mouse.get_pos()):
                            game_paused = False
                            start_timer = start_timer + (time.time() - pause_timer)
                            pygame.display.update()
                        elif restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                            if checkpoint.reached:
                                player.rect.x = checkpoint.rect.x + 20
                                player.rect.y = checkpoint.rect.y - 1 * block_size
                                offset_x = -block_size
                                player.lives = 2
                                player.hit = False
                                message = 1
                                timer = time.time()
                                start_timer = time.time()
                                time.sleep(0.5)
                            else:
                                player.rect.x = -10 * block_size + 20
                                player.rect.y = HEIGHT - 1 * block_size
                                offset_x = - 12 * block_size
                                player.lives = 3
                                player.hit = False
                                message = 1
                                timer = time.time()
                                start_timer = time.time()
                                time.sleep(0.5)

                            menu_button.off()
                            menu_button.pressed = False
                        elif again_button.rect.collidepoint((pygame.mouse.get_pos())):

                            start_checkpoint, end_point, checkpoint, player, fire_traps, hearts_to_collect, coins, \
                                saw_traps, left_boundary, right_boundary, floor, grass_Blocks = lvl2_objects()

                            start_checkpoint.on()
                            for heart in hearts_to_collect:
                                heart.loop()
                            for fire in fire_traps:
                                fire.on()
                            for coin in coins:
                                coin.on()
                                coin.loop()
                            for saw in saw_traps:
                                saw.on()

                            menu_button.pressed = False
                            checkpoint.off()
                            objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                       *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

                            dont_collide = ["start"]
                            player.rect.x = -10 * block_size + 20
                            player.rect.y = HEIGHT - 1 * block_size
                            offset_x = - 12 * block_size
                            player.lives = 3
                            player.coins = 0
                            player.hit = False
                            message = 1
                            timer = time.time()
                            start_timer = time.time()

                            for coin in coins:
                                coin.on()
                                coin.loop()
                            pygame.display.update()
                            time.sleep(0.5)

                        elif volume_button.rect.collidepoint((pygame.mouse.get_pos())):
                            if volume:
                                volume_button.on()
                                pygame.mixer.music.pause()
                                coin_sound.set_volume(0)
                                heart_sound.set_volume(0)
                                death_sound.set_volume(0)
                                victory_sound.set_volume(0)
                                hit_sound.set_volume(0)
                                volume = False

                            else:
                                volume_button.off()
                                pygame.mixer.music.unpause()
                                coin_sound.set_volume(3.0)
                                heart_sound.set_volume(5)
                                death_sound.set_volume(50)
                                victory_sound.set_volume(4)
                                hit_sound.set_volume(0.6)
                                volume = True

                        elif menu_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                            level = "Menu"
                            menu_play_text_button.pressed = False

                        elif quit_text_button.rect.collidepoint((pygame.mouse.get_pos())):
                            run = False
                            break
                if event.type == 30:
                    pygame.mixer.music.play()

            if game_paused:
                continue

            player.loop(FPS)
            start_checkpoint.loop()
            checkpoint.loop()
            end_point.loop()
            menu_button.loop()
            volume_button.loop()
            volume_button.image = pygame.transform.scale(volume_button.image, (50, 50))
            volume_button.rect = volume_button.image.get_rect(topleft=(volume_button.rect.x, volume_button.rect.y))
            volume_button.mask = pygame.mask.from_surface(volume_button.image)

            for saw in saw_traps:
                saw.loop()
            for fire in fire_traps:
                fire.loop()
            for heart in hearts_to_collect:
                heart.loop()
            for coin in coins:
                coin.loop()

            if handle_move(player, objects, dont_collide, None, None) == "checkpoint":
                checkpoint.on()
                dont_collide.append("checkpoint")

            if handle_move(player, objects, dont_collide, None, None) == "end_point":
                if player.coins < 9:
                    message = 2
                    timer = time.time()
                    continue
                if player.coins == 9:
                    message = 3
                    victory_sound.play()
                    timer = time.time()
                    end_point.on()
                    dont_collide.append("end_point")

            for heart in hearts_to_collect:
                if handle_move(player, objects, dont_collide, heart, None):
                    hearts_to_collect.remove(heart)
                    player.lives += 1
                    heart_sound.play()
                    objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                               *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

            for coin in coins:
                if handle_move(player, objects, dont_collide, None, coin):
                    coin_sound.play()
                    coins.remove(coin)
                    player.coin_colected()
                    objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                               *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

            draw(window, background, bg_image, player, objects, offset_x, player.lives, heart_image, player.coins,
                 coin_image, start_timer)

            window.blit(menu_button.image, (960, 10))

            if menu_button.pressed:
                draw_menu(window, buttons)
            pygame.display.update()

            if time.time() - start_timer > 60:
                player.lives = 0
                message = 5

            if message != 0:
                if message == 1:
                    draw_message(window, "Colecteaza toate cele 9 monede pentru a termina nivelul!", 90, 140)
                elif message == 2:
                    draw_message(window, "Nu ai obtinut monedele necesare!", 200, 140)
                elif message == 3:
                    draw_message(window, "AI CASTIGAT!!!", 430, 140)
                elif message == 4:
                    draw_message(window, "AI MURIT!!!", 440, 140)
                elif message == 5:
                    draw_message(window, "A EXPIRAT TIMPUL, INCEARCA DIN NOU!", 200, 140)
                if time.time() - timer > 3:
                    if message == 3:
                        level = "Menu"
                        menu_button.pressed = False
                        menu_play_text_button.pressed = False
                        hearts_to_collect = [Heart(1 * block_size + 10, HEIGHT - 7 * block_size - 64, 50, 50),
                                             Heart(6 * block_size + 10, HEIGHT - 1 * block_size - 64, 50, 50)]
                        coins = [Coin(-6 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                 Coin(-2 * block_size, HEIGHT - 8 * block_size, 50, 50),
                                 Coin(2 * block_size, HEIGHT - 3 * block_size, 50, 50),
                                 Coin(8 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                 Coin(3 * block_size, HEIGHT - 8 * block_size - 10, 50, 50),
                                 Coin(11 * block_size, HEIGHT - 7 * block_size, 50, 50),
                                 Coin(14 * block_size, HEIGHT - 6 * block_size, 50, 50),
                                 Coin(13 * block_size, HEIGHT - 2 * block_size, 50, 50),
                                 Coin(-3 * block_size, HEIGHT - 4 * block_size, 50, 50)]
                        checkpoint.off()
                        objects = [*floor, *left_boundary, *right_boundary, *grass_Blocks, *fire_traps, *saw_traps,
                                   *hearts_to_collect, *coins, start_checkpoint, checkpoint, end_point]

                        dont_collide = ["start"]
                        player.rect.x = -10 * block_size + 20
                        player.rect.y = HEIGHT - 7 * block_size
                        offset_x = - 12 * block_size
                        player.lives = 3
                        player.coins = 0
                        player.hit = False
                        timer = time.time()
                        start_timer = time.time()

                        for heart in hearts_to_collect:
                            heart.loop()

                        for coin in coins:
                            coin.on()
                            coin.loop()
                        pygame.display.update()
                        time.sleep(0.5)
                    message = 0

            if player.lives == 0:
                if checkpoint.reached:
                    player.rect.x = checkpoint.rect.x + 20
                    player.rect.y = checkpoint.rect.y - 1 * block_size
                    offset_x = checkpoint.rect.x - 2 * block_size
                    player.lives = 2
                    player.hit = False
                    if message == 0:
                        message = 4
                    timer = time.time()
                    start_timer = time.time()
                    death_sound.play()
                    time.sleep(0.5)

                else:
                    player.rect.x = -10 * block_size + 20
                    player.rect.y = HEIGHT - 1 * block_size
                    offset_x = - 12 * block_size
                    player.lives = 3
                    player.hit = False
                    if message == 0:
                        message = 4
                    timer = time.time()
                    start_timer = time.time()
                    death_sound.play()
                    time.sleep(0.5)

            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                    (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
