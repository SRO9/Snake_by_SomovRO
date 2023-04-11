import pygame as pg
import random

pg.init()
# задаем игровое поле и цвета
w = 800
h = 600
white = 255, 255, 255
black = 0, 0, 0
red = 200, 0, 0
green = 152, 251, 152
blue = 66, 170, 255
orange = 250, 87, 25

main_surf = pg.display.set_mode((w, h))

pg.display.set_caption("SNAKE by SomovRO")
# pg.display.set_icon(pg.image.load(r"C:\Users\romas\Desktop\photo_2023-03-29_15-13-25.jpg"))
pg.display.update()
# прописываем координаты и нужные параметры


# задаем fps

FPS = 15
clock = pg.time.Clock()

snake_block = 20

font_style = pg.font.SysFont('calibri', 40, bold=True, italic=True)
score_font = pg.font.SysFont('verdana', 40)


def get_score(score):
    value = score_font.render(f"Ваш счет: {score}", True, black)
    main_surf.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for i in snake_list:
        pg.draw.rect(main_surf, black, [i[0], i[1], snake_block, snake_block])


def message(msg, color, x=0, y=0):
    caption = font_style.render(msg, True, color)
    main_surf.blit(caption, [w / 2.8 + x, h / 2.5 + y])


def game_loop():
    out = False
    game_over = False

    # начальное положене змейки
    x1 = w // 2
    y1 = h // 2

    # изменение координат змейки
    x1_change = 0
    y1_change = 0

    snake_list = []  # текущая длина змейки
    length_snake = 1

    foodx = round(random.randrange(0, w - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, h - snake_block) / snake_block) * snake_block

    while not game_over:
        while out:
            main_surf.fill(blue)
            message(f"Ваш счет {length_snake - 1}!", orange)
            message("Нажмите R для повтора или Q для выхода", black, x=-260, y=50)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        game_loop()
                    elif event.key == pg.K_q:
                        game_over = True
                        out = False
                if event.type == pg.QUIT:
                    game_over = True
                    out = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            x1_change = snake_block
            y1_change = 0
        elif keys[pg.K_LEFT]:
            x1_change = -snake_block
            y1_change = 0
        elif keys[pg.K_DOWN]:
            x1_change = 0
            y1_change = snake_block
        elif keys[pg.K_UP]:
            x1_change = 0
            y1_change = -snake_block

        if (not 0 <= x1 <= w) or (not 0 <= y1 <= h):
            out = True

        x1 += x1_change
        y1 += y1_change
        main_surf.fill(green)
        pg.draw.rect(main_surf, red, (foodx, foody, snake_block, snake_block))

        snake_head = []  # список из положений головы змейки

        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                out = True

        snake(snake_block, snake_list)
        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, w - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, h - snake_block) / snake_block) * snake_block
            length_snake += 1

        get_score(length_snake - 1)
        pg.display.update()
        clock.tick(FPS)

    pg.quit()

game_loop()
