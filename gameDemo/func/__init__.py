import pygame,sys
import os

#path of the game folder
path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
width, height= 1200,800

#useful function
#create frames for the animation
def CreateFrame(file,FrameNumber):
    Rect = file.get_rect()
    Rect.width = Rect.width//FrameNumber
    return Rect

def LoadImage():
    #1.load hand
    hand = pygame.image.load(path+"/image/hand.png")
    handRect = CreateFrame(hand,3)
    #2.load monster
    monster = pygame.image.load(path+"/image/monster.png")
    monsterRect = CreateFrame(monster,1)
    #3.load weapon
    weapon = pygame.image.load(path+"/image/weapon.png")
    weaponRect = CreateFrame(weapon,3)
    lightening = pygame.image.load(path+"/image/lightening.png")
    lighteningRect = CreateFrame(lightening,3)
    #4.background
    background = pygame.image.load(path+"/image/background.png")
    backgroundRect = CreateFrame(background,1)
    
    monster_position = [width//2-monsterRect.width//2,height//2-monsterRect.height//2]
    hand_position =[width-handRect.width,height-handRect.height]
    weapon_position=[(width-weaponRect.width)//2,(height-weaponRect.height)//2]
    lightening_position = [(width-lighteningRect.width)//2,(height-lighteningRect.height)//4]
    
    
    return hand,handRect,monster,monsterRect,weapon,weaponRect,lightening,lighteningRect,background,backgroundRect,monster_position,hand_position,weapon_position,lightening_position

#def LoadPosition():
    