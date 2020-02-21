import pygame as py

py.init()

display_width = 600
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = py.display.set_mode((display_width, display_height))
gameDisplay.fill(white)
py.display.set_caption('Tic Tac Toe')
clock = py.time.Clock()

crashed = False

strtpnt = (0, 0)

frst_secquadpnt = [display_width/3, 0]
frst_frthquadpnt = [0, display_height / 3]
sec_thrdquadpnt = [2 * display_width / 3, 0]
thrd_sxthquadpnt = [display_width, display_height / 3]
frth_svnquadpnt = [0, 2 * display_height / 3]
sxth_ninequadpnt = [display_width, 2 * display_height / 3]
svn_eghtquadpnt = [display_width / 3, display_height]
eght_ninequadpnt = [2 * display_width / 3, display_height]

X = py.image.load(r'./x.png')
O = py.image.load(r'./O.png')

filled1 = False
filled2 = False
filled3 = False
filled4 = False
filled5 = False
filled6 = False
filled7 = False
filled8 = False
filled9 = False
filledx = False

filledquadvals = ["", "", "", "", "", "", "", "", ""]

while not crashed:
    for event in py.event.get():
        py.draw.line(gameDisplay, black, frst_secquadpnt, svn_eghtquadpnt)
        py.draw.line(gameDisplay, black, sec_thrdquadpnt, eght_ninequadpnt)

        py.draw.line(gameDisplay, black, frst_frthquadpnt, thrd_sxthquadpnt)
        py.draw.line(gameDisplay, black, frth_svnquadpnt, sxth_ninequadpnt)
        if event.type == py.MOUSEBUTTONUP and event.type != py.QUIT:
            pos = py.mouse.get_pos()
            image = X
            if not filledx == False:
                image = O
                filledx = False
            elif not filledx == True:
                image = X
                filledx = True
            if pos[0] <= frst_secquadpnt[0] and pos[1] <= frst_frthquadpnt[1] and not filled1 == True:
                gameDisplay.blit(image, strtpnt)
                if image == X:
                    filledquadvals[0] = "X"
                elif image == O:
                    filledquadvals[0] = "O"
                filled1 = True
            elif sec_thrdquadpnt[0] >= pos[0] >= frst_secquadpnt[0] and pos[1] <= frst_frthquadpnt[1] and not filled2 == True:
                gameDisplay.blit(image, frst_secquadpnt)
                if image == X:
                    filledquadvals[1] = "X"
                elif image == O:
                    filledquadvals[1] = "O"
                filled2 = True
            elif pos[0] >= sec_thrdquadpnt[0] and pos[1] <= thrd_sxthquadpnt[1] and not filled3 == True:
                gameDisplay.blit(image, sec_thrdquadpnt)
                if image == X:
                    filledquadvals[2] = "X"
                elif image == O:
                    filledquadvals[2] = "O"
                filled3 = True
            elif frst_frthquadpnt[0] <= pos[0] <= frst_secquadpnt[0] and frst_frthquadpnt[1] <= pos[1] <= frth_svnquadpnt[1] and not filled4 == True:
                gameDisplay.blit(image, frst_frthquadpnt)
                if image == X:
                    filledquadvals[3] = "X"
                elif image == O:
                    filledquadvals[3] = "O"
                filled4 = True
            elif frst_secquadpnt[0] <= pos[0] <= sec_thrdquadpnt[0] and frst_secquadpnt[1] <= pos[1] <= frth_svnquadpnt[1] and not filled5 == True:
                gameDisplay.blit(image, (frst_secquadpnt[0], frst_frthquadpnt[1]))
                if image == X:
                    filledquadvals[4] = "X"
                elif image == O:
                    filledquadvals[4] = "O"
                filled5 = True
            elif sec_thrdquadpnt[0] <= pos[0] <= thrd_sxthquadpnt[0] and frst_frthquadpnt[1] <= pos[1] <= frth_svnquadpnt[1] and not filled6 == True:
                gameDisplay.blit(image, (sec_thrdquadpnt[0], frst_frthquadpnt[1]))
                if image == X:
                    filledquadvals[5] = "X"
                elif image == O:
                    filledquadvals[5] = "O"
                filled6 = True
            elif frth_svnquadpnt[0] <= pos[0] <= svn_eghtquadpnt[0] and frth_svnquadpnt[1] <= pos[1] <= display_height and not filled7 == True:
                gameDisplay.blit(image, frth_svnquadpnt)
                if image == X:
                    filledquadvals[6] = "X"
                elif image == O:
                    filledquadvals[6] = "O"
                filled7 = True
            elif svn_eghtquadpnt[0] <= pos[0] <= eght_ninequadpnt[0] and frth_svnquadpnt[1] <= pos[1] <= display_height and not filled8 == True:
                gameDisplay.blit(image, (svn_eghtquadpnt[0], frth_svnquadpnt[1]))
                if image == X:
                    filledquadvals[7] = "X"
                elif image == O:
                    filledquadvals[7] = "O"
                filled8 = True
            elif eght_ninequadpnt[0] <= pos[0] <= display_width and sxth_ninequadpnt[1] <= pos[1] <= display_height and not filled9 == True:
                gameDisplay.blit(image, (eght_ninequadpnt[0], frth_svnquadpnt[1]))
                if image == X:
                    filledquadvals[8] = "X"
                elif image == O:
                    filledquadvals[8] = "O"
                filled9 = True
        elif event.type == py.QUIT or filled1 and filled2 and filled3 and filled4 and filled5 and filled6 and filled7 and filled8 and filled9:
            crashed = True
    py.display.update()
    clock.tick(6000)
py.quit()
quit()