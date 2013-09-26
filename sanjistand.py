import pygame
class Sanji(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('sanjisinfondo.png')
        self.sheet.set_clip(pygame.Rect(0, 30, 56, 70))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.x_velocity=0
        self.max_speed=10
        self.y_velocity=0
        self.jump_speed=20
        self.jumping=False

        
        self.frame = 0

        self.rightstand_states={ 0:(14,33,36,60),
                                 1:(48,33,36,60),
                                 2:(83,33,36,60),
                                 3:(120,33,36,60)}
        
        self.leftstand_states={ 0:(180,33,36,60),
                                1:(223,33,36,60),
                                2:(260,33,36,60),
                                3:(295,33,36,60)}
        
        self.left_states = { 0: (459, 115, 60, 60),
                             1: (520, 115, 60, 60),
                             2: (579, 115, 60, 60),
                             3: (632, 115, 53, 60),
                             4: (675, 115, 60, 60),
                             5: (730, 115, 60, 60),
                             6: (785, 115, 60, 60),
                             7: (840, 115, 50, 60) }
        
        self.right_states = { 0: (5, 115, 60, 60),
                              1: (58, 115, 60, 60),
                              2: (117, 115, 60, 60),
                              3: (165, 115, 60, 60),
                              4: (213, 115, 60, 60),
                              5: (274,  115, 60, 60),
                              6: (335, 115, 60, 60),
                              7: (386, 115, 60, 60)}
        
        self.attackright_states={0:(15,575,34,67),
                                 1:(51,575,53,67),
                                 2:(104,575,53,67),
                                 3:(158,575,80,67),
                                 4:(237,575,80,67),
                                 5:(330,575,80,67),
                                 6:(428,575,80,67),
                                 7:(515,575,80,67),
                                 8:(604,575,80,67),
                                 9:(686,575,60,67),
                                 10:(740,575,60,67),
                                 11:(790,575,60,67)}
        
        self.attackleft_states={0:(15,670,34,67),
                                1:(65,670,53,67),
                                2:(128,670,53,67),
                                3:(190,670,80,67),
                                4:(275,665,80,67),
                                5:(365,665,80,67),
                                6:(461,665,80,67),
                                7:(561,665,80,67),
                                8:(665,659,80,70),
                                9:(745,660,50,70),
                                10:(785,660,50,70),
                                11:(830,660,50,70)}
        
        self.win_states={0:(20,4495,43,90),
                         1:(70,4495,43,90),
                         2:(125,4495,43,90),
                         3:(170,4495,43,90),
                         4:(220,4495,43,90),
                         5:(273,4495,43,90),
                         #
                         6:(329,4495,43,90),
                         #
                         7:(125,4495,43,90),
                         8:(170,4495,43,90),
                         9:(220,4495,43,90),
                         10:(273,4495,43,90),
                         #
                         11:(385,4495,46,80),
                         #
                         12:(125,4495,43,90),
                         13:(170,4495,43,90),
                         14:(220,4495,43,90),
                         15:(273,4495,43,90),
                         #
                         16:(443,4495,43,90),
                         #
                         17:(125,4495,43,90),
                         18:(170,4495,43,90),
                         19:(220,4495,43,90),
                         20:(273,4495,43,90),
                         #
                         21:(506,4495,43,90),
                         22:(555,4495,43,90),
                         23:(595,4495,43,90)}
        
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


    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 10

        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 10
  
        if direction == 'stand_left':
            self.clip(self.leftstand_states)
            
        if direction == 'stand_right':
            self.clip(self.rightstand_states)

        if direction=='attackright':
            self.clip(self.attackright_states)
            self.rect.x-=5
        if direction=='attackleft':
            self.clip(self.attackleft_states)
            self.rect.x+=5
        if direction=='win':
            self.clip(self.win_states)
            if self.frame==7 or self.frame==12 or self.frame==17 or self.frame==22:
                pygame.time.delay(100)
        if self.rect.x>330:
            self.rect.x=330
        if self.rect.x<0:
            self.rect.x=0

 
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 

    def handle_event(self, event):
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        while pygame.event.get(): pass
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            

            if key[pygame.K_a]:
                self.update('left')
            if key[pygame.K_a] and key[pygame.K_e]:
                self.update('attackleft')
            if key[pygame.K_d]:
                self.update('right')
            if key[pygame.K_d] and key[pygame.K_e]:
                self.update('attackright')
            if key[pygame.K_r]:
                self.update('win')
            if key[pygame.K_g]:
                self.update('jump')


                    
            

 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_a or  event.key==pygame.K_q:
                self.update('stand_left')            
            if event.key == pygame.K_d or event.key==pygame.K_e or event.key==pygame.K_r:
                self.update('stand_right')


