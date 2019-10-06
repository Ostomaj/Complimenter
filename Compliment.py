import random
import sys, pygame
from pygame.locals import *
import time
pygame.init()
info=pygame.display.Info()
#Create the screen
display_w=info.current_w-100
display_h=info.current_h-100
screen = pygame.display.set_mode((display_w,display_h),pygame.RESIZABLE)

#Caption the icon
pygame.display.set_caption("Complimenter")
icon=pygame.image.load("TU.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("Compliment.jpg")
bg= pygame.transform.scale(bg, (display_w,display_h))
smile = pygame.image.load("Smile.jpg")

def text_objects(text,font):
    textSurface=font.render(text,True,(0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',38)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center= ((display_w/2),(display_h/2.5))
    screen.blit(TextSurf,TextRect)

def generating_text(text):
    largeText = pygame.font.Font('freesansbold.ttf',85)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center= ((display_w/2),(display_h/2.5))
    screen.blit(TextSurf,TextRect)    

def smiley():
    x=display_w/2.5
    y=display_h/4.3
    screen.blit(smile, (x,y))

def pick():
    L = ["You Are The Most Perfect You There Is", "You Should Be Proud Of Yourself",
     "You’re Really Something Special","You’re More Fun Than A Ball Pit Filled With Candy",
     "You’re More Fun Than Bubble Wrap","You Are Making A Difference","You’re A Gift To Those Around You",
     "Everything Would Be Better If More People Were Like You!", "You Were Cool Way Before Hipsters Were Cool.",
     "You’re Smarter Than Google And Mary Poppins Combined."]
    r=random.randint(0,9)
    message_display(L[r])
    

def main():
    p=1
    clicks=0
    while p==1:
        mouse=pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if clicks == 0:
            screen.blit(bg,(0,0))
            pygame.display.update()
        else:
            pygame.display.update()

        if 1065>mouse[0]>222 and 541>mouse[1]>432 and click[0] == 1 != None:
            screen.blit(bg,(0,0))
            start = time.time()

            if time.time()-start<1:
                screen.blit(bg,(0,0))
                generating_text("Generating Compliment....")
                time.sleep(1)
                pygame.display.update()

            if time.time()-start<2:
                screen.blit(bg,(0,0))
                generating_text("Generating Compliment...")
                time.sleep(1)
                pygame.display.update()

            if time.time()-start<3:
                screen.blit(bg,(0,0))
                generating_text("Generating Compliment..")
                time.sleep(1)
                pygame.display.update()

            if time.time()-start<4:
                screen.blit(bg,(0,0))
                generating_text("Generating Compliment.")
                time.sleep(1)
                pygame.display.update()

            if time.time()-start<5:
                screen.blit(bg,(0,0))
                smiley()
                time.sleep(1)
                pygame.display.update()
            
            if time.time()-start>3:
               screen.blit(bg,(0,0))
               pick()
               clicks+=1
               print(clicks)
               time.sleep(2)
           

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            pygame.display.update()
if __name__=='__main__':
    main()
