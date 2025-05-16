from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, rect_x, rect_y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (42, 42))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

lost = 0
font.init()
font1 = font.Font(None, 36)



class Enemy(GameSprite):
   
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 420)
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()




bullets = sprite.Group()

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy('zombie.png', randint(1,3), randint(80,420), 100)
    monsters.add(monster)

class Player(GameSprite):
    global lost
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', 10, self.rect.centerx, self.rect.top)
        bullets.add(bullet)





player = Player('raketa.png', 15, 200, 440)

a = 700
b = 500
background = transform.scale(image.load ('kruto.jpeg'), (a, b))

game = True

window = display.set_mode((700, 500)) 


mixer.init()
mixer.music.load('sneg.mp3')
mixer.music.play()

while game:
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
        if not finish:
    for s in sprite_group:
        score += 1
        monster = Enemy
        monsters_add(monster)

    sprite
    window.blit(background, (0, 0))
    player.reset()
    player.update()
    text_lose = font1.render("Пропущено:" + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (1, 1))


    monsters.draw(window)
    monsters.update()    
    bullets.update()
    bullets.draw(window)
    monster.update()
    display.update()
