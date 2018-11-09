import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.

class Game():
    

        # Anweisungen:
        anweisung0 = "----  Drücke schnell die entsprechende Taste!  ----"
        anweisung1 = "STOP! Buzzer von Spieler 1 wurde am schnellsten aktiviert. Er darf jetzt Antworten!" 
        anweisung2 = "STOP! Buzzer von Spieler 2 wurde am schnellsten aktiviert. Er darf jetzt Antworten!"
        anweisung3 = "STOP! Die Zeit ist abgelaufen...Nächste Frage kommt..."
        frage={}
        frage[1]= "Wieviel kostet der Programmierkurs von Horst Jens in einer Stunde?"
        frage[2]= "Was heißt 'Guten Tag' auf Französisch?"
        frage[3]= "Wenn zehn Äpfel 3€ kosten, wieviel Euro kosten dann 50 Äpfel?"
        frage[4]= "Wann gilt der Pythagoräische Lehrsatz in der Mathematik?"
        frage[5]= "Wieviele Tage hat das Jahr?"
        frage[6]= "Wann gilt ein Schachspiel als Patt?"
        frage[7]= "Wie lautet die Landesvorwahl von England?"
        frage[8]= "In der Programmiersprache 'Python' bewirkt dieses Zeichen '#' was...?"
        frage[9]= "Die IBAN ist notwendig bei/für..?"
        frage[10]= "Mit welchen vier Standard Tasten lässt sich der PC-Charakter in Minecraft steuern?"
        frage[11]= "Aus wie vielen Worten besteht dass Götz Zitat?"
        frage[12]= "'Romeo und Julia' ist ein Stück von...?"
        frage[13]= "In der Programmiersprache 'HTML' steht dieses Zeichen '<b>...</b> für welche Textformatierung?"
        frage[14]= "Ein Titel der EAV lautet...?"
        frage[15]= "Als 'Bug' wird in der IT-Sprache was bezeichnet?"


        antwort = {}
        # die richtige Antwort muss immmer die erste sein, beliebig viel falsche danach!
        antwort[1] = ["12,-€", "120,-€", "2.50€", "60,-€"]
        antwort[2] = ["Bonjour", "bienvenuti", "Grüss Gott", "bon soir"]
        antwort[3] = ["15€", "30€", "45€", "5€", "150€"]
        antwort[4] = ["Nur in einem rechtwinkeligen Dreieck", "In jedem Dreieck", "Nur bei gleichschenkeligen Dreiecken", "Der Lehrsatz ist garnicht existent"]
        antwort[5] = ["365 Tage", "563 Tage", "635 Tage", "536 Tage", "653 Tage"]
        antwort[6] = ["Wenn keine Figur sich mehr bewegen kann, aber der König nicht im Schach steht und alle Ausweichfelder blockiert sind"]
        antwort[7] = ["+44","+55","+66","+43"]
        antwort[8] = ["Es kommentiert einen Befehl vorrübergehend aus","Es stoppt das Skript komplett","Es macht nichts","Es wird nicht in Python sondern in HTML verwendet"]
        antwort[9] = ["Zahlungen","Das Ausleihen von Büchern","Programmen","Anrufe"]
        antwort[10] = ["WASD", "Pfeiltasten","HIJK","OLKÖ"]
        antwort[11] = ["4 Wörtern", "8 Wörtern", "12 Wörtern", "16 Wörtern"]
        antwort[12] = ["William Shakespear", "Walter Shakespear", "Werner Shakespear", "Willhelm Shakespear"]
        antwort[13] = ["Fett", "Kursiv", "Unterstrichen", "Durchgestrichen"]
        antwort[14] = []
    
class TextPrint():
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 35)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 50
        self.y = 50
        self.line_height = 50
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10

class PygView():
    def __init__(self,xres=3000,yres=800):
        PygView.xres=xres
        PygView.yres=yres

        pygame.init()
         
        # Set the width and height of the screen [width,height]
        self.size = [xres, yres]
        self.screen = pygame.display.set_mode(self.size)
        self.version = "0.1.1"
        pygame.display.set_caption("Quiz-Game".format(self.version))

        #Loop until the user clicks the close button.
        self.gameover = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # Initialize the joysticks
        pygame.joystick.init()
            
        # Get ready to print
        self.textPrint = TextPrint()

    def run(self):
        

        # -------- Main Program Loop -----------
        while not self.gameover:
            # EVENT PROCESSING STEP
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self.gameover=True        # Flag that we are done so we exit this loop
                
                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
                    
         
            # DRAWING STEP
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            self.screen.fill(WHITE)
            self.textPrint.reset()

            # Get count of joysticks
            self.joystick_count = pygame.joystick.get_count()

            #textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
            self.textPrint.print(self.screen, "{}".format(Game.anweisung0))
            self.textPrint.indent()
            
            # For each joystick:
            for j in range(self.joystick_count):
                self.joystick = pygame.joystick.Joystick(j)
                self.joystick.init()
            
                self.textPrint.print(self.screen, "Joystick {}".format(j) )
                #textPrint.indent()
            
                # Get the name from the OS for the controller/joystick
                self.name = self.joystick.get_name()
                self.textPrint.print(self.screen, "Joystick name: {}".format(self.name) )
                
                # Usually axis run in pairs, up/down for one, and left/right for
                # the other.
                self.axes = self.joystick.get_numaxes()
                #textPrint.print(screen, "Number of axes: {}".format(axes) )
                #textPrint.indent()
                
                for i in range( self.axes ):
                    self.axis = self.joystick.get_axis( i )
                    #textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
                #textPrint.unindent()
                    
                self.buttons = self.joystick.get_numbuttons()
                #textPrint.print(screen, "Number of buttons: {}".format(buttons) )
                #textPrint.indent()
                # wir wollen button0
                for i in range( self.buttons ):
                    self.button = self.joystick.get_button( i )
                    if j==0 and i in (0,1,2,3) and self.button==1:
                        #joystick 0, button 0 wurde gedruckt
                        self.textPrint.print(self.screen, "{}".format(Game.anweisung1))
                        self.textPrint.print(self.screen, "Es wurde der Button {} gedrückt!".format(i))
                    if j==1 and i in (0,1,2,3) and self.button ==1:
                        #joystick 1, button 0 wurde gedruckt
                        self.textPrint.print(self.screen, "{}".format(Game.anweisung2))
                        self.textPrint.print(self.screen, "Es wurde der Button {} gedrückt!".format(i))
                    #textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
                #textPrint.unindent()
                    
                # Hat switch. All or nothing for direction, not like joysticks.
                # Value comes back in an array.
                self.hats = self.joystick.get_numhats()
                #textPrint.print(screen, "Number of hats: {}".format(hats) )
                #textPrint.indent()

                for i in range( self.hats ):
                    self.hat = self.joystick.get_hat( i )
                    #textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
                #textPrint.unindent()
                
                self.textPrint.unindent()

            
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Limit to 20 frames per second
            self.clock.tick(20)
            
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit ()
if __name__ == "__main__":
    PygView().run()
