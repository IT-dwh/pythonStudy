import random
from constants import *


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """

    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        self.rect.y += self.speed

    def kill(self) -> None:
        pass


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./../images/background.png")
        if is_alt:
            self.rect.y = -SCREEN_RECT.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy_Plane(GameSprite):

    def __init__(self):
        super().__init__("./../images/enemy1.png", random.randint(2, 5))
        self.rect.y = 0 - self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Main_Plane(GameSprite):

    def __init__(self):
        super().__init__("./../images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        if self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        self.rect.x += self.speed

    def fire(self):
        bullet = Bullet()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top - 2
        self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./../images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()
