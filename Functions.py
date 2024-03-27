import time
import pygame
from os import listdir
from os.path import isfile, join

from main import TIMER_FONT, TEXT_FONT_1, TEXT_FONT_2

FPS = 60
WIDTH, HEIGHT = 1000, 800
PLAYER_VEL = 5
block_size = 96

pygame.mixer.init()
hit_sound = pygame.mixer.Sound("Python-Platformer/assets/Music/hit.mp3")
hit_sound.set_volume(0.6)


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False, dir3=None):
    path = join("Python-Platformer", "assets", dir1, dir2)
    if dir3:
        path = join("Python-Platformer", "assets", dir1, dir2, dir3)

    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("Python-Platformer", "assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


def get_background(name):
    image = pygame.image.load(join("Python-Platformer", "assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x,
         lives, heart, coins_collected, coin_image, start_timer):
    lives_str = lives.__str__() + "×"
    formatted_lives_score = TEXT_FONT_1.render(f"{lives_str}", 1, (67, 15, 4))

    coins_str = coins_collected.__str__() + "×"
    formatted_coins_collected = TEXT_FONT_1.render(f"{coins_str}", 1, (248, 187, 37))
    coin_image.image = pygame.transform.scale(coin_image.image, (70, 70))

    formatted_start_timer = TIMER_FONT.render(f"{(time.time() - start_timer):.1f}", 1, (0, 0, 0))

    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    window.blit(formatted_lives_score, (840, 40))
    window.blit(heart.image, (910, 30))

    window.blit(formatted_coins_collected, (50, 40))
    window.blit(coin_image.image, (120, 30))

    window.blit(formatted_start_timer, (900, 10))



    pygame.display.update()


def draw_message(window, text, x, y):
    COLOR = (157, 249, 104)
    BLACK = (0, 0, 0)
    offset = 2

    formatted_text = TEXT_FONT_2.render(text, 1, COLOR)
    outline = TEXT_FONT_2.render(text, 1, BLACK)
    window.blit(outline, (x - offset, y))
    window.blit(outline, (x, y - offset))
    window.blit(outline, (x + offset, y))
    window.blit(outline, (x, y + offset))
    window.blit(formatted_text, (x, y))
    pygame.display.update()


def draw_menu(window, buttons):
    pass
    pygame.draw.rect(window, (0, 0, 0), (300, 200, 400, 470))
    pygame.draw.rect(window, (255, 255, 255), (305, 205, 390, 460))
    for button in buttons:
        window.blit(button.image, (button.rect.x, button.rect.y))
    pygame.display.update()


def handle_vertical_collision(player, objects, dy, dont_collide):
    collided_objects = []
    for obj in objects:
        if obj.name not in dont_collide:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                collided_objects.append(obj)
            if obj.name in dont_collide:
                if player.rect.y == obj.rect.y - 2:
                    collided_objects.append(obj)
                if player.rect.y == obj.rect.y + 2:
                    collided_objects.append(obj)

    return collided_objects


def collide(player, objects, dx, dont_collide):
    player.move(dx, 0)
    player.update()
    collided_object = None

    for obj in objects:
        if obj.name not in dont_collide:
            if pygame.sprite.collide_mask(player, obj):
                collided_object = obj
                break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects, dont_collide, heart=None, coin=None):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2, dont_collide)
    collide_right = collide(player, objects, PLAYER_VEL * 2, dont_collide)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel, dont_collide)
    to_check = [collide_left, collide_right, *vertical_collide]

    trap_name = ["fire", "saw"]

    for obj in to_check:
        if obj:
            if heart and obj.name == heart.name and obj.rect == heart.rect:
                return True
            if coin and obj.name == coin.name and obj.rect == coin.rect:
                return True
            if obj.name in trap_name:
                if not player.invulnerability:
                    player.make_hit()
                    player.lives_count()
                    hit_sound.play()
            if obj.name == "checkpoint":
                return "checkpoint"
            if obj.name == "end_point":
                return "end_point"
