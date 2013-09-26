import pygame
class Zoro(pygame.sprite.Sprite):
    def __init__(self,position):
        self.sheet=pygame.image.load('Zorosinfondo.png')
        self.sheet.set_clip(pygame.Rect((8,0,43,95)))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0

        self.rightstand_states={0:(8,0,43,95),
                                1:(55,0,43,95),
                                2:(105,0,43,95),
                                3:(155,0,43,95)}
        
        self.leftstand_states={0:(8,86,43,95),
                               1:(56,86,43,95),
                               2:(105,86,43,95),
                               3:(155,86,43,95)}
        
        self.runright_states={0:(240,0,60,95),
                             1:(300,0,60,95),
                             2:(360,0,60,95),
                             3:(420,0,60,95),
                             4:(480,0,60,95),
                             5:(540,0,60,95),
                             6:(605,0,60,95),
                             7:(670,0,60,95)}
        
        self.runleft_states={0:(240,86,60,95),
                             1:(300,86,60,95),
                             2:(360,86,60,95),
                             3:(420,86,60,95),
                             4:(480,86,60,95),
                             5:(540,86,60,95),
                             6:(607,86,60,95),
                             7:(670,86,60,95)}
        
        self.attackright_states={0:(5,175,60,95),
                                 1:(70,175,60,95),
                                 2:(135,175,60,95),
                                 3:(195,175,90,95),
                                 4:(290,175,90,95),
                                 5:(385,175,90,95),
                                 6:(480,175,90,95),
                                 7:(570,175,60,95),
                                 8:(630,175,60,95)}
        
        self.attackleft_states={0:(5,265,60,95),
                               1:(70,265,60,95),
                               2:(135,265,60,95),
                               3:(195,265,90,95),
                               4:(290,265,90,95),
                               5:(385,265,90,95),
                               6:(480,265,90,95),
                               7:(570,265,60,95),
                               8:(630,265,60,95)}
        

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       

    def update(self,direction):
        if direction=='stand_right':
            self.clip(self.rightstand_states)
        if direction=='stand_left':
            self.clip(self.leftstand_states)
        if direction=='run_right':
            self.rect.x+=10
            self.clip(self.runright_states)
        if direction=='run_left':
            self.rect.x-=10
            self.clip(self.runleft_states)
        if direction=='attack_right':
            self.rect.x-=5
            self.clip(self.attackright_states)
        if direction=='attack_left':
            self.rect.x+=5
            self.clip(self.attackleft_states)

        if self.rect.x>330:
            self.rect.x=330
        if self.rect.x<0:
            self.rect.x=0

        self.image=self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,event):
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        while pygame.event.get(): pass
        key = pygame.key.get_pressed()
        if event.type==pygame.QUIT:
            game_over= True
        if event.type==pygame.KEYDOWN:
            if key[pygame.K_RIGHT]:
                self.update('run_right')
            if key[pygame.K_RIGHT] and key[pygame.K_l]:
                self.update('attack_right')            
            if key[pygame.K_LEFT]:
                self.update('run_left')
            if key[pygame.K_LEFT] and key[pygame.K_l]:
                self.update('attack_left')
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_l:
                self.update('stand_right')
            if event.key==pygame.K_LEFT:
                self.update('stand_left')
