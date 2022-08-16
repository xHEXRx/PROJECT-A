import pygame
from pygame.locals import *
import sys
import random
import pygame_gui
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
HEIGHT = 500
WIDTH = 1900
FPS = 60
#0 = killer 1 = platform
selection = 0
FramePerSec = pygame.time.Clock()
boyutx = 15
boyuty = 15
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("editor")
manager = pygame_gui.UIManager((500, 1900))
kiilerbut = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 100), (100, 50)),
                                             text='killer',
                                             manager=manager)
platbut = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 151), (100, 50)),
                                             text='platform',
                                             manager=manager)
boyutxsld = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 272), (250, 20)),start_value= 15,value_range=(0,250),manager=manager)
boyutysld = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 293), (250, 20)),start_value= 15,value_range=(0,250),manager=manager)
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,30))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
    def move(self):
        pass
class Killer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((15,15))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (150,150))
    def move(self):
        pass

PT1 = platform()

K1 = Killer()

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((0,255,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
K1.surf = pygame.Surface((WIDTH, 20))
K1.surf.fill((255,0,0))
K1.rect = K1.surf.get_rect(center = (WIDTH/2, HEIGHT/2 -30)) 



all_sprites = pygame.sprite.Group()

platforms = pygame.sprite.Group()
platforms.add(PT1)

killers = pygame.sprite.Group()

all_sprites.add(platforms,killers)
def levelmaker():
    #hovering trueysa yapma
    cursor_position = pygame.mouse.get_pos() 
    ks = Killer()
    pt = platform()
    if selection == 0:
         
        ks.surf = pygame.Surface((boyutx,boyuty))
        ks.surf.fill((255,0,0))
        ks.rect = ks.surf.get_rect(center = (cursor_position))
        killers.add(ks)
    elif selection == 1:
        pt.surf = pygame.Surface((boyutx,boyuty))  
        pt.surf.fill((0,255,30))
        pt.rect = pt.surf.get_rect(center = (cursor_position))
        platforms.add(pt)
    
    print(cursor_position)
    all_sprites.add(killers,platforms)
kilersloc = []
killersboy = []

platformloc = []
platformboy = []
def yaz():
    for kil in killers:
        kilersloc.append(str(kil.rect.center))
        killersboy.append(str(kil.rect.size))
    with open('poskiller.txt', 'w') as f:
        for line in kilersloc:
                f.write(line)
                f.write('\n')
    with open('boykiller.txt', 'w') as f:
        for line in killersboy:
                f.write(line)
                f.write('\n')            
    for plats in platforms:
        platformboy.append(str(plats.rect.size))
        platformloc.append(str(plats.rect.center))
    with open('posplat.txt', 'w') as f:
        for line in platformloc:
                f.write(line)
                f.write('\n')      
    with open('boyplat.txt', 'w') as f:
        for line in platformboy:
                f.write(line)
                f.write('\n')   
def delete():
    cursor_position = pygame.mouse.get_pos() 
    checkersurf = pygame.Surface((15,15))
    checkerrect = checkersurf.get_rect(center = (cursor_position))	   
    for obj in all_sprites:
        if checkerrect.colliderect(obj.rect):
            obj.kill()

while True:
    time_delta =  FramePerSec.tick(FPS)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            yaz()
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                levelmaker()
            elif event.button == 1:
                delete()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == kiilerbut:
                  selection = 0
                elif event.ui_element == platbut:
                  selection = 1
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == boyutxsld:
              boyutx = event.value
            elif event.ui_element == boyutysld:
              boyuty = event.value    
            
        manager.process_events(event)
                  
    manager.update(time_delta)
    
 
    
    displaysurface.fill((0,0,0))
     
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    manager.draw_ui(displaysurface)
    pygame.display.update()
    FramePerSec.tick(FPS) 
 

 

 
 
        
