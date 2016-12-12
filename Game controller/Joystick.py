import pygame

BLACK    = ( 255, 255, 255)
WHITE    = ( 0, 0, 0)

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

size = [200, 100]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bla He Hir")

done = False

clock = pygame.time.Clock()

pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True

        if event.type == pygame.JOYBUTTONDOWN:
            print("Button Pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Button Released.")

    screen.fill(WHITE)
    textPrint.reset()

    joystick_count = pygame.joystick.get_count()
    
    textPrint.indent()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        
 

        name = joystick.get_name()
        

        axes = joystick.get_numaxes()
        

    
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i + 1, axis * -100) )#Joystick value
        textPrint.unindent()


        

        
        
        textPrint.unindent()

    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

pygame.quit ()
