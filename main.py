import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("ИГРА МИШЕНЬ")

icon = pygame.image.load("img/shuter.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Уровень скорости перемещения мишени
level = 0.25

# Скорость перемещения мишени
speed_x = random.choice([-level, level])
speed_y = random.choice([-level, level])

# Переменная для хранения баллов
score = 0

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

def draw_text(surface, text, pos, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                speed_x = random.choice([-level, level])
                speed_y = random.choice([-level, level])
                score += int(level*10)  # Добавляем баллы в зависимости от уровня

    # Обновление позиции мишени
    target_x += speed_x
    target_y += speed_y

    # Проверка границ экрана и изменение направления движения
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        speed_x = -speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        speed_y = -speed_y

    screen.blit(target_image, (target_x, target_y))

    # Отображение текущего счета
    draw_text(screen, f"Счет: {score}", (SCREEN_WIDTH - 150, 10), font)

    pygame.display.update()

pygame.quit()



