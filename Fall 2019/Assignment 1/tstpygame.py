import pygame

pygame.init()

# main colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 125, 0)
blue = (0, 0, 255)
light_blue = (135,206,235)
brown = (139,69,19)
dark_brown = (100, 50, 0)
lime_green = (50, 205, 50)
dark_blue = (0, 0, 125)

# display window
houseDisplay = pygame.display.set_mode((500,500))
houseDisplay.fill(light_blue)

# clouds
pygame.draw.ellipse(houseDisplay, (245, 245, 245), (0, 0, 130, 70))
pygame.draw.ellipse(houseDisplay, (255, 255, 250 ), (20, 20, 150, 70))
pygame.draw.ellipse(houseDisplay, (240, 240, 240), (20, 0, 150, 70))
pygame.draw.ellipse(houseDisplay, (255, 255, 250 ), (120, 20, 150, 70))
pygame.draw.ellipse(houseDisplay, (240, 240, 240), (120, 0, 150, 70))
pygame.draw.ellipse(houseDisplay, (245, 245, 245), (100, 0, 130, 70))
pygame.draw.ellipse(houseDisplay, (245, 245, 245), (200, 0, 130, 70))
pygame.draw.ellipse(houseDisplay, (255, 255, 250 ), (220, 20, 150, 70))
pygame.draw.ellipse(houseDisplay, (240, 240, 240), (220, 0, 150, 70))
pygame.draw.ellipse(houseDisplay, (240, 240, 240), (220, 0, 150, 70))
pygame.draw.ellipse(houseDisplay, (255, 255, 250 ), (220, 20, 150, 70))
pygame.draw.ellipse(houseDisplay, (245, 245, 245), (200, 0, 130, 70))
pygame.draw.ellipse(houseDisplay, (245, 245, 245), (300, 0, 130, 70))
pygame.draw.ellipse(houseDisplay, (255, 255, 250 ), (320, 20, 150, 70))
pygame.draw.ellipse(houseDisplay, (240, 240, 240), (320, 0, 150, 70))

# polygons displaying the roof
pygame.draw.polygon(houseDisplay, green, [(150, 50), (50, 150), (250, 150)])
pygame.draw.polygon(houseDisplay, dark_green, [(150, 50), (250, 150), (400, 125), (280, 50)])

# main part of the house (floors)
pygame.draw.polygon(houseDisplay, dark_blue, [(250, 150), (250, 350), (400, 325), (400, 125)])
pygame.draw.rect(houseDisplay, blue, (50, 150, 200, 200))

# the ground
pygame.draw.rect(houseDisplay, green, (0, 350, 900, 1))
pygame.draw.rect(houseDisplay, (105, 105, 105), (0, 350, 900, 500))
pygame.draw.rect(houseDisplay, (200, 200, 200), (0,385,800,80))

#windows
pygame.draw.rect(houseDisplay, (234, 123, 87), (70, 170, 180, 60))

#chimney
pygame.draw.polygon(houseDisplay, dark_brown, [(300, 50), (300, 115), (320, 120),(320, 50)])
pygame.draw.polygon(houseDisplay, (80, 30, 0), [(320, 50), (320, 120), (330, 115)])

#door
pygame.draw.rect(houseDisplay, brown, (55, 260, 30, 70))

#door knob
pygame.draw.ellipse(houseDisplay, red, (80, 295, 5, 5))

# the grass
pygame.draw.polygon(houseDisplay, dark_green, [(250, 350), (400, 325), (500, 325), (500, 350)])

#bushes
pygame.draw.ellipse(houseDisplay, (0,128,0), (90, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (50,205,50), (70, 300, 50, 53))
pygame.draw.ellipse(houseDisplay, (34,139,34), (50, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (50,205,50), (130, 300, 50, 53))
pygame.draw.ellipse(houseDisplay, (0,128,0), (110, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (34,139,34), (150, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (34,139,34), (170, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (0,128,0), (210, 300, 50, 50))
pygame.draw.ellipse(houseDisplay, (50,205,50), (190, 300, 50, 53))
pygame.draw.polygon(houseDisplay, green, [(0, 325),(0, 350), (250, 350), (400, 325), (250, 340)])

# tree
pygame.draw.rect(houseDisplay, brown, (450, 125, 20, 200))
pygame.draw.ellipse(houseDisplay, (0,128,0), (410, 110, 50, 50))
pygame.draw.ellipse(houseDisplay, (50,205,50), (430, 110, 50, 53))
pygame.draw.ellipse(houseDisplay, green, (455, 110, 50, 53))
pygame.draw.ellipse(houseDisplay, green, (410, 120, 50, 53))
pygame.draw.ellipse(houseDisplay, lime_green, (430, 90, 50, 53))
pygame.draw.ellipse(houseDisplay, green, (410, 83, 50, 53))
pygame.draw.ellipse(houseDisplay, green, (440, 83, 50, 53))
pygame.draw.ellipse(houseDisplay, lime_green, (425, 100, 50, 50))
pygame.draw.ellipse(houseDisplay, (50,205,50), (440, 120, 50, 53))

pygame.display.update()

pygame.time.delay(3000)

pygame.image.save(houseDisplay, "house_zakaria.bmp")

pygame.display.quit()