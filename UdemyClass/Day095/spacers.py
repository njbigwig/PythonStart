# Copilot prompt:
# I need a python program for: Space Invaders - Build the classic arcade game where you shoot down alien ships. 
# I want an 8-bit bit mapped graphics look, like the game. 
# Exclude any deprecated packages. functions, or methods. 
# It would be great to include any sounds and track and display the score.


# pip install pygame

import sys
import math
import random
import pygame
import numpy as np
import time

# -------- Config --------
WIDTH, HEIGHT = 480, 640
SCALE = 4  # pixel scale factor for crisp 8-bit look
FPS = 60

ALIEN_COLS = 8
ALIEN_ROWS = 4
ALIEN_X_MARGIN = 20
ALIEN_Y_MARGIN = 60
ALIEN_X_SPACING = 18
ALIEN_Y_SPACING = 16

PLAYER_SPEED = 3
BULLET_SPEED = 6
ALIEN_BULLET_SPEED = 4
ALIEN_MOVE_X_SPEED = 0.1
ALIEN_MOVE_Y_STEP = 0.2
ALIEN_FIRE_CHANCE = 0.002  # per alien per frame

LIVES = 3

# -------- Init --------
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - 8-bit")
clock = pygame.time.Clock()

# -------- Colors --------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (230, 50, 50)
HUD_COLOR = (220, 220, 220)

# -------- Sound helpers --------
def square_wave(freq=440, duration_ms=120, volume=0.3, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    t = np.arange(n_samples)
    # Square wave: sign of sine
    wave = np.sign(np.sin(2 * np.pi * freq * t / sample_rate)).astype(np.float32)
    # Apply simple decay for retro bleeps
    decay = np.linspace(1.0, 0.5, n_samples).astype(np.float32)
    wave *= decay
    wave = (wave * volume * 32767).astype(np.int16)
    return pygame.mixer.Sound(wave)

SND_SHOOT = square_wave(700, 80, 0.35)
SND_HIT = square_wave(300, 100, 0.4)
SND_EXPLODE = square_wave(100, 200, 0.5)

# -------- Pixel sprite helpers --------
def make_sprite(pattern, fg=GREEN, bg=None):
    """pattern: list of strings of '0' (off) and '1' (on)"""
    h = len(pattern)
    w = len(pattern[0])
    surf = pygame.Surface((w * SCALE, h * SCALE), pygame.SRCALPHA)
    if bg is not None:
        surf.fill(bg)
    for y in range(h):
        for x in range(w):
            if pattern[y][x] == '1':
                rect = pygame.Rect(x * SCALE, y * SCALE, SCALE, SCALE)
                surf.fill(fg, rect)
    return surf

# Simple 8-bit style sprites (11x8-ish)
ALIEN_PATTERNS = [
    [
        "00111100",
        "01111110",
        "11111111",
        "11011011",
        "11111111",
        "01100110",
        "11000011",
        "01000010",
    ],
    [
        "00111100",
        "01111110",
        "11111111",
        "11011011",
        "11111111",
        "01100110",
        "10000001",
        "01000010",
    ],
]

PLAYER_PATTERN = [
    "00011000",
    "00011000",
    "00111100",
    "01111110",
    "11111111",
    "00111100",
    "00011000",
    "00011000",
]

BARRIER_PATTERN = [
    "11111111",
    "11111111",
    "11111111",
    "11111111",
    "11101111",
    "11000111",
    "10000011",
    "00000001",
]

BULLET_PATTERN = ["1"]

ALIEN_COLOR = (80, 200, 120)
PLAYER_COLOR = (200, 200, 255)
BULLET_COLOR = (255, 255, 255)
BARRIER_COLOR = (100, 255, 100)

ALIEN_SPRITES = [make_sprite(p, ALIEN_COLOR) for p in ALIEN_PATTERNS]
PLAYER_SPRITE = make_sprite(PLAYER_PATTERN, PLAYER_COLOR)
BULLET_SPRITE = make_sprite(BULLET_PATTERN, BULLET_COLOR)
ALIEN_BULLET_SPRITE = make_sprite(BULLET_PATTERN, RED)
BARRIER_SPRITE = make_sprite(BARRIER_PATTERN, BARRIER_COLOR)

# -------- Entities --------
class Player:
    def __init__(self):
        self.sprite = PLAYER_SPRITE
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 40)
        self.cooldown = 0

    def update(self, pressed):
        if pressed[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if pressed[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self, bullets):
        if self.cooldown == 0 and not any(b.owner == "player" for b in bullets):
            bullets.append(Bullet(self.rect.centerx, self.rect.top, -BULLET_SPEED, "player"))
            SND_SHOOT.play()
            self.cooldown = 15

    def draw(self, surf):
        surf.blit(self.sprite, self.rect)

class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.alive = True

    def rect(self):
        r = ALIEN_SPRITES[self.frame].get_rect()
        r.x = int(self.x)
        r.y = int(self.y)
        return r

    def draw(self, surf):
        if self.alive:
            surf.blit(ALIEN_SPRITES[self.frame], (int(self.x), int(self.y)))

class Bullet:
    def __init__(self, x, y, vy, owner):
        self.sprite = BULLET_SPRITE if owner == "player" else ALIEN_BULLET_SPRITE
        self.rect = self.sprite.get_rect()
        self.rect.center = (x, y)
        self.vy = vy
        self.owner = owner

    def update(self):
        self.rect.y += self.vy

    def draw(self, surf):
        surf.blit(self.sprite, self.rect)

class Barrier:
    def __init__(self, x, y):
        self.sprite = BARRIER_SPRITE.copy()
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (x, y)
        # Use mask for damage
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, surf):
        surf.blit(self.sprite, self.rect)

    def damage_at(self, point, radius=2):
        # Carve out pixels
        px, py = point[0] - self.rect.x, point[1] - self.rect.y
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                if 0 <= px + dx < self.rect.width and 0 <= py + dy < self.rect.height:
                    if dx*dx + dy*dy <= radius*radius:
                        pygame.draw.rect(self.sprite, (0, 0, 0, 0),
                                         pygame.Rect(px + dx, py + dy, 1, 1))
        self.mask = pygame.mask.from_surface(self.sprite)

# -------- Game setup --------
player = Player()

aliens = []
start_x = ALIEN_X_MARGIN
start_y = ALIEN_Y_MARGIN
for row in range(ALIEN_ROWS):
    for col in range(ALIEN_COLS):
        x = start_x + col * ALIEN_X_SPACING * SCALE
        y = start_y + row * ALIEN_Y_SPACING * SCALE
        aliens.append(Alien(x, y))

bullets = []
barriers = []
barrier_count = 3
for i in range(barrier_count):
    bx = (WIDTH // (barrier_count + 1)) * (i + 1) - (BARRIER_SPRITE.get_width() // 2)
    by = HEIGHT - 140
    barriers.append(Barrier(bx, by))

alien_dir = 1
alien_speed_x = ALIEN_MOVE_X_SPEED
tick = 0
score = 0
lives = LIVES
font = pygame.font.SysFont("Consolas", 18)

def reset_wave():
    global aliens, alien_dir, alien_speed_x
    aliens.clear()
    for row in range(ALIEN_ROWS):
        for col in range(ALIEN_COLS):
            x = start_x + col * ALIEN_X_SPACING * SCALE
            y = start_y + row * ALIEN_Y_SPACING * SCALE
            aliens.append(Alien(x, y))
    alien_dir = 1
    alien_speed_x = ALIEN_MOVE_X_SPEED

def draw_hud():
    hud = f"Score: {score}   Lives: {lives}"
    text = font.render(hud, True, HUD_COLOR)
    screen.blit(text, (10, 10))

def any_alien_reached_player_line():
    return any(a.alive and a.y + ALIEN_SPRITES[0].get_height() >= player.rect.top for a in aliens)

def aliens_rects():
    return [a.rect() for a in aliens if a.alive]

# -------- Main loop --------
running = True
print("minimize other windows, game is starting....")
time.sleep(10)
while running:
    dt = clock.tick(FPS)
    tick += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False
            elif event.key == pygame.K_SPACE:
                player.shoot(bullets)

    pressed = pygame.key.get_pressed()
    player.update(pressed)

    # Animate aliens
    if tick % 30 == 0:
        for a in aliens:
            a.frame = (a.frame + 1) % len(ALIEN_SPRITES)

    # Move aliens horizontally, bounce at edges, step down
    left_edge = min((r.x for r in aliens_rects()), default=0)
    right_edge = max((r.x + r.width for r in aliens_rects()), default=WIDTH)
    bounce = False
    if left_edge <= 10:
        alien_dir = 1
        bounce = True
    elif right_edge >= WIDTH - 10:
        alien_dir = -1
        bounce = True

    for a in aliens:
        if a.alive:
            a.x += alien_speed_x * alien_dir

    if bounce:
        for a in aliens:
            a.y += ALIEN_MOVE_Y_STEP
        alien_speed_x *= 1.01  # speed up slightly as they bounce

    # Alien firing
    for a in aliens:
        if a.alive and random.random() < ALIEN_FIRE_CHANCE:
            rect = a.rect()
            bullets.append(Bullet(rect.centerx, rect.bottom, ALIEN_BULLET_SPEED, "alien"))

    # Update bullets
    for b in bullets:
        b.update()
    bullets = [b for b in bullets if -20 < b.rect.y < HEIGHT + 20]

    # Collisions: player bullet vs alien
    for b in [x for x in bullets if x.owner == "player"]:
        hit = None
        for a in aliens:
            if a.alive and b.rect.colliderect(a.rect()):
                hit = a
                break
        if hit:
            hit.alive = False
            score += 10
            SND_HIT.play()
            bullets.remove(b)

    # Collisions: alien bullet vs player
    for b in [x for x in bullets if x.owner == "alien"]:
        if b.rect.colliderect(player.rect):
            lives -= 1
            SND_EXPLODE.play()
            bullets.remove(b)
            player.cooldown = 30
            if lives <= 0:
                running = False

    # Collisions: bullets vs barriers (damage)
    for b in list(bullets):
        for barrier in barriers:
            if b.rect.colliderect(barrier.rect):
                barrier.damage_at(b.rect.center, radius=3)
                bullets.remove(b)
                break

    # Check if aliens reached player line
    if any_alien_reached_player_line():
        lives -= 1
        SND_EXPLODE.play()
        reset_wave()
        if lives <= 0:
            running = False

    # If all aliens dead, next wave with faster speed, bonus
    if not any(a.alive for a in aliens):
        score += 50
        reset_wave()
        alien_speed_x *= 1.1

    # -------- Draw --------
    screen.fill(BLACK)
    # Ground line
    pygame.draw.line(screen, (60, 60, 60), (0, HEIGHT - 60), (WIDTH, HEIGHT - 60), 2)

    for barrier in barriers:
        barrier.draw(screen)

    for a in aliens:
        a.draw(screen)

    for b in bullets:
        b.draw(screen)

    player.draw(screen)
    draw_hud()

    pygame.display.flip()

# -------- Game over screen --------
screen.fill(BLACK)
msg = font.render(f"Game Over  |  Final Score: {score}", True, WHITE)
screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 10))
pygame.display.flip()
pygame.time.wait(2000)

pygame.quit()
sys.exit()
