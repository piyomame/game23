import pyxel

class Map:
    def __init__(self):
        self.x,self.y = 0,0
        self.caunnt = 0
    def update(self):
        self.caunnt += 1
        if self.caunnt%2 == 0:
            self.x -= 1
    def draw(self):
        pyxel.bltm(self.x,self.y,0,0,0,20*8,15*8)

class App:
    def __init__(self):
        pyxel.init(160,120,title = "Map Drawing Sample")

        pyxel.load("mapkannsei.pyxres")
        self.map = Map() 
        pyxel.run(self.update,self.draw)
    def update(self):
        self.map.update()
    def draw(self):
        pyxel.cls(0)
        self.map.draw()

App()