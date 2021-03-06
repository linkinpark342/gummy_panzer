from __future__ import division
#notes on Background Carnage:
#Must code for building damage and collapsing
#code for little animations in the background?  Or am I just coding buildings here?

#notes on sound-
#Enemy A:  Move Sound, Attack Sound, Fall Sound, Die Sound
#Enemy B:  Move Sound, Attack Sound, Fall Sound, Die Sound
#Enemy C:  Move Sound, Attack Sound, Fall Sound, Die Sound

#Boss:  Move Sound, Attack Sound A, B, C, Fall Sound, Die Sound

import pygame
import random
import logging
from gummy_panzer import settings
from gummy_panzer.sprites import effects, util
#+= settings.SCROLL_RATE

LOG = logging.getLogger(__name__)

BUILDING_IMAGES = None
BUILDING_SIZE_SCALE = 1

#Building:  Damage Sound, Fall Sound, Die Sound
#Player:  Move Sound, Attack Sound A, B C, Fall Sound, Die Sound
class Building(pygame.sprite.Sprite):
    def __init__(self, lev,start = False, *groups):
        global BUILDING_IMAGES
        if BUILDING_IMAGES is None:
            BUILDING_IMAGES = map(util.load_image, ("building1_%d.png" % x for x in xrange(1, 5)))
            BUILDING_IMAGES.extend(map(util.load_image,
                ("building2_%d.png" % x for x in xrange(1,4))))
        #Fallspeed is the number of pixels the building falls each incriment when it is being destroyed
        #Image is the location of the building spritesheet.  Carnageimage is the dust when the building collapses
        #Height should be 0 for below the street, 2 for above the street, 1 for on the street (1 should not be used)
        #state is 0 for whole, 1 for damaged, 2 for destroyed.
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = random.choice(BUILDING_IMAGES)
        #self.wavex=0    #X position in the wave
        self.level=lev  #Level 0 for below street, 1 for above street
        self.fallspeed=1#How many pixels it falls each loop.
        
        self._layer = random.randint(-10, 10)
        self.rect = self.image.get_rect()
        
        ratio =random.randint(6,12)/10#((self.level * BUILDING_SIZE_SCALE) + 1 - (self._layer / 20))

        self.rect.width *= ratio
        self.rect.height *= ratio
        
        self.image = pygame.transform.scale(self.image, self.rect.size)
        height = self.rect.height
        self.rect = self.image.get_rect()
        if start:
            x = random.randint(0,1000)
            if self.level==0:      
                self.rect.topleft=(x, 615 - height)
            elif self.level==1:
                self.rect.topleft=(x, 540 - height)
        else:
            if self.level==0:
                self.rect.topleft=(1000, 615 - height)
            elif self.level==1:
                self.rect.topleft=(1000, 540 - height)

        self._layer = random.randint(-10, 10)
        self.rect.top += self._layer
        self.draw_area = pygame.Rect((0,0), self.rect.size)


        self.BUILDING_TICKS = 0

        self.being_destroyed = False
        self.state=0    #State of the building.  0 intact, 1 damaged, 2 destroyed.
        
        
   # def draw(self, surface):
        #note that when state changes it will make the building sprite change(in this case move over 50 pixels)
    #    if self.alive ==2:
     #       screen.blit(self.image, self.rect, pygame.Rect(50*(self.state), 0, 50, 50))  # change this
        #loop over all enemies,  checking fallers against ground height.  Set enemy to explode, add effects, and all buildings, check if it's in the blast radius.

    def update(self):
        if self.level == 0:
            self.rect.left+= settings.SCROLL_RATE
            self.BUILDING_TICKS += 1
            if self.BUILDING_TICKS == 5:
                self.rect.left -= 1
                self.BUILDING_TICKS = 0
        if self.level == 1:
            self.rect.left+= settings.SCROLL_RATE
            
        if self.being_destroyed:
            LOG.info("draw_area.height: %d" % self.draw_area.height)
            LOG.info("rect.y: %d" % self.rect.y)
            self.draw_area.height -= 6
            self.rect.y += 6
            if self.draw_area.height <= 0:
                self.kill()

        #    self.state+=1
         #   if self.state ==2:
        #        self.alive=2
        #if self.alive==2:
         #   self.rect.move_ip(0,fallspeed)
         #   height-=1
         #               if height==0:
          #                  self.alive=0
                
            
            
        #INTACT STATE: 0
        #DAMAGED STATE: 1
        #DESTROYED STATE: 2
        #If state is intact display sprite is 1
        #If state is damaged display sprite is 2
        #If state is Destroyed display sprite is 3
        #If building takes 1 damage, change sprite
