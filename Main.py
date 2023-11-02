import os, ProgramList

os.system("pip install pygame") # needed to run the program 


import pygame
from pygame import Rect
from time import sleep

class button:
    def __init__(self, buttonpos:Rect) -> None:
        self.buttonpos = buttonpos
        self.iconrec = buttonpos
        self.isclickeddown = False      
        self.clickpoint = (-1,-1)  

        self.iconrecup = (self.iconrec.x, self.iconrec.y - 10)
    def clickcheck(self, leftmouseup, leftmousedown, action, input, icon):
        if  self.buttonpos.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(display,(89, 60, 143),self.buttonpos)
                self.iconrec = self.buttonpos
                self.clickpoint = pygame.mouse.get_pos()
                if leftmousedown:
                    self.isclickeddown = True
            else:
                self.iconrec = self.iconrecup
                pygame.draw.rect(display,(240, 188, 212),self.buttonpos)
        else:
            self.iconrec = self.buttonpos
            pygame.draw.rect(display,(17, 181, 228),self.buttonpos)
        
        if leftmouseup:
            if self.buttonpos.collidepoint(self.clickpoint):
                if self.buttonpos.collidepoint(pygame.mouse.get_pos()):
                    if input != None and self.isclickeddown:
                        action(input)
                        sleep(.5)
                        self.clickpoint = (-1,-1)
                        self.isclickeddown = False
                
        if icon != None:
            display.blit(icon, self.iconrec)
        

def InitImage(images:str, buttonsize):
    return pygame.transform.scale(pygame.image.load(images), (buttonsize,buttonsize))
def runscript(scriptname:str):
    if scriptname != None:
        os.system(f"start {scriptname}")
def getlow(i:int, j:int):
    if i >= j:
        return j
    else:
        return i
def gethigh(i:int, j:int):
    if i <= j:
        return j
    else:
        return i

pygame.init()
pygame.display.set_caption('util')
pygame.display.set_icon(InitImage('utilicon.png', 100))

displaysize = w, h = (1280, 720)


display = pygame.display.set_mode(displaysize)
clock = pygame.time.Clock()


def Input(key:str):
    return pygame.key.get_pressed()[pygame.key.key_code(key)]



allbutton = []
def grid(gridx, gridy, buttonsize, fill, holeX, holeY):
    for y in range(gridy):
        for x in range(gridx):
            allbutton.append(button(Rect((x * (buttonsize + fill)) + holeX, (y * (buttonsize + fill)) + holeY, buttonsize, buttonsize)))

gridx = 4
gridy = 4


buttonsize = (250 * 2 /(getlow(gridx, gridy)))


fill = 20 
holeX = (w - (gridx * (buttonsize + fill)))/2
holeY = (h - (gridy * (buttonsize + fill)))/2


grid(gridx, gridy, buttonsize, fill, holeX, holeY)


scriptlist = []

for i in range(len(ProgramList.scriptlist)):
    scriptlist.append([ProgramList.scriptlist[i][0], InitImage(ProgramList.scriptlist[i][1], buttonsize)])








leftmouseup = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            leftmouseup = True
        else:
            leftmouseup = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            leftmousedown = True
        else:
            leftmousedown = False
    if Input("escape"):
        done = True 
    pygame.draw.rect(display,(165, 204, 209),(0,0,w,h))

    for b in range(len(allbutton)):
        try:
            scriptlist[b][0]
            scriptlist[b][1]
        except:
            # pygame.draw.rect(display,(12, 202, 74),allbutton[b].buttonpos)
            allbutton[b].clickcheck(leftmouseup, leftmousedown, runscript,None,InitImage("utilicon.png", buttonsize))
            continue
        allbutton[b].clickcheck(leftmouseup, leftmousedown, runscript,scriptlist[b][0],scriptlist[b][1])

    clock.tick(60)
    pygame.display.update()

pygame.quit()
os._exit(0)