import pygame

pygame.init()

w_in_squares = 10
h_in_squares = 10

square_dim = 50

drawing_window = pygame.display.set_mode((w_in_squares * square_dim, h_in_squares * square_dim))

drawing_window.fill((127, 127, 127))

the_colour_white = (255, 255, 255)
the_colour_black = (0, 0, 0)

current_colour = the_colour_white

finished = False

while not finished:
    for i in range(0, h_in_squares):
        for j in range(0, w_in_squares):
            pygame.draw.rect(drawing_window, current_colour, (j * square_dim, i * square_dim, square_dim, square_dim))
            pygame.display.update()
            pygame.time.delay(100)
            if current_colour == the_colour_white:
                current_colour = the_colour_black
            else:
                current_colour = the_colour_white
        if current_colour == the_colour_white:
            current_colour = the_colour_black
        else:
            current_colour = the_colour_white
