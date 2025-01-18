import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 800
screen_height = 600

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Птичка на проводах")

# Загрузка изображения
background_image = pygame.image.load("picPython.JPG")

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    pygame.display.flip()

import pygame
import sys
import random

# Устанавливаем размер окна
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy Bird")

# Загружаем изображения
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Константы
GRAVITY = 0.5
BIRD_X = 50
PIPE_GAP = 150
PIPE_SPEED = 4
SCORE_FONT = pygame.font.SysFont("Arial", 32)

# Класс для птички
class Bird:
    def __init__(self, y):
        self.x = BIRD_X
        self.y = y
        self.velocity = 0

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        if self.y < 0:
            self.y = 0
            self.velocity = 0
        if self.y > 550:
            self.y = 550
            self.velocity = 0

    def jump(self):
        self.velocity = -9

# Класс для труб
class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.top_y = y - PIPE_GAP / 2 - pipe_image.get_height()
        self.bottom_y = y + PIPE_GAP / 2

    def draw(self):
        screen.blit(pipe_image, (self.x, self.top_y))
        flipped_pipe = pygame.transform.flip(pipe_image, False, True)
        screen.blit(flipped_pipe, (self.x, self.bottom_y))

    def collides_with_bird(self, bird):
        bird_mask = pygame.mask.from_surface(bird_image)
        top_pipe_mask = pygame.mask.from_surface(pipe_image)
        bottom_pipe_mask = pygame.mask.from_surface(pygame.transform.flip(pipe_image, False, True))

        offset_top = (round(self.x - bird.x), round(self.top_y - bird.y))
        offset_bottom = (round(self.x - bird.x), round(self.bottom_y - bird.y))

        point_top = bird_mask.overlap(top_pipe_mask, offset_top)
        point_bottom = bird_mask.overlap(bottom_pipe_mask, offset_bottom)

        return point_top or point_bottom

    def update(self):
        self.x -= PIPE_SPEED
        if self.x < -pipe_image.get_width():
            self.x = 500
            self.top_y = random.randint(0, 350) - pipe_image.get_height()
            self.bottom_y = self.top_y + PIPE_GAP

# Начальные условия
bird = Bird(300)
pipes = [Pipe(500, random.randint(0, 350))]
score = 0
clock = pygame.time.Clock()

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Обновление состояния игры
    bird.update()
    for pipe in pipes:
        pipe.update()
        if pipe.collides_with_bird(bird):
            pygame.quit()
            sys.exit()

    # Добавление новой трубы каждые 125 фреймов
    if len(pipes) < 2 and pipes[-1].x < 325:
        new_pipe_y = random.randint(0, 350)
        pipes.append(Pipe(500, new_pipe_y))

    # Отрисовка элементов
    screen.fill((135, 206, 235))  # Небесный фон
    for pipe in pipes:
        pipe.draw()
    bird.draw()

    # Отображение счета
    score_text = SCORE_FONT.render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (175, 50))

    # Обновление дисплея
    pygame.display.flip()
    clock.tick(60)

    # Увеличение счета
    score += 1






# Завершение работы Pygame
pygame.quit()



