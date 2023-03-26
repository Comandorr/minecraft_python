from math import sin, cos, radians


class Hero:
    def __init__(self):
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

    def forward(self):
        a = radians(self.model.getH())
        dx = sin(a) * 0.1
        dy = cos(a) * 0.1
        self.model.setX(self.model.getX() - dx)
        self.model.setY(self.model.getY() + dy)

    def backward(self):
        a = radians(self.model.getH() + 180)
        dx = sin(a) * 0.1
        dy = cos(a) * 0.1
        self.model.setX(self.model.getX() - dx)
        self.model.setY(self.model.getY() + dy)

    def right(self):
        a = radians(self.model.getH() - 90)
        dx = sin(a) * 0.1
        dy = cos(a) * 0.1
        self.model.setX(self.model.getX() - dx)
        self.model.setY(self.model.getY() + dy)

    def left(self):
        a = radians(self.model.getH() + 90)
        dx = sin(a) * 0.1
        dy = cos(a) * 0.1
        self.model.setX(self.model.getX() - dx)
        self.model.setY(self.model.getY() + dy)
