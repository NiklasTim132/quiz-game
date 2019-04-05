"""
author: Niklas REBEL
email: niklas.rebel@gmail.com
license: gpl, see http://www.gnu.org/licenses/gpl-3.0.de.html
download: https://github.com/niklastim132/quiz-game/master/quiz.py
idea: clean python3/pygame template using pygame.math.vector2

"""
import pygame
import random
import os
import time

class Game():
    

        # Anweisungen:
        anweisung0 = "----  Drücke schnell die entsprechende Taste!  ----"
        #anweisung1 = "STOP! Buzzer von Spieler 1 wurde am schnellsten aktiviert. Er darf jetzt Antworten!" 
        #anweisung2 = "STOP! Buzzer von Spieler 2 wurde am schnellsten aktiviert. Er darf jetzt Antworten!"
        anweisung3 = "STOP! Die Zeit ist abgelaufen...Nächste Frage kommt..."
        frage={}
        frage[1]= ["Wieviel kostet der Programmierkurs",
                   "von Horst Jens in einer Stunde?"]
        frage[2]= ["Was heißt 'Guten Tag' auf Französisch?"]
        frage[3]= ["Wenn zehn Äpfel 3€ kosten, wieviel Euro",
                   " kosten dann 50 Äpfel?"]
                 
        frage[4]= ["Wann gilt der Pythagoräische Lehrsatz", 
        "in der Mathematik?"]
        frage[5]= ["Wieviele Tage hat das Jahr?"]
        frage[6]= ["Wann gilt ein Schachspiel als Patt?"]
        frage[7]= ["Wie lautet die Landesvorwahl von England?"]
        frage[8]= ["In der Programmiersprache 'Python'",
        "bewirkt dieses Zeichen '#' was...?"]
        frage[9]= ["Die IBAN ist notwendig bei/für..?"]
        frage[10]= ["Mit welchen vier Standard Tasten",
        " lässt sich der PC-Charakter in Minecraft steuern?"]
        frage[11]= ["Aus wie vielen Worten besteht dass Götz Zitat?"]
        frage[12]= ["'Romeo und Julia' ist ein Stück von...?"]
        frage[13]= ["In der Programmiersprache 'HTML'",
        " steht dieses Zeichen '<b>...</b>' für welche Textformatierung?"]
        frage[14]= ["Ein Titel der EAV lautet...?"]
        frage[15]=["Löse die Gleichung, und nenne das Ergebniss: X + 10 = 5 * 4"]
        #frage[16]=["Die Finken waren für Charles Darwin besonders. Warum?"]
        #frage[17]= "Als 'Bug' wird in der IT-Sprache was bezeichnet?"


        antwort = {}
        # die richtige Antwort muss immmer die erste sein, beliebig viel falsche danach!
        antwort[1] = ["12,-€", "120,-€", "2.50€", "60,-€"]
        antwort[2] = ["Bonjour", "bienvenuti", "Grüss Gott", "bon soir"]
        antwort[3] = ["15€", "30€", "45€", "5€", "150€"]
        antwort[4] = ["Nur in einem rechtwinkeligen Dreieck", "In jedem Dreieck", "Nur bei gleichschenkeligen Dreiecken", "Der Lehrsatz ist garnicht existent"]
        antwort[5] = ["365 Tage", "563 Tage", "635 Tage", "536 Tage", "653 Tage"]
        antwort[6] = ["Wenn keine Figur sich mehr bewegen kann, aber der König nicht im Schach steht und alle Ausweichfelder blockiert sind", "Wenn der König im Schach steht und alle Ausweichfelder bedroht sind", "Wenn die Dame bedroht wird und es für sie keine Ausweichfelder mehr gibt", "Keine der genannten Antworten"]
        antwort[7] = ["+44","+55","+66","+43"]
        antwort[8] = ["Es kommentiert einen Befehl vorrübergehend aus","Es stoppt das Skript komplett","Es macht nichts","Es wird nicht in Python sondern in HTML verwendet"]
        antwort[9] = ["Zahlungen","Das Ausleihen von Büchern","Programmen","Anrufe"]
        antwort[10] = ["WASD", "Pfeiltasten","HIJK","OLKÖ"]
        antwort[11] = ["4 Wörtern", "8 Wörtern", "12 Wörtern", "16 Wörtern"]
        antwort[12] = ["William Shakespear", "Walter Shakespear", "Werner Shakespear", "Willhelm Shakespear"]
        antwort[13] = ["Fett", "Kursiv", "Unterstrichen", "Durchgestrichen"]
        antwort[14] = ["Werwolf-Attacke", "Monsterball ist überall", "Waka Waka", "La La La"]
        antwort[15] = ["X = 10", "X = -10", "X = 20", "X = 0", "X = -20"]

def cleanbyte(number):
    """makes sure the entered number is in the range of 0-255 and returns an integer in this range"""
    if number< 0:
        return 0
    elif number > 255:
        return 255
    else:
        return int(number)


def randomize_color(color, delta=50):
    d=random.randint(-delta, delta)
    color = color + d
    color = min(255,color)
    color = max(0, color)
    return color


def make_text(msg="pygame is cool", fontcolor=(255, 0, 255), fontsize=42, font=None):
    """returns pygame surface with text. You still need to blit the surface."""
    myfont = pygame.font.SysFont(font, fontsize)
    mytext = myfont.render(msg, True, fontcolor)
    mytext = mytext.convert_alpha()
    return mytext

def write(background, text, x=50, y=150, color=(0,0,0),
          fontname="mono", fontsize=None, center=False):
        """write text on pygame surface. """
        if fontsize is None:
            fontsize = 24
        font = pygame.font.SysFont(fontname, fontsize, bold=True)
        fw, fh = font.size(text)
        surface = font.render(text, True, color)
        if center: # center text around x,y
            background.blit(surface, (x-fw//2, y-fh//2))
        else:      # topleft corner is x,y
            background.blit(surface, (x,y))
        return fw, fh

def elastic_collision(sprite1, sprite2):
        """elasitc collision between 2 VectorSprites (calculated as disc's).
           The function alters the dx and dy movement vectors of both sprites.
           The sprites need the property .mass, .radius, pos.x pos.y, move.x, move.y
           by Leonard Michlmayr"""
        if sprite1.static and sprite2.static:
            return 
        dirx = sprite1.pos.x - sprite2.pos.x
        diry = sprite1.pos.y - sprite2.pos.y
        sumofmasses = sprite1.mass + sprite2.mass
        sx = (sprite1.move.x * sprite1.mass + sprite2.move.x * sprite2.mass) / sumofmasses
        sy = (sprite1.move.y * sprite1.mass + sprite2.move.y * sprite2.mass) / sumofmasses
        bdxs = sprite2.move.x - sx
        bdys = sprite2.move.y - sy
        cbdxs = sprite1.move.x - sx
        cbdys = sprite1.move.y - sy
        distancesquare = dirx * dirx + diry * diry
        if distancesquare == 0:
            dirx = random.randint(0,11) - 5.5
            diry = random.randint(0,11) - 5.5
            distancesquare = dirx * dirx + diry * diry
        dp = (bdxs * dirx + bdys * diry) # scalar product
        dp /= distancesquare # divide by distance * distance.
        cdp = (cbdxs * dirx + cbdys * diry)
        cdp /= distancesquare
        if dp > 0:
            if not sprite2.static:
                sprite2.move.x -= 2 * dirx * dp
                sprite2.move.y -= 2 * diry * dp
            if not sprite1.static:
                sprite1.move.x -= 2 * dirx * cdp
                sprite1.move.y -= 2 * diry * cdp

        
class Flytext(pygame.sprite.Sprite):
    def __init__(self, x, y, text="hallo", color=(255, 0, 0),
                 dx=0, dy=-50, duration=2, acceleration_factor = 1.0, delay = 0, fontsize=22):
        """a text flying upward and for a short time and disappearing"""
        self._layer = 7  # order of sprite layers (before / behind other sprites)
        pygame.sprite.Sprite.__init__(self, self.groups)  # THIS LINE IS IMPORTANT !!
        self.text = text
        self.r, self.g, self.b = color[0], color[1], color[2]
        self.dx = dx
        self.dy = dy
        self.x, self.y = x, y
        self.duration = duration  # duration of flight in seconds
        self.acc = acceleration_factor  # if < 1, Text moves slower. if > 1, text moves faster.
        self.image = make_text(self.text, (self.r, self.g, self.b), fontsize)  # font 22
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.time = 0 - delay

    def update(self, seconds):
        self.time += seconds
        if self.time < 0:
            self.rect.center = (-100,-100)
        else:
            self.y += self.dy * seconds
            self.x += self.dx * seconds
            self.dy *= self.acc  # slower and slower
            self.dx *= self.acc
            self.rect.center = (self.x, self.y)
            if self.time > self.duration:
                self.kill()      # remove Sprite from screen and from groups


class VectorSprite(pygame.sprite.Sprite):
    """base class for sprites. this class inherits from pygames sprite class"""
    number = 0
    numbers = {} # { number, Sprite }

    def __init__(self, **kwargs):
        self._default_parameters(**kwargs)
        self._overwrite_parameters()
        pygame.sprite.Sprite.__init__(self, self.groups) #call parent class. NEVER FORGET !
        self.number = VectorSprite.number # unique number for each sprite
        VectorSprite.number += 1
        VectorSprite.numbers[self.number] = self
        self.create_image()
        self.distance_traveled = 0 # in pixel
        self.rect.center = (-300,-300) # avoid blinking image in topleft corner
        if self.angle != 0:
            self.set_angle(self.angle)

    def _overwrite_parameters(self):
        """change parameters before create_image is called""" 
        pass

    def _default_parameters(self, **kwargs):    
        """get unlimited named arguments and turn them into attributes
           default values for missing keywords"""

        for key, arg in kwargs.items():
            setattr(self, key, arg)
        if "layer" not in kwargs:
            self._layer = 4
        else:
            self._layer = self.layer
        if "static" not in kwargs:
            self.static = False
        if "pos" not in kwargs:
            self.pos = pygame.math.Vector2(random.randint(0, Viewer.width),-50)
        if "move" not in kwargs:
            self.move = pygame.math.Vector2(0,0)
        if "radius" not in kwargs:
            self.radius = 5
        if "width" not in kwargs:
            self.width = self.radius * 2
        if "height" not in kwargs:
            self.height = self.radius * 2
        if "color" not in kwargs:
            #self.color = None
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        if "hitpoints" not in kwargs:
            self.hitpoints = 100
        self.hitpointsfull = self.hitpoints # makes a copy
        if "mass" not in kwargs:
            self.mass = 10
        if "damage" not in kwargs:
            self.damage = 1
        if "bounce_on_edge" not in kwargs:
            self.bounce_on_edge = False
        if "kill_on_edge" not in kwargs:
            self.kill_on_edge = False
        if "angle" not in kwargs:
            self.angle = 0 # facing right?
        if "max_age" not in kwargs:
            self.max_age = None
        if "max_distance" not in kwargs:
            self.max_distance = None
        if "picture" not in kwargs:
            self.picture = None
        if "bossnumber" not in kwargs:
            self.bossnumber = None
        if "kill_with_boss" not in kwargs:
            self.kill_with_boss = False
        if "sticky_with_boss" not in kwargs:
            self.sticky_with_boss = True
        if "mass" not in kwargs:
            self.mass = 15
        if "speed" not in kwargs:
            self.speed = None
        if "age" not in kwargs:
            self.age = 0 # age in seconds
        if "warp_on_edge" not in kwargs:
            self.warp_on_edge = False
        if "edge_distance" not in kwargs:
            self.edge_distance = 0

    def kill(self):
        if self.number in self.numbers:
           del VectorSprite.numbers[self.number] # remove Sprite from numbers dict
        pygame.sprite.Sprite.kill(self)

    def create_image(self):
        if self.picture is not None:
            self.image = self.picture.copy()
        else:
            self.image = pygame.Surface((self.width,self.height))
            self.image.fill((self.color))
        self.image = self.image.convert_alpha()
        self.image0 = self.image.copy()
        self.rect= self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def rotate(self, by_degree):
        """rotates a sprite and changes it's angle by by_degree"""
        self.angle += by_degree
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter

    def set_angle(self, degree):
        """rotates a sprite and changes it's angle to degree"""
        self.angle = degree
        oldcenter = self.rect.center
        self.image = pygame.transform.rotate(self.image0, self.angle)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = oldcenter

    def update(self, seconds):
        """calculate movement, position and bouncing on edge"""
        # ----- kill because... ------
        if self.hitpoints <= 0:
            self.kill()
            return
        if self.max_age is not None and self.age > self.max_age:
            self.kill()
            return
        if self.max_distance is not None and self.distance_traveled > self.max_distance:
            self.kill()
            return
            
        # ---- movement with/without boss ----
        if self.bossnumber is not None:
            if self.kill_with_boss:
                if self.bossnumber not in VectorSprite.numbers:
                    self.kill()
                    return
            if self.sticky_with_boss:
                boss = VectorSprite.numbers[self.bossnumber]
                #self.pos = v.Vec2d(boss.pos.x, boss.pos.y)
                self.pos = pygame.math.Vector2(boss.pos.x, boss.pos.y)
        self.pos += self.move * seconds
        self.distance_traveled += self.move.length() * seconds
        self.age += seconds
        self.wallbounce()
        self.rect.center = ( round(self.pos.x, 0), -round(self.pos.y, 0) )

    def wallbounce(self):
        # ---- bounce / kill on screen edge ----
        # ------- left edge ----
        if self.pos.x < 0 - self.edge_distance:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.x = 0 - self.edge_distance
                self.move.x *= -1
            elif self.warp_on_edge:
                self.pos.x = Viewer.width + self.edge_distance 
        # -------- upper edge -----
        if self.pos.y  > 0:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.y = 0
                self.move.y *= -1
            elif self.warp_on_edge:
                self.pos.y = -Viewer.height
        # -------- right edge -----                
        if self.pos.x  > Viewer.width + self.edge_distance:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.x = Viewer.width + self.edge_distance
                self.move.x *= -1
            elif self.warp_on_edge:
                self.pos.x = 0 - self.edge_distance
        # --------- lower edge ------------
        if self.pos.y   < -Viewer.height:
            if self.kill_on_edge:
                self.kill()
            elif self.bounce_on_edge:
                self.pos.y = -Viewer.height
                self.move.y *= -1
            elif self.warp_on_edge:
                self.pos.y = 0


class Spark(VectorSprite):
    
    def _overwrite_parameters(self):
        self._layer = 2
        self.kill_on_edge = True
    
    def create_image(self):
        r,g,b = self.color
        r = randomize_color(r,50)
        g = randomize_color(g,50)
        b = randomize_color(b,50)
        self.image = pygame.Surface((10,10))
        pygame.draw.line(self.image, (r,g,b), 
                         (10,5), (5,5), 3)
        pygame.draw.line(self.image, (r,g,b),
                          (5,5), (2,5), 1)
        self.image.set_colorkey((0,0,0))
        self.rect= self.image.get_rect()
        self.image0 = self.image.copy()    



class Viewer(object):
    width = 0
    height = 0
    images = {}

    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments """
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        Viewer.width = width    # make global readable
        Viewer.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((64,64,64)) # fill background white
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        # --- höchste fragennummer is? ----
        self.maxnr = 0
        for nr in Game.frage:
            if nr > self.maxnr:
                self.maxnr = nr
        # ------ background images ------
        self.backgroundfilenames = [] # every .jpg file in folder 'data'
        try:
            for root, dirs, files in os.walk("data"):
                for file in files:
                    if file[-4:] == ".jpg" or file[-5:] == ".jpeg":
                        self.backgroundfilenames.append(file)
            random.shuffle(self.backgroundfilenames) # remix sort order
        except:
            print("no folder 'data' or no jpg files in it")
        #if len(self.backgroundfilenames) == 0:
        #    print("Error: no .jpg files found")
        #    pygame.quit
        #    sys.exit()
        #Viewer.bombchance = 0.015
        #Viewer.rocketchance = 0.001
        #Viewer.wave = 0
        self.age = 0
        # ------ joysticks ----
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for j in self.joysticks:
            j.init()
        #self.load_sprite_images()
        self.prepare_sprites()
        #self.loadbackground()
        #self.load_sounds()
        
    def load_sounds(self):
        # ---- sounds -----
        Viewer.powerup = pygame.mixer.Sound(os.path.join(
              "data", "powerup.wav"))
        
        # --- music ---
        self.music1 = pygame.mixer.music.load(os.path.join(
              "data", "music1.ogg"))
              

    def load_sprite_images(self):
        Viewer.images["tank1"] = pygame.image.load(os.path.join(
                       "data", "tank1.png")).convert_alpha()
        #Viewer.images["spaceship"] = pygame.image.load(os.path.join(
        #               "data", "spaceship.png")).convert_alpha()
        

    def loadbackground(self):
        
        try:
            self.background = pygame.image.load(os.path.join("data",
                 self.backgroundfilenames[Viewer.wave %
                 len(self.backgroundfilenames)]))
        except:
            self.background = pygame.Surface(self.screen.get_size()).convert()
            self.background.fill((255,255,255)) # fill background white
            
        self.background = pygame.transform.scale(self.background,
                          (Viewer.width,Viewer.height))
        self.background.convert()
        

    def prepare_sprites(self):
        """painting on the surface and create sprites"""
        # --- sprites in the allgroup will be visible each frame ---
        self.allgroup =  pygame.sprite.LayeredUpdates() # for drawing
        # --- additional groups for collision detection ----
        #self.crosshairgroup = pygame.sprite.Group()
#        self.rocketgroup = pygame.sprite.Group()
 #       self.playergroup = pygame.sprite.Group()
  #      self.bubblegroup = pygame.sprite.Group()
   #     self.monstergroup = pygame.sprite.Group()
        
        # ---- assign sprite groups to the Sprite classes ----
        VectorSprite.groups = self.allgroup
        Flytext.groups = self.allgroup
        #Crosshair.groups = self.allgroup, self.crosshairgroup
    #    Rocket.groups = self.allgroup, self.rocketgroup
     #   Spaceship.groups = self.allgroup, self.playergroup
        Spark.groups = self.allgroup
        #Star.groups = self.allgroup
   #     Bubble.groups = self.allgroup, self.bubblegroup
    #    Monster1.groups = self.allgroup, self.monstergroup


        
        #self.mouse1 = Crosshair(control="mouse", color=(255,0,0))
        #self.mouse2 = Crosshair(control='keyboard1', color=(255,255,0))
        #self.mouse3 = Crosshair(control="keyboard2", color=(255,0,255))
        #self.mouse4 = Crosshair(control="joystick1", color=(255,128,255))
        #self.mouse5 = Crosshair(control="joystick2", color=(255,255,255))

                    
    def new_question(self):
        self.number = random.randint(1,self.maxnr)
        self.question = Game.frage[self.number]
        
        
   
    def run(self):
        """The mainloop"""
        running = True
        self.new_question()
        pygame.mouse.set_visible(False)
        oldleft, oldmiddle, oldright  = False, False, False
        # joysticknumber, buttonnumer. dös is a dict of dicts.
        jpushed = { 0 : {0:False, 1:False, 2:False, 3:False} ,
                    1 : {0:False, 1:False, 2:False, 3:False}, 
                    2 : {0:False, 1:False, 2:False, 3:False},
                    3 : {0:False, 1:False, 2:False, 3:False}
                   }
        joldpushed = { 0 : {0:False, 1:False, 2:False, 3:False} ,
                    1 : {0:False, 1:False, 2:False, 3:False}, 
                    2 : {0:False, 1:False, 2:False, 3:False},
                    3 : {0:False, 1:False, 2:False, 3:False}
                   }
        self.snipertarget = None
        gameOver = False
        exittime = 0
        # start the music
        #pygame.mixer.music.play(loops=-1)
        while running:
            milliseconds = self.clock.tick(self.fps) #
            seconds = milliseconds / 1000
            self.playtime += seconds
            if gameOver:
                if self.playtime > exittime:
                    break
            #Game over?
            #if not gameOver:
            # -------- events ------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # ------- pressed and released key ------
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    #if event.key == pygame.K_n:
                    #    Flytext(200,50, text="Niklas codet")
                    #if event.key == pygame.K_h:
                    #    Flytext(Viewer.width//2,Viewer.height//2, text="Horst dreht durch!!!",color=(32,229,16), fontsize = random.randint(100,700))
                    
                    if event.key == pygame.K_SPACE:
                        self.new_question()
                    
                    # ---- shooting rockets for player1 ----
           #         if event.key == pygame.K_TAB:
           #             self.player1.fire()
                        #Viewer.powerup.play()
                    
                    #if event.key == pygame.K_x:
                    #    self.player1.speed += 10
                    
                    
                    
                    
                    # ---- stop movement for self.player1 -----
                    #if event.key == pygame.K_r:
                    #    self.player1.move *= 0.1 # remove 90% of movement
                    
   
            # ----- delete everything on screen --------
            self.screen.blit(self.background, (0, 0))
            
            # --- question schreiben ---
            # self question ist eine liste weil mehrzeilig
            # deshalb, stück für stück abarbeiten
            wt, ht = 0, 0
            for y, q in enumerate(self.question):
                 w, h =write(self.screen, q, Viewer.width // 2, 100+y*30, fontsize=30, color=(255,255,255),center=True)
                 if w > wt:
                     wt = w
            
            #pygame.draw.rect( self.screen, (255,255,255), (Viewer.width // 2 - wt//2 - 5, 100+ y*30 -5, wt + 10, y*30+10), 1)
            pygame.draw.rect( self.screen, (255,255,255), (15, 80, Viewer.width - 30,  y*30 +50), 1)
             
            
            
            farben = [(0,255,0) , (255,0,0) , (255,165,0) , (0,0,255)  ]
            
            # ---- antworten schreiben -----
            reihung= [0,1,2,3]
            random.shuffle(reihung)
            for nr, char in enumerate(["(A)","(B)","(Y)","(X)"]):
                bcolor = farben [nr]
                print("nr", nr)
                print("self.number", self.number)
                rnr = reihung[nr]
                print("game.antwort[self.number][rnr]:", Game.antwort[self.number][nr])
                w, h = write(self.screen, Game.antwort[self.number][nr], 200, 300+100*nr, fontsize=50, color=bcolor)
        
                
                w,h = write(self.screen, char, 50, 300+100*nr, fontsize=50, color=bcolor)
                
                pygame.draw.rect(self.screen, (200,200,200), (50, 300+100*nr,w,h), 1)
                

            # ------------ pressed keys ------
            pressed_keys = pygame.key.get_pressed()
            

            # ------ mouse handler ------
            left,middle,right = pygame.mouse.get_pressed()
            #if oldleft and not left:
            #    self.launchRocket(pygame.mouse.get_pos())
            #if right:
            #    self.launchRocket(pygame.mouse.get_pos())
            oldleft, oldmiddle, oldright = left, middle, right

            # ------ joystick handler -------
            #mouses = [self.mouse4, self.mouse5]
            for number, j in enumerate(self.joysticks):
                # ====== number is di nummer des joysticks, oida! ====
                if number == 0 or number==1 or number==2 or number==3:
                   #x = j.get_axis(0)
                   #y = j.get_axis(1)
                   #mouses[number].x += x * 20 # *2 
                   #mouses[number].y += y * 20 # *2 
                   buttons = j.get_numbuttons()
                   
                   for b in range(buttons):
                       if b > 3:
                           continue   # uns interessieren nur die ersten 4 buttons
                       # ========= b is di interne nummer vom joystickbutton , kapiert? ============ print("was ist b?", b)
                       pushed = j.get_button( b )
                       # === pushed is demnach true oda foisch, gö?
                       #jpushed[number][b] = False # prinzipiell amal auf falsch setzen
                       jpushed[number][b] = pushed
                       
                       if b == 0 and pushed and not joldpushed[number][b]:
                           Flytext(100, 400,"X {}".format(number), color=(0,0,255),fontsize=200,acceleration_factor=1.2,duration=2.0)
                       elif b == 1 and pushed and not joldpushed[number][b]:
                           Flytext(200,400, "A {}".format(number),color=(17,206,19),fontsize=200,acceleration_factor=1.2,duration=2.0)
                       elif b == 2  and pushed and not joldpushed[number][b]:
                           Flytext(300,400, "B {}".format(number),color=(255,0,0),fontsize=200,acceleration_factor=1.2,duration=2.0)
                       elif b == 3  and pushed and not joldpushed[number][b]:
                           Flytext(400,400, "Y {}".format(number),color=(255,165,0),fontsize=200,acceleration_factor=1.2,duration=2.0)
                       
                       joldpushed[number][b] = jpushed[number][b]
            # write text below sprites
            write(self.screen, "FPS: {:8.3}".format(
                self.clock.get_fps()), x=10, y=10, color=(128,0,128))
            # --------- update all sprites --------
            self.allgroup.update(seconds)
            
            # ----------- clear, draw , update, flip -----------------
            self.allgroup.draw(self.screen)

            # -------- next frame -------------
            pygame.display.flip()
        #-----------------------------------------------------
        pygame.mouse.set_visible(True)    
        pygame.quit()

if __name__ == '__main__':
    Viewer(1430,800).run() # try Viewer(800,600).run()
