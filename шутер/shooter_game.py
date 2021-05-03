#Создай собственный Шутер!

from pygame import *
from random import randint
font.init()
mixer.init()

#classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y,player_speed):
        super().__init__()

        #images
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed

        #rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#player class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 20, 20, 5)
        bullets.add(bullet)


#enemy class
miss = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 1000:
            self.rect.x = randint(10, 620)
            self.rect.y = -65

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()
    #install gamed
#view
window = display.set_mode((700, 900))
display.set_caption("Межгалактические войны")
background = transform.scale(image.load('galaxy.jpg'), (700, 900))
#переменные
score = 0
finish = False
#music
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

#spites
player = Player("rocket.png", 0, 815, 100, 100, 3)

monsters = sprite.Group()
for i in range (5):
    monster = Enemy('ufo.png', randint(10, 320), -65, 100, 100,randint(2, 5))
    monsters.add(monster)

bullets = sprite.Group()


#time|FPS
FPS = 60
clock = time.Clock()

#game functional
game = True
font1 = font.Font(None, 100)
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if miss == 3:
        finish = True

    if finish == False:
        window.blit(background, (0, 0))

        player.update()
        player.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for collide in collides:
            monster = Enemy('ufo.png', randint(10, 320), -65, 100, 100,randint(2, 5))
            monsters.add(monster)
            score += 1
            
        if sprite.spritecollide(player, monsters, False, False):
            finish = True
            text_lose = font1.render('LOSER', 1, (255, 255, 200))
            window.blit(text_lose, (10, 50))

    display.update()
    clock.tick(FPS)