import time
import pygame
from os.path import isfile, join


from Functions import load_sprite_sheets, get_block
pygame.init()
FPS = 60


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)
    ANIMATION_DELAY = 4

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.lives = 3
        self.coins = 0
        self.invulnerability = False
        self.invulnerability_count = time.time()

    def jump(self):
        self.y_vel = -self.GRAVITY * 10
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True
        self.hit_count = 0

    def lives_count(self):
        if time.time() - self.invulnerability_count < 0.3:
            self.lives += 1
        self.invulnerability = True
        self.lives -= 1
        pass

    def coin_colected(self):
        self.coins += 1

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > FPS * 2:
            self.hit = False
            self.hit_count = 0
        if self.invulnerability:
            if time.time() - self.invulnerability_count > 1:
                self.invulnerability = False
                self.invulnerability_count = time.time()

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        if self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Button(Object):
    def __init__(self, x, y, width, height, animation_mane_1=None, animation_name_2=None, scale_dim_1=50, scale_dim_2 = 50, directory="Buttons"):
        super().__init__(x, y, width, height, "button")
        self.animation_name_1 = animation_mane_1
        self.animation_name_2 = animation_name_2
        self.button = load_sprite_sheets("Menu", directory, width, height)
        self.image = self.button[self.animation_name_1][0]
        self.image = pygame.transform.scale(self.image, (scale_dim_1, scale_dim_2))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_name = self.animation_name_1
        self.pressed = False

    def on(self):
        self.animation_name = self.animation_name_2

    def off(self):
        self.animation_name = self.animation_name_1

    def loop(self):
        self.image = self.button[f"{self.animation_name}"][0]
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)


class Heart(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "heart")
        path = join("Python-Platformer", "assets", "Other", "Heart.png")
        self.image = pygame.image.load(path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (70, 70))

    def loop(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)


class Coin(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "coin")
        self.coin = load_sprite_sheets("Items", "Coin", width, height)
        self.image = self.coin["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.coin[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask .from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (70, 70))

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Saw(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "saw")
        self.saw = load_sprite_sheets("Traps", "Saw", width, height)
        self.image = self.saw["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.saw[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Fire(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class StartPoint(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "start")

        self.start = load_sprite_sheets("Items", "Checkpoints", width, height, False, "Start")
        self.image = self.start["Start (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Start (Idle)"

    def on(self):
        self.animation_name = "Start (Moving) (64x64)"

    def off(self):
        self.animation_name = "Start (Idle)"

    def loop(self):
        sprites = self.start[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class EndPoint(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "end_point")
        self.end = load_sprite_sheets("Items", "Checkpoints", width, height, False, "End")
        self.image = self.end["End (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "End (Idle)"

    def on(self):
        self.animation_name = "End (Pressed) (64x64)"

    def off(self):
        self.animation_name = "End (Idle)"

    def loop(self):
        sprites = self.end[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class CheckPoint(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "checkpoint")

        self.checkpoint = load_sprite_sheets("Items", "Checkpoints", width, height, False, "Checkpoint")
        self.image = self.checkpoint["Checkpoint (No Flag)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Checkpoint (No Flag)"
        self.reached = False

    def on(self):
        self.animation_name = "Checkpoint (Flag Out) (64x64)"
        self.reached = True

    def off(self):
        self.animation_name = "Checkpoint (No Flag)"
        self.image = self.checkpoint["Checkpoint (No Flag)"][0]
        self.reached = False
        self.animation_count = 0

    def loop(self):
        if self.reached:
            sprites = self.checkpoint[self.animation_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.image = sprites[sprite_index]
            self.animation_count += 1

            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
            self.mask = pygame.mask.from_surface(self.image)

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
                self.animation_count = 0
                self.animation_name = "Checkpoint (Flag Idle)(64x64)"
