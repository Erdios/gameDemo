import pygame,sys
import os
import func
import threading
import VoiceRec

pygame.init()
WHITE = (255, 255, 255)
#variables







#frame
fps=300 #the refresh times per second
fclock = pygame.time.Clock()#control time

#create a window for video game using pygame
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game Demo")

#load images and create a frame for them
hand,handRect,monster,monsterRect,\
weapon,weaponRect,lightening,lighteningRect,\
background,backgroundRect,monster_position,\
hand_position,weapon_position,lightening_position = func.LoadImage()


#attack functions
def Attack(time,Rect,attackType):
    global monster_healthPoint,handRect
    if time>0 and time<5:
        handRect.x = handRect.width*attackType
        Rect.x = Rect.width
        monster_healthPoint-=10*attackType
        time+=1
    elif time>=5 and time<11:
        Rect.x = Rect.width*2
        time+=1
    elif time>=10:
        time=0
        handRect.x=0
        Rect.x=0
        VoiceRec.resultInit()
    return time,Rect



#monster walk to player


    
    
    








#multiple thread for recording voice
thread_voice = threading.Thread(target=VoiceRec.VoiceRec)
thread_voice.start()

#loop for the game (the core of the game)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            VoiceRec.stop()
            thread_voice.join()
            sys.exit()
        
    result = VoiceRec.result
    if "A" in result or "a" in result and check_if_attack2==0 and check_if_attack==0:
        check_if_attack=1
        VoiceRec.resultInit()
            
    elif "Fire" in result or "fire" in result and check_if_attack==0 and check_if_attack2==0:
        check_if_attack2 = 1  
        VoiceRec.resultInit()


    check_if_attack,weaponRect = Attack(check_if_attack,weaponRect,1)
    check_if_attack2,lighteningRect = Attack(check_if_attack2,lighteningRect,2)
    check_if_monster_walk = monsterWalk(check_if_monster_walk)
    
    text = ""








        
    
    
    screen.blit(background,(0,0),backgroundRect)
    screen.blit(monster,(monster_position[0],monster_position[1]),monsterRect)
    screen.blit(weapon,(weapon_position[0],weapon_position[1]),weaponRect)
    screen.blit(lightening,(lightening_position[0],lightening_position[1]),lighteningRect)
    screen.blit(hand,(hand_position[0],hand_position[1]),handRect)
    
    pygame.font.init()
    myfont = pygame.font.Font(None,60)
    textImage = myfont.render("Monster Health:"+str(monster_healthPoint), True, WHITE)
    textImage2 = myfont.render(text, True, WHITE)
    screen.blit(textImage,(0,0))
    screen.blit(textImage2,(width//2-20,height//2-10))

    pygame.display.update()
    
    fclock.tick(fps)

