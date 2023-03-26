# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from panda3d.core import WindowProperties
from player import *

from direct.task import *


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.camLens.setFov(90)
        self.manager = Mapmanager()
        self.load_map()
        base.accept('m', self.save_map)
        base.accept('l', self.load_map)

        self.disableMouse()
        wp = WindowProperties()
        wp.setSize(1200, 800)
        wp.setMouseMode(WindowProperties.M_absolute)
        wp.setCursorHidden(True)
        self.win.requestProperties(wp)

        self.player = Hero()
        self.mouseTask = taskMgr.add(self.mouseTask)

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
            self.player.falling_speed += 0.001
            self.player.model.setZ(
                self.player.model.getZ() - self.player.falling_speed)
        else:
            self.player.falling_speed = 0
        return Task.cont


game = Game()
game.run()
