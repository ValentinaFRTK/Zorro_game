import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
screen_width = 800
screen_height = 600

# Создание игрового окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра")

# Цвета
FORESTGREEN = (34, 139, 34)

# Позиция и скорость главного героя
hero_x = 100
hero_y = 100
hero_speed = 0.5

# Загрузка кадров анимации
frames = []
for i in range(10):
    frame = pygame.image.load(f"pictures/Diego_walk{i+1}.png")  # Замените на путь к вашим кадрам
    frames.append(frame)

# Размер кадров
frame_width = 300
frame_height = 300

# Изменение размера кадров
frames = [pygame.transform.scale(frame, (frame_width, frame_height)) for frame in frames]

current_frame = 0
frame_counter = 0
animation_speed = 60  # Скорость смены кадров анимации

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_x -= hero_speed
    if keys[pygame.K_RIGHT]:
        hero_x += hero_speed
    if keys[pygame.K_UP]:
        hero_y -= hero_speed
    if keys[pygame.K_DOWN]:
        hero_y += hero_speed

    # Обновление анимации
    frame_counter += 1
    if frame_counter >= animation_speed:
        current_frame = (current_frame + 1) % len(frames)
        frame_counter = 0

    # Очистка экрана
    screen.fill(FORESTGREEN)

    # Отрисовка главного героя
    current_frame_image = frames[current_frame]
    screen.blit(current_frame_image, (hero_x, hero_y))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()