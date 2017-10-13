import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()
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



# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    #textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.print(screen, "{}".format(anweisung0))
    textPrint.indent()
    
    # For each joystick:
    for j in range(joystick_count):
        joystick = pygame.joystick.Joystick(j)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(j) )
        #textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        #textPrint.print(screen, "Number of axes: {}".format(axes) )
        #textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            #textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        #textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        #textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        #textPrint.indent()
        # wir wollen button0
        for i in range( buttons ):
            button = joystick.get_button( i )
            if j==0 and i==0 and button==1:
                #joystick 0, button 0 wurde gedruckt
                textPrint.print(screen, "{}".format(anweisung1))
            if j==1 and i==0 and button==1:
                #joystick 1, button 0 wurde gedruckt
                textPrint.print(screen, "{}".format(anweisung2))
            #textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        #textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        #textPrint.print(screen, "Number of hats: {}".format(hats) )
        #textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            #textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        #textPrint.unindent()
        
        textPrint.unindent()

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
