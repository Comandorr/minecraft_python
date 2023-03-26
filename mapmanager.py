class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = loader.loadTexture('wood.png')
        self.color = (1, 0, 0, 1)
        self.map = []

    def addBlock(self, position):
        b = loader.loadModel(self.model)
        b.setTexture(self.texture)
        b.setPos(position)
        b.reparentTo(render)
        self.map.append(b)

    def on_ground(self, position):
        x, y, z = position
        for block in self.map:
            xb, yb, zb = block.getPos()
            if xb-1 <= x <= xb+1:
                if yb-1 <= y <= yb+1:
                    if zb-1 <= z <= zb+1:
                        return True
        return False
