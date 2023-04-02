from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.task import *

from player import *
from mapmanager import *


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.camLens.setFov(90)
        self.manager = Mapmanager()
        self.load_map()
        self.manager.addBlock((3, 3, 2))
        base.accept('m', self.save_map)
        base.accept('l', self.load_map)
        base.accept('f', self.buildblock)
        base.accept('e', self.destroyblock)

        self.disableMouse()
        wp = WindowProperties()
        wp.setSize(1200, 800)
        wp.setMouseMode(WindowProperties.M_absolute)
        wp.setCursorHidden(True)
        self.win.requestProperties(wp)

        self.player = Hero(self.manager.map)
        self.mouseTask = taskMgr.add(self.mouseTask)

    def buildblock(self):
        if self.manager.on_ground(self.player.model.getPos()):
            a = radians(self.player.model.getH())
            dx = sin(a) * 2
            dy = cos(a) * 2
            x = round(self.player.model.getX() - dx)
            y = round(self.player.model.getY() + dy)
            point = (x, y, self.player.model.getZ())
            self.manager.addBlock(point)

    def destroyblock(self):
        a = radians(self.player.model.getH())
        dx = sin(a) * 2
        dy = cos(a) * 2
        x = round(self.player.model.getX() - dx)
        y = round(self.player.model.getY() + dy)
        point = (x, y, self.player.model.getZ())
        for block in self.manager.map:
            if self.check_collide(block, point):
                self.manager.map.remove(block)
                block.removeNode()

    def check_collide(self, block, position):
        x, y, z = position
        xb, yb, zb = block.getPos()
        if xb-1 <= x <= xb+1:
            if yb-1 <= y <= yb+1:
                if zb-1 <= z <= zb+1:
                    return True
        return False


    def save_map(self):
        with open('map.txt', 'w') as file:
            for block in self.manager.map:
                result = str(block.getX()) + ' ' + \
                    str(block.getY()) + ' ' + str(block.getZ()) + '\n'
                file.write(result)

    def load_map(self):
        with open('map.txt', 'r') as file:
            map = file.readlines()
        for block in map:
            block = block.split()
            self.manager.addBlock(
                (float(block[0]), float(block[1]), float(block[2])))

    def mouseTask(self, task):
        mw = base.mouseWatcherNode
        if mw.hasMouse():
            x = mw.getMouseX()
            y = mw.getMouseY()
            self.player.model.setH(self.player.model.getH() - x*50)
            self.player.model.setP(self.player.model.getP() + y*50)
            base.win.movePointer(0, 600, 400)
        if not self.manager.on_ground(self.player.model.getPos()):
            self.player.falling_speed -= 0.01
        else:
            self.player.falling_speed = 0
        self.player.model.setZ(self.player.model.getZ() + self.player.falling_speed)
        return Task.cont


game = Game()
game.run()
