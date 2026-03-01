import pyxel

WALL_TILES = [(0,1)]

class Player:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.w, self.h = 8,8
        self.speed = 2   
    def update(self):
        next_x, next_y = self.x,self.y
        if pyxel.btn(pyxel.KEY_LEFT): next_x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT): next_x += self.speed
        if pyxel.btn(pyxel.KEY_UP): next_y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN): next_y += self.speed
    
        next_tile_x,next_tile_y = next_x // 8,next_y // 8
        tile = pyxel.tilemap(0).pget(next_tile_x,next_tile_y)

        if tile not in WALL_TILES:
            self.x,self.y = next_x,next_y
    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h,7)
class App:
    def __init__(self):
        pyxel.init(160,120,title = "Map Drawing Sample")

        pyxel.load("mapkannsei.pyxres")


        self.player = Player(16,16)

        pyxel.run(self.update,self.draw)

    def update(self):

        self.player.update()

    def draw(self):
        pyxel.cls(0)

        pyxel.bltm(0,0,0,0,0,20*8,15*8)

        self.player.update()
App()