import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров окна
screen_width = 1000
screen_height = 700

# Создание игрового окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра")

# Цвета
FORESTGREEN = (34, 139, 34)

# Позиция и скорость главного героя
hero_x = 100
hero_y = 100
hero_speed = 0.35

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
animation_speed = 70  # Скорость смены кадров анимации
is_moving = False  # Флаг, указывающий, что персонаж движется

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        is_moving = True
        if keys[pygame.K_LEFT] and hero_x > -100:
            hero_x -= hero_speed
        if keys[pygame.K_RIGHT] and hero_x < screen_width - frame_width + 100:
            hero_x += hero_speed
        if keys[pygame.K_UP] and hero_y > 0:
            hero_y -= hero_speed
        if keys[pygame.K_DOWN] and hero_y < screen_height - frame_height:
            hero_y += hero_speed
    else:
        is_moving = False
        current_frame = 0  # Возвращаемся к первому кадру анимации

    # Обновление анимации
    if is_moving:
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