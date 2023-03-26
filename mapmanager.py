# напиши здесь код создания и управления картой

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
