import pygame
import sanjistand
import zorostand
               
pygame.init()
fondo='JS-OnePiece.png' 
screen = pygame.display.set_mode((388, 200))
pygame.display.set_caption("Python/Pygame Animation")
clock = pygame.time.Clock()
player = sanjistand.Sanji((0, 135))
player2 = zorostand.Zoro((320,110))
def checkcollision(player1,player2):
    col=pygame.sprite.collide_mask(player,player2)
    
    if col!=None:
        print(col)
        return col

 
game_over = False
 
while game_over == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    def mouse(self,event):
        pygame.event.set_blocked(pygame.MOUSEMOTION)
    checkcollision(player,player2)
    
        
    player.handle_event(event)
    player2.handle_event(event)
    background=pygame.image.load(fondo).convert()
    screen.blit(background,(0,0)) 
    screen.blit(player.image, player.rect)
    screen.blit(player2.image,player2.rect) 
    pygame.display.flip()              
    clock.tick(12)
 
pygame.quit ()
