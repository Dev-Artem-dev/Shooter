from pygame import *
from random import randint
font.init()

#classes
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)

       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
   def fire(self):
       pass

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(0,620)
            self.rect.y = 0
            lost +=1
        #if lost == 5:################################################v
           # pass
class Bullet(GameSprite):
    def update(self):
        

#переменные
lost = 0
score = 0

#bullets = sprite.Group()#############################################################################
#bullets.add(bullet)###################################################

monsters = sprite.Group()
for i in range (5):
    monster = Enemy('ufo.png', 0,  randint(10, 320), 65, 10, randint(2, 5))
    monsters.add(monster)



font1  = font.Font(None, 36)
finish = False

#music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

#window
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

#sprites
ship = Player("rocket.png", 5, win_height - 100, 80, 100, 10)
#bullet = Bullet('bullet.png', self.rect.center.x, self.rect.top, 10, 15, 7)##########################

#game cycle
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
        elif 2.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

   if not finish:
       window.blit(background,(0,0))

       text_lose = font1.render('Missed: ' + str(lost), 1, (255, 255, 200))
       text_score = font1.render('Score: ' + str(lost), 1, (255, 255, 200))

       window.blit(text_lose, (10, 10))
       window.blit(text_score, (10, 10))

       ship.update()
       ship.reset()

       monsters.update()
       monsters.draw(window)
       bullet.update()###################################################################
       bullet.draw(window)######################################################

       display.update()

   time.delay(50)