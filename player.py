from math import sin, cos, radians


class Hero:
    def __init__(self, map):
        self.model = loader.loadModel('smiley')
        self.model.setScale(0.3)
        self.model.setPos(5, 5, 2)
        self.model.reparentTo(render)
        base.camera.reparentTo(self.model)
        base.camera.setZ(1)
        base.accept('w', self.forward)
        base.accept('w-repeat', self.forward)
        base.accept('s', self.backward)
        base.accept('s-repeat', self.backward)
        base.accept('d', self.right)
        base.accept('d-repeat', self.right)
        base.accept('a', self.left)
        base.accept('a-repeat', self.left)
        self.falling_speed = 0
        self.map = map

    def is_collide(self, position):
        x, y, z = position
        z += 0.1
        for block in self.map:
            xb, yb, zb = block.getPos()
            if xb-0.8 <= x <= xb+0.8:
                if yb-0.8 <= y <= yb+0.8:
                    if zb-0.8 <= z <= zb+0.8:
                        return True
        return False

    def move(self, povorot):
        a = radians(self.model.getH() + povorot)
        dx = sin(a) * 0.1
        dy = cos(a) * 0.1
        x = self.model.getX() - dx
        y = self.model.getY() + dy
        point = (x, y, self.model.getZ())
        if not self.is_collide(point):
            self.model.setPos(point)

    def forward(self):
        self.move(0)

    def backward(self):
        self.move(180)

    def right(self):
        self.move(-90)

    def left(self):
        self.move(90)
