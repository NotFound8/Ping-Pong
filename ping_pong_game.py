import pygame
pygame.init()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed,x1, y1):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 