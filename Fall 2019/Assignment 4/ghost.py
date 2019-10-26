import pygame

pygame.init()

white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255

displayheight = 600
displaywidth = 800

game_display = pygame.display.set_mode((displaywidth, displayheight))
background_image = pygame.image.load('./images/background.jpg')
game_display.blit(pygame.transform.scale(background_image, (displaywidth, displayheight)), (0, 0))

ghostimg = pygame.image.load('./images/ghost.png')

clicked = False
running = True
def main(width, height):
    global clicked
    width = width+100
    height = height+100
    game_display.blit(pygame.transform.scale(ghostimg, (150, 300)), (width, height))
    clicked = True


crashed = False
while not crashed:
    for event in pygame.event.get():
        while running:
            y = int(input(f"input your x or width value from 1 to {displaywidth} \n"))
            z = int(input(f"input your y or height value; from 1 to {displayheight} \n"))
            main(y, z)
            change = input("Do you want to change your values\n").lower()
            if change == "no":
                running = False
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()