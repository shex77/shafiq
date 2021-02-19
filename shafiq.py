import pygame

import time

import random

 

pygame.init()

 

white = (255, 255, 255)

yellow = (255, 255, 102)

black = (0, 0, 0)

red = (213, 50, 80)

green = (0, 255, 0)

blue = (50, 153, 213)

 

dis_width = 500

dis_height = 500

 

dis = pygame.display.set_mode((dis_width, dis_height))

border=(0,0,500,500)

 

clock = pygame.time.Clock()

 

snake_block = 10

snake_speed = 9

 

font_style = pygame.font.SysFont("bahnschrift", 25)

 

def our_snake(snake_block, snake_list):

    for x in snake_list:

        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

        pygame.draw.rect(dis,(0, 0, 255),border,5)

 

 

def message(msg, color):

    mesg = font_style.render(msg, True, color)

    dis.blit(mesg, [200, 150])

def Score(score, color):

    Sco = font_style.render(score, True, color)

    dis.blit(Sco, [100, 50])

    

def gameLoop():

    

    game_over = False

    game_close = False

 

    x1 = dis_width / 2

    y1 = dis_height / 2

 

    x1_change = 0

    y1_change = 0

 

    snake_List = []

    Length_of_snake = 1

 

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

 

    while not game_over:

 

        while game_close == True:

            dis.fill(yellow)

            message("Game Over ! P-Play or Q-Quit", red)

 

            pygame.display.update()

 

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:

                        game_over = True

                        game_close = False

                    if event.key == pygame.K_p:

                        gameLoop()

 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_f:

                    x1_change = -snake_block

                    y1_change = 0

                elif event.key == pygame.K_h:

                    x1_change = snake_block

                    y1_change = 0

                elif event.key == pygame.K_t:

                    y1_change = -snake_block

                    x1_change = 0

                elif event.key == pygame.K_c:

                    y1_change = snake_block

                    x1_change = 0

 

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:

            game_close = True

        x1 += x1_change

        y1 += y1_change

        dis.fill(yellow)

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_Head = []

        snake_Head.append(x1)

        snake_Head.append(y1)

        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:

            del snake_List[0]

 

        for x in snake_List[:-1]:

            if x == snake_Head:

                game_close = True

 

        our_snake(snake_block, snake_List)

 

 

        pygame.display.update()

 

        if x1 == foodx and y1 == foody:

            Score("GOOOOOOD", green)

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            Length_of_snake += 1

            pygame.display.update()

 

        clock.tick(snake_speed)

 

    pygame.quit()

    quit()

 

 

gameLoop()
