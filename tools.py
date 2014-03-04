import pygame
from lib import tmx
from pygame import rect as rect
from pygame.locals import *


class Tools(pygame.sprite.Sprite):
    def __init__(self, game, player, name):
        super(Tools, self).__init__()
        self.game = game
        self.name = name
        self.player = player
        self.visible = False
        self.hub = self.__followPlayer__()
        self.rect_aff = Rect((self.hub[0], self.hub[1]+8), (5, 100))

    def draw(self, screen):
        print self.visible
        pygame.draw.rect(screen, (140,240,130), self.rect_aff)

    def definir_position(self, x, y):
        self.rect_aff.x = x
        self.rect_aff.y = y

    def update(self, dt, *args):
        self.hub = self.__followPlayer__()
        self.rect_aff = Rect((self.hub[0], self.hub[1]+8), (5, 100))

    #overide
    def set_view(self, *args):
        pass

    def __followPlayer__(self):
        #Centrer la position du HUD par rapport au personnage
        playerx, playery = self.player.collision_rect.x, self.player.collision_rect.y
        hubx = playerx - (playerx - (self.game.screen.get_width() / 2))
        huby = playery - (playery - (self.game.screen.get_height() / 2))

        if playerx < hubx:
            hubx = playerx

        if playery < huby:
            huby = playery

        centerx = self.game.tilemap.px_width - self.game.screen.get_width() / 2
        centery = self.game.tilemap.px_height - self.game.screen.get_height() / 2

        if playerx > centerx:
            hubx += playerx - centerx

        if playery > centery:
            huby += playery - centery
            hubx += self.game.tilemap.tile_width / 2
            huby += self.game.tilemap.tile_height / 2

        return hubx,huby
