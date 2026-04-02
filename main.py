import  pygame
import random



WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PAQUETA CRISPS")
run=True


bg1=pygame.image.load(r"spritesinpygame\rocket.png")
bg2=pygame.image.load(r"rocketinspace\background.png")

class Rocket(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

rocket=Rocket(bg1,300,300)
spritegroup=pygame.sprite.Group()
spritegroup.add(rocket)

       

        

while run == True:
    screen.blit(bg2,(0,0))
    spritegroup.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False 

    keypressed=pygame.key.get_pressed()
    if keypressed[pygame.K_w]:
        rocket.rect.y=rocket.rect.y-2
    if keypressed[pygame.K_s]:
        rocket.rect.y=rocket.rect.y+2
    if keypressed[pygame.K_a]:
        rocket.rect.x=rocket.rect.x-2
    if keypressed[pygame.K_d]:
        rocket.rect.x=rocket.rect.x+2
    
    if rocket.rect.x>=450:
        rocket.rect.x=450
    if rocket.rect.y>=381:
        rocket.rect.y=381
    if rocket.rect.x<=0:
        rocket.rect.x=0
    if rocket.rect.y<=0:
        rocket.rect.y=0
    





    

        































    pygame.display.update()