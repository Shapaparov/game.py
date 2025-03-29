import random
import threading

import pygame

# Инициализация Pygame
pygame.init()

# Настройки игры
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простая игра")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 375
        self.rect.y = 500
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


# Создание игрока
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Функция для генерации случайных чисел
def generate_random_numbers():
    while True:
        random.randint(1, 1000000)


# Создание потока для генерации случайных чисел
random_thread = threading.Thread(target=generate_random_numbers)
random_thread.start()

# Основной игровой цикл
running = True
while running:
    clock.tick(60)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
