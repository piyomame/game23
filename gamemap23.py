import pyxel

class Player:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.w, self.h = 8,8
        self.speed = 2  

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT): self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT): self.x += self.speed
        if pyxel.btn(pyxel.KEY_UP): self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN): self.y += self.speed

    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h,7) 

class Map:
    def __init__(self):
        self.x,self.y = 0,0
        self.w = 200*8
    def update(self):
        if self.x == 80:
            self.x -= 1
    def draw(self):
        pyxel.bltm(self.x,self.y,0,0,0,self.w,15*8)

class App:
    def __init__(self):
        pyxel.init(160,120,title = "Map Drawing Sample")

        pyxel.load("mapkannsei.pyxres")
        self.map = Map() 
        self.player = Player(16,16)
        pyxel.run(self.update,self.draw)
    def update(self):
        self.map.update()
        self.player.update()
    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        self.player.draw()

App()