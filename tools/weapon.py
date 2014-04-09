# -*- coding: utf-8 -*-
#
# Projet5001: un jeu de survie post-apocalyptique
# Copyright (C) 2014  Équipe Projet5001
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pygame
from pygame import Rect
from pygame.locals import *
from eventManager import EventEnum
from basetool import BaseTool



class Weapon(BaseTool):


    def __init__(self, layer_manager, owner, name, size_x, size_y, dmg, obj=None):
        super(Weapon, self).__init__(layer_manager, owner, name, obj)
        self.size = {}
        self.image = None
        self.base_mod = 20
        self.rect = Rect(0, 0, 0, 0)
        self.dommage = dmg
        self.equippable = True
        self.mod_left = self.base_mod
        self.mod_top = self.base_mod
        self.hub = None
        self.init_size(size_x, size_y)

    def init_size(self, size_x, size_y):
        self.size['x'] = size_x
        self.size['y'] = size_y
        self.size['flippe'] = 'v'


    @classmethod
    def is_type_for(cls, object_type):
        return object_type == "weapon"

    def is_equippable(self):
        return self.equippable

    def draw(self, screen):
        if self.visible:
            self.hub = self.__followPlayer__()
            pygame.draw.rect(screen, (140, 240, 130), ((self.hub[0]+self.mod_left,
                                                        self.hub[1]+self.mod_top),
                                                       (self.size['y'], self.size['x'])))

    def update(self, dt, *args):
        self.rect = Rect(0, 0, 0, 0)

    def __update_rect__(self):
            self.rect = Rect((self.player.collision_rect[0]+self.mod_left,
                              self.player.collision_rect[1]+self.mod_top),
                             (self.size['y'], self.size['x']))

    def receive_event(self, event):
        if event.type == EventEnum.MOVE:
            self.update_rect_box_direction(event)
        elif event.type == EventEnum.ATTACK:
            self.__update_rect__()

    def update_rect_box_direction(self, event):
        if event.m == "left":
            if self.size['flippe'] == 'h':
                self.flip_rect_box()
            self.mod_left = self.base_mod - self.size['y']
            self.mod_top = self.base_mod

        elif event.m == "right":
            if self.size['flippe'] == 'h':
                self.flip_rect_box()
            self.mod_left = self.base_mod
            self.mod_top = self.base_mod

        elif event.m == "up":
            if self.size['flippe'] == 'v':
                self.flip_rect_box()
            self.mod_left = self.base_mod
            self.mod_top = self.base_mod - self.size['x']

        elif event.m == "down":
            if self.size['flippe'] == 'v':
                self.flip_rect_box()
            self.mod_left = self.base_mod
            self.mod_top = self.base_mod

    def flip_rect_box(self):
            x = self.size['x']
            y = self.size['y']
            self.size['x'] = y
            self.size['y'] = x
            if self.size['flippe'] == 'h':
                self.size['flippe'] = 'v'
            else:
                self.size['flippe'] = 'h'

    def handle_collision(self):
        pass

