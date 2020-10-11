class Game:
    bx_sz = 50
    height = 700
    width = 1000
    gravity = 0.5
    data = dict()
    # data = {1:[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    #            [0, 0, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    #            [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    #            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]]}
    def __init__(self, d):
        Game.data = d
        self.level = Game.data[1]
        self.num_bxy = Game.height//Game.bx_sz
        self.num_bxx = Game.width//Game.bx_sz
        sty = len(self.level)-self.num_bxy
        self.viewtop = sty*Game.bx_sz
        self.viewleft = (len(self.level[0])-self.num_bxx)*Game.bx_sz
       
    def handle_coins(self, player):
        i = int((player.y+self.viewtop)//Game.bx_sz)
        j = int((player.x+self.viewleft)//Game.bx_sz)
        mxi = min(i+2, len(self.level))
        mni = max(0, i)
        mxj = min(j+2, len(self.level[0]))
        mnj = max(0, j)
        for p in range(mni, mxi):
            for q in range(mnj, mxj):
                if self.level[p][q] == 2:
                    player.coins += 1
                    self.level[p][q] = 0
        textSize(48)
        text("Coins: " + str(player.coins), 20, 50)
        textSize(12)    
    def at_loc(self, x, y):
        i = int((y+self.viewtop)//Game.bx_sz)
        j = min(int((x+self.viewleft)//Game.bx_sz), (len(self.level[i])-1))
       
        return self.level[i][j]
    def update_game(self, player):
        if self.viewleft > 0 and player.x < Game.width*1/2:
            player.x += 1
            self.viewleft -= 1
        if self.viewleft < (len(self.level[0]) - self.num_bxx)*Game.bx_sz and player.x > Game.width*2/3:
            player.x -= 1
            self.viewleft += 1
        if self.viewtop > 0 and player.y < Game.height*1/2:
            self.viewtop -= 1
        if self.viewtop < (len(self.level)-self.num_bxy)*Game.bx_sz and player.y > Game.height*2/3:
            self.viewtop += 1
    def update(self):
        num_bxy = Game.height//Game.bx_sz
        num_bxx = Game.width//Game.bx_sz
        for i in range(0, len(self.level)):
            for j in range(0, len(self.level[i])):
                if self.level[i][j] == 0:
                    fill("#99FF99")
                    stroke("#99FF99")
                elif self.level[i][j] == 2:
                    fill("#FFE51C")
                    stroke("#FFE51C")
                elif self.level[i][j] == 3:
                    fill("#FF2F1C")
                    stroke("#FF2F1C")
                else:
                    fill("#000000")
                    stroke("#000000")
                rect(j*Game.bx_sz-self.viewleft, i*Game.bx_sz-self.viewtop, Game.bx_sz, Game.bx_sz)
               
class Player:
    def __init__(self):
        self.x = Game.width//2
        self.y = 0#Game.height - Game.bx_sz*2
        self.w = Game.bx_sz
        self.h = Game.bx_sz
        self.vx = 0
        self.vy = 1
        self.lives = 3
        self.coins = 0
        self.img = None
        self.on_ground = False
        self.alpha = 0
    def lose_life(self):
        self.x = Game.width//2
        self.y = 0
        self.alpha = 0
        self.vx = 0
        self.vy = 0
        self.lives -= 1
    def update(self):
        #try to move
        self.x += self.vx
        self.y += self.vy
        #detect hits
        hits = self.hit_block()
        #interpret hits
        left = hits[0] and hits[2]
        right = hits[1] and hits[3]
        top = hits[0] or hits[1]
        bottom = hits[2] or hits[3]
        if bottom:
            if self.y + self.w <= Game.height+100:
                #self.y -= self.vy
                self.vy = 0
                self.on_ground = True
                self.y = ((self.y+g.viewtop)//Game.bx_sz)*(Game.bx_sz)-g.viewtop
            else:
                self.lose_life()
        if right:
            #self.x = (self.x//Game.bx_sz)*(Game.bx_sz)-1
            self.vx = -abs(self.vx)
        if top:
           
            #self.y = (self.y//Game.bx_sz)*Game.bx_sz
            self.vy = abs(self.vy)*0.8
        if left:
            self.x -= self.vx
            #self.x = (self.x//Game.bx_sz)*Game.bx_sz+1
            self.vx = abs(self.vx)
        if not bottom:
            self.vy += Game.gravity
            self.on_ground = False
        if self.hit_lava():
            print("lava")
            self.lose_life()    
        if abs(self.vx) > 0.05:
            self.vx *= 0.8
        else:
            self.vx = 0
        fill(255, 0, 0, self.alpha)
        self.alpha += 1
        strokeWeight(5)
        stroke("#000000")
        rect(self.x, self.y, self.w, self.h)
        strokeWeight(1)
        text("X" + str(self.x), 900, 20)
        text("Y" + str(self.y), 900, 40)
        text("top:" + str(top), 900, 60)
        text("right:" + str(right), 900, 80)
        text("left:" + str(left), 900, 100)
        text("bottom:" + str(bottom), 900, 120)
        g.handle_coins(self)
        g.update_game(self)
    def hit_block(self):
        global g
        #self.x < 0 or (self.y + self.h >= g.height) or
        #self.x + self.w >= g.width or (self.y + self.h >= g.height) or
        u_l = self.x < 0 or self.y < 0 or g.at_loc(self.x, self.y) == 1
        u_r = self.x + self.w >= g.width or self.y < 0 or g.at_loc(self.x + self.w, self.y) == 1
        b_l = g.at_loc(self.x, self.y + self.h) == 1
        b_r = g.at_loc(self.x + self.w, self.y + self.h-1) == 1
        return [u_l, u_r, b_l, b_r]
    def hit_lava(self):
        return g.at_loc(self.x, self.y) == 3 or g.at_loc(self.x+self.w, self.y) == 3 or g.at_loc(self.x, self.y+self.h) == 3 or g.at_loc(self.x + self.w, self.y + self.h) == 3
    def move(self, dir):
       
        if dir == "left":
            self.vx = -5
           
        if dir == "right":
            self.vx = 5
        if dir == "up":
           
                self.vy = -10
def setup():
    global g, p
   
    size(Game.width, Game.height)
    #noStroke()

   
    #g.init_levels()
    listy = loadStrings("lvl1.csv")
   
    temp = []
   
    for r in range(len(listy)):
        k = listy[r].split(",")
        newRow = []
        for t in range(len(k)):
           
            newRow.append(int(k[t]))
        temp.append(newRow)
    Game.data = {1:temp}
    print(temp[-1])
    g = Game({1:temp})
    p = Player()
g = None
p = None    
def draw():
    global g, p
    background("#FFFFFF")
    g.update()
    p.update()

def keyPressed():
    global g, p
    if keyCode == UP:
        p.move("up")
    if keyCode == DOWN:
        p.move("down")
    if keyCode == LEFT:
        p.move("left")
    if keyCode == RIGHT:
        p.move("right")
