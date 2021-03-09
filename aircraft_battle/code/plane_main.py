from plane_sprites import *
from constants import *


class PlaneGame(object):
    def __init__(self):
        print("game init")
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_PLANE, 1000)
        pygame.time.set_timer(FIRE_BULLET, 500)

    def __create_sprites(self):
        bg1 = Background(False)
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_plane_group = pygame.sprite.Group()

        self.main_plane = Main_Plane()
        self.main_plane_group = pygame.sprite.Group(self.main_plane)

    def start_game(self):
        print("start game")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_PLANE:
                enemy_plane = Enemy_Plane()
                self.enemy_plane_group.add(enemy_plane)
            elif event.type == FIRE_BULLET:
                self.main_plane.fire()

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     self.main_plane.fire()
        if keys[pygame.K_RIGHT]:
            self.main_plane.speed = 2
        elif keys[pygame.K_LEFT]:
            self.main_plane.speed = -2
        else:
            self.main_plane.speed = 0

    def __check_collide(self):
        sprite_list = pygame.sprite.groupcollide(self.main_plane.bullet_group, self.enemy_plane_group, True, True)
        for sl in sprite_list:
            sl.kill()

        enemies = pygame.sprite.spritecollide(self.main_plane, self.enemy_plane_group, True)
        if len(enemies) > 0:
            self.main_plane.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_plane_group.update()
        self.enemy_plane_group.draw(self.screen)

        self.main_plane_group.update()
        self.main_plane_group.draw(self.screen)

        self.main_plane.bullet_group.update()
        self.main_plane.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("game over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
