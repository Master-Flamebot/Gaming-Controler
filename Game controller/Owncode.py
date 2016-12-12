import pygame
pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print ( j.get_name())
def get():
    while True:
        out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        it = 0 #iterator
        pygame.event.pump()
        for i in range(0, j.get_numaxes()):
            out[it] = j.get_axis(i)
            it+=1
        for i in range(0, j.get_numbuttons()):
            out[it] = j.get_button(i)
            it+=1
        return out
def bob():
    pygame.event.pump()
    while True:
        pygame.event.pump()
        x = j.get_button(3)
        print (x)
def dog():
    while True:
        pygame.event.pump()
        x = j.get_button(3)
        if x == 1:
            print (4)
        if x == 0:
            print (0)
        pygame.event.pump()
        y = j.get_button(2)
        if y == 1:
            print (3)
        if y == 0:
            print (0)
def cat():
    while True:
        pygame.event.pump()
        x = j.get_button(3)#4
        y = j.get_button(2)#3
        if x == 1 and y ==0:#just number 4 is pressed
            print (4)
        if x == 0 and y ==1:#just number 3 is pressed
            print (3)
        if x == 0 and y ==0:#neither are pressed
            print (0)
        if x == 1 and y ==1:#both are pressed
            print (34)
def fish():
    while True:
        pygame.event.pump()
        x = j.get_button(3)#4
        y = j.get_button(2)#3
        w = j.get_button(1)#2
        z = j.get_button(0)#1
        #       4          3          2          1
        if x == 1 and y == 0 and w == 0 and z == 0:#Only button 4 is pressed
            print (4)
        if x == 0 and y == 1 and w == 0 and z == 0:#Only button 3 is pressed
            print (3)
        if x == 0 and y == 0 and w == 1 and z == 0:#Only button 2 is pressed
            print (2)
        if x == 0 and y == 0 and w == 0 and z == 1:#Only button 1 is pressed
            print (1)
        if x == 0 and y == 0 and w == 0 and z == 0:#None are pressed
            print (0)
        if x == 0 and y == 0 and w == 1 and z == 1:#buttons 1 and 2 are pressed
            print (12)
        if x == 0 and y == 1 and w == 0 and z == 1:#buttons 1 and 3 are pressed
            print (13)
        if x == 1 and y == 0 and w == 0 and z == 1:#buttons 1 and 4 are pressed
            print (14)
        if x == 0 and y == 1 and w == 1 and z == 0:#buttons 2 and 3 are pressed
            print (23)
        if x == 1 and y == 0 and w == 1 and z == 0:#buttons 2 and 4 are pressed
            print (24)
        if x == 1 and y == 1 and w == 0 and z == 0:#buttons 3 and 4 are pressed
            print (34)
        if x == 1 and y == 1 and w == 1 and z == 1:#All are pressed
            print (1234)
        if x == 0 and y == 1 and w == 1 and z == 1:#buttons 1, 2, and 3 are pressed
            print (123)
        if x == 1 and y == 1 and w == 1 and z == 0:#buttons 2, 3, and 4 are pressed
            print (234)
        if x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 3, and 4 are pressed
            print (134)
        if x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 2, and 4 are pressed
            print (124)

def chicken():
    while True:
        pygame.event.pump()
        a = j.get_button(4)#L1
        b = j.get_button(5)#R1
        c = j.get_button(6)#L2
        d = j.get_button(7)#R2
        #       L1         L2         R1         R2
        if a == 1 and c == 0 and b == 0 and d == 0:#Only L1 is pressed
            print ("L1")
        if a == 0 and c == 1 and b == 0 and d == 0:#Only L2 is pressed
            print ("L2")
        if a == 0 and c == 0 and b == 1 and d == 0:#Only R1 is pressed
            print ("R1")
        if a == 0 and c == 0 and b == 0 and d == 1:#Only R2 is pressed
            print ("R2")
        if a == 0 and c == 0 and b == 0 and d == 0:#None are pressed
            print (0)
        if a == 0 and c == 0 and b == 1 and d == 1:#buttons R1 and R2 are pressed
            print ("R1 and R2")
        if a == 1 and c == 1 and b == 0 and d == 0:#buttons L1 and L2 are pressed
            print ("L1 and L2")
        if a == 0 and c == 1 and b == 0 and d == 1:#buttons R2 and L2 are pressed
            print ("R2 and L2")
        if a == 1 and c == 0 and b == 1 and d == 0:#buttons R1 and L1 are pressed
            print ("R1 and L1")
        if a == 1 and c == 0 and b == 0 and d == 1:#buttons R2 and L1 are pressed
            print ("R2 and L1")
        if a == 0 and c == 1 and b == 1 and d == 0:#buttons R1 and L2 are pressed
            print ("R1 and L2")
        if a == 1 and c == 1 and b == 1 and d == 1:#All are pressed
            print ("R1, R2, L1, and L2")
        if a == 0 and c == 1 and b == 1 and d == 1:#buttons R1, R2, and L2 are pressed
            print ("R1, R2, and L2")
        if a == 1 and c == 0 and b == 1 and d == 1:#buttons R1, R2, and L1 are pressed
            print ("R1, R2, and L1")
        if a == 1 and c == 1 and b == 0 and d == 1:#buttons R2, L1, and L2 are pressed
            print ("R2, L1, and L2")
        if a == 1 and c == 1 and b == 1 and d == 0:#buttons R1, L1, and L2 are pressed
            print ("R1, L1, and L2")

"""
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#
            print()
"""
def snake():
    while True:
        pygame.event.pump()
        x = j.get_button(0)#1
        y = j.get_button(1)#2
        w = j.get_button(2)#3
        z = j.get_button(3)#4
        a = j.get_button(4)#L1
        b = j.get_button(5)#R1
        c = j.get_button(6)#L2
        d = j.get_button(7)#R2
    #----------------------------------------------------------All Regular--------------------------------------------------------------------    
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#Only L1 pressed
            print("L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#Only L2 pressed
            print("L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#Only R1 pressed
            print("R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#Only R2 pressed
            print("R2")
            
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#Only button 1 pressed
            print(1)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#Only button 2 pressed
            print(2)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#Only button 3 pressed
            print(3)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#Only button 4 pressed
            print(4)
    #-----------------------------------------------------------4's--------------------------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#None are pressed
            print(0)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#All numbers pressed
            print(1234)
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#All triggers pressed
            print("R1, R2, L1, and L2")
    #-----------------------------------------------------------All 2 Combos-----------------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1 and 2 are pressed
            print(12)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1 and 3 are pressed
            print(13)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1 and 4 are pressed
            print(14)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2 and 3 are pressed
            print(23)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2 and 4 are pressed
            print(24)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3 and 4 are pressed
            print(34)
            
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#buttons L1 and L2 are pressed
            print("L1 and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#buttons L1 and R1 are pressed
            print("L1 and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons L1 and R2 are pressed
            print("L1 and R2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R1 and R2 are pressed
            print("R1 and R2")
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R1 and L2 are pressed
            print("R1 and L2")
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R2 and L2 are pressed
            print("L2 and R2")
    #-----------------------------------------------------------All 3 Combos----------------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, and 3 are pressed
            print(123)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, and 4 are pressed
            print(234)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, and 4 are pressed
            print(134)
        if a == 0 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, and 4 are pressed
            print(124)
            
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R1, R2, and L2 are pressed
            print("R1, R2, and L2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R1, R2, and L1 are pressed
            print("R1, R2, and L1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R2, L1, and L2 are pressed
            print("R2, L1, and L2")
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 0:#buttons R1, L1, and L2 are pressed
            print("R1, L1, and L2")
    #-----------------------------------------------------------All Mixed 2 Combos----------------------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1 and L1
            print("1 and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1 and L2
            print("1 and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1 and R1
            print("1 and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1 and R2
            print("1 and R2")
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2 and L1
            print("2 and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2 and L2
            print("2 and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2 and R1
            print("2 and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2 and R2
            print("2 and R2")
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3 and L1
            print("3 and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3 and L2
            print("3 and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3 and R1
            print("3 and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3 and R2
            print("3 and R2")
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4 and L1
            print("4 and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4 and L2
            print("4 and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4 and R1
            print("4 and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4 and R2
            print("4 and R2")
    #-----------------------------------------------------------All Mixed 2 Numbered Combos 1---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, and L1
            print("1, 2, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, and L2
            print("1, 2, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, and R1
            print("1, 2, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, and R2
            print("1, 2, and R2")
            
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, and L1
            print("1, 3, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, and L2
            print("1, 3, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, and R1
            print("1, 3, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, and R2
            print("1, 3, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, and L1
            print("1, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, and L2
            print("1, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, and R1
            print("1, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, and R2
            print("1, 4, and R2")
    #-----------------------------------------------------------All Mixed 2 Numbered Combos 2 & 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4       
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, and L1
            print("2, 3, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, and L2
            print("2, 3, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, and R1
            print("2, 3, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, and R2
            print("2, 3, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, and L1
            print("2, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, and L2
            print("2, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, and R1
            print("2, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, and R2
            print("2, 4, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, and L1
            print("3, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, and L2
            print("3, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, and R1
            print("3, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, and R2
            print("3, 4, and R2")
    #-----------------------------------------------------------All Mixed 3 Numbered Combos---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, and L1
            print("1, 2, 3, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, and L2
            print("1, 2, 3, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, and R1
            print("1, 2, 3, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, and R2
            print("1, 2, 3, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, and L1
            print("2, 3, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, and L2
            print("2, 3, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, and R1
            print("2, 3, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, and R2
            print("2, 3, 4, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, and L1
            print("1, 3, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, and L2
            print("1, 3, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, and R1
            print("1, 3, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, and R2
            print("1, 3, 4, and R2")

        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, and L1
            print("1, 2, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, and L2
            print("1, 2, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, and R1
            print("1, 2, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, and R2
            print("1, 2, and R2")
    #-----------------------------------------------------------All Mixed 4 Numbered Combos---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 0 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, and L1
            print("1, 2, 3, 4, and L1")
        if a == 0 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, and L2
            print("1, 2, 3, 4, and L2")
        if a == 0 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, and R1
            print("1, 2, 3, 4, and R1")
        if a == 0 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, and R2
            print("1, 2, 3, 4, and R2")
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------All Mixed 2 trigger Combos with one number---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, and L2
            print("1, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, and R1
            print("1, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, and R2
            print("1, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, R1, and L2
            print("1, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, R1, and R2
            print("1, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, R2, and L2
            print("1, R2, and L2")
            
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, and L2
            print("2, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, and R1
            print("2, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, and R2
            print("2, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, R1, and L2
            print("2, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, R1, and R2
            print("2, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, R2, and L2
            print("2, R2, and L2")

        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, and L2
            print("3, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, and R1
            print("3, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, and R2
            print("3, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, R1, and L2
            print("3, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, R1, and R2
            print("3, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, R2, and L2
            print("3, R2, and L2")

        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, and L2
            print("4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, and R1
            print("4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, and R2
            print("4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, R1, and L2
            print("4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, R1, and R2
            print("4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, R2, and L2
            print("4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 1 and 2---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, and L2
            print("1, 2, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, and R1
            print("1, 2, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, and R2
            print("1, 2, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, R1, and L2
            print("1, 2, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, R1, and R2
            print("1, 2, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, R2, and L2
            print("1, 2, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 1 and 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, and L2
            print("1, 3, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, and R1
            print("1, 3, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, and R2
            print("1, 3, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, R1, and L2
            print("1, 3, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, R1, and R2
            print("1, 3, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, R2, and L2
            print("1, 3, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 1 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, and L2
            print("1, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, and R1
            print("1, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, and R2
            print("1, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, R1, and L2
            print("1, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, R1, and R2
            print("1, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, R2, and L2
            print("1, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 2 and 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, and L2
            print("2, 3, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, and R1
            print("2, 3, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, and R2
            print("2, 3, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, R1, and L2
            print("2, 3, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, R1, and R2
            print("2, 3, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, R2, and L2
            print("2, 3, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 2 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, and L2
            print("2, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, and R1
            print("2, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, and R2
            print("2, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, R1, and L2
            print("2, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, R1, and R2
            print("2, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, R2, and L2
            print("2, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 3 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, and L2
            print("3, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, and R1
            print("3, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, and R2
            print("3, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, R1, and L2
            print("3, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, R1, and R2
            print("3, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, R2, and L2
            print("3, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 1, 2, and 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, and L2
            print("1, 2, 3, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, and R1
            print("1, 2, 3, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, and R2
            print("1, 2, 3, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, R1, and L2
            print("1, 2, 3, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, R1, and R2
            print("1, 2, 3, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, R2, and L2
            print("1, 2, 3, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 2, 3, and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, and L2
            print("2, 3, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, and R1
            print("2, 3, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, and R2
            print("2, 3, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, R1, and L2
            print("2, 3, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, R1, and R2
            print("2, 3, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, R2, and L2
            print("2, 3, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with  1, 2, and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, and L2
            print("1, 2, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, and R1
            print("1, 2, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, and R2
            print("1, 2, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, R1, and L2
            print("1, 2, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, R1, and R2
            print("1, 2, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, R2, and L2
            print("1, 2, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with  1, 3, and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, and L2
            print("1, 2, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, and R1
            print("1, 2, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, and R2
            print("1, 2, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, R1, and L2
            print("1, 2, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, R1, and R2
            print("1, 2, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, R2, and L2
            print("1, 2, 4, R2, and L2")
    #-----------------------------------------------------------All Mixed 2 trigger Combos with 1, 2, 3, and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 0 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, and L2
            print("1, 2, 3, 4, L1, and L2")
        if a == 1 and c == 0 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, and R1
            print("1, 2, 3, 4, L1, and R1")
        if a == 1 and c == 0 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, and R2
            print("1, 2, 3, 4, L1, and R2")
            
        if a == 0 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, R1, and L2
            print("1, 2, 3, 4, R1, and L2")
        if a == 0 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, R1, and R2
            print("1, 2, 3, 4, R1, and R2")
        
        if a == 0 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, R2, and L2
            print("1, 2, 3, 4, R2, and L2")
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------All Mixed 3 trigger Combos with one number---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, L2, and R1
            print("1, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, L2, and R2
            print("1, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, R1, L2, and R2
            print("1, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, R1, and R2
            print("1, L1, R1, and R2")

        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, L2, and R1
            print("2, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, L2, and R2
            print("2, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, R1, L2, and R2
            print("2, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, R1, and R2
            print("2, L1, R1, and R2")
            
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, L2, and R1
            print("3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, L2, and R2
            print("3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, R1, L2, and R2
            print("3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, R1, and R2
            print("3, L1, R1, and R2")
            
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, L2, and R1
            print("4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, L2, and R2
            print("4, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, R1, L2, and R2
            print("4, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, R1, and R2
            print("4, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 4 trigger Combos with one number---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, L2, R1, and R2
            print("1, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, L2, R1, and R2
            print("2, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, L2, R1, and R2
            print("3, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, L2, R1, and R2
            print("4, L1, L2, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 1 and 2---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, L2, and R1
            print("2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, L2, and R2
            print("2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, R1, L2, and R2
            print("2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, R1, and R2
            print("2, 3, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 1 and 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, L2, and R1
            print("2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, L2, and R2
            print("2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, R1, L2, and R2
            print("2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, R1, and R2
            print("2, 3, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 1 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, L2, and R1
            print("2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, L2, and R2
            print("2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, R1, L2, and R2
            print("2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, R1, and R2
            print("2, 3, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 2 and 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, L2, and R1
            print("2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, L2, and R2
            print("2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, R1, L2, and R2
            print("2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, R1, and R2
            print("2, 3, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 2 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, L2, and R1
            print("2, 4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, L2, and R2
            print("2, 4, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, R1, L2, and R2
            print("2, 4, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, R1, and R2
            print("2, 4, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 3 and 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, L2, and R1
            print("2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, L2, and R2
            print("2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, R1, L2, and R2
            print("2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, R1, and R2
            print("2, 3, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, L2, and R1
            print("1, 2, 3, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, L2, and R2
            print("1, 2, 3, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, R1, L2, and R2
            print("1, 2, 3, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, R1, and R2
            print("1, 2, 3, L1, R1, and R2")

        if a == 1 and c == 1 and b == 1 and d == 0 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, L2, and R1
            print("2, 3, 4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, L2, and R2
            print("2, 3, 4, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, R1, L2, and R2
            print("2, 3, 4, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, R1, and R2
            print("2, 3, 4, L1, R1, and R2")

        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, L2, and R1
            print("1, 3, 4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, L2, and R2
            print("1, 3, 4, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, R1, L2, and R2
            print("1, 3, 4, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, R1, and R2
            print("1, 3, 4, L1, R1, and R2")

        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, L2, and R1
            print("1, 2, 4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, L2, and R2
            print("1, 2, 4, L1, L2, and R2")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, R1, L2, and R2
            print("1, 2, 4, R1, L2, and R2")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, R1, and R2
            print("1, 2, 4, L1, R1, and R2")
    #-----------------------------------------------------------All Mixed 3 trigger Combos with 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 0 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, L2, and R1
            print("1, 2, 3, 4, L1, L2, and R1")
        if a == 1 and c == 1 and b == 0 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, L2, and R2
            print("1, 2, 3, 4, L1, L2, and R1")
        if a == 0 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, R1, L2, and R2
            print("1, 2, 3, 4, L1, L2, and R1")
        if a == 1 and c == 0 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, R1, and R2
            print("1, 2, 3, 4, L1, L2, and R1")
    #-----------------------------------------------------------All Mixed 4 trigger Combos with 1---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 0:#buttons 1, L1, L2, R1, and R2
            print("1, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 0:#buttons 2, L1, L2, R1, and R2
            print("2, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 0:#buttons 3, L1, L2, R1, and R2
            print("3, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 0 and z == 1:#buttons 4, L1, L2, R1, and R2
            print("4, L1, L2, R1, and R2")
    #-----------------------------------------------------------All Mixed 4 trigger Combos with 2---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 0:#buttons 1, 2, L1, L2, R1, and R2
            print("1, 2, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 0:#buttons 1, 3, L1, L2, R1, and R2
            print("1, 3, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 0 and z == 1:#buttons 1, 4, L1, L2, R1, and R2
            print("1, 4, L1, L2, R1, and R2")

        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 0:#buttons 2, 3, L1, L2, R1, and R2
            print("2, 3, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 0 and z == 1:#buttons 2, 4, L1, L2, R1, and R2
            print("2, 4, L1, L2, R1, and R2")
            
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 0 and w == 1 and z == 1:#buttons 3, 4, L1, L2, R1, and R2
            print("3, 4, L1, L2, R1, and R2")
    #-----------------------------------------------------------All Mixed 4 trigger Combos with 3---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 0:#buttons 1, 2, 3, L1, L2, R1, and R2
            print("1, 2, 3, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 0 and y == 1 and w == 1 and z == 1:#buttons 2, 3, 4, L1, L2, R1, and R2
            print("2, 3, 4, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 0 and w == 1 and z == 1:#buttons 1, 3, 4, L1, L2, R1, and R2
            print("1, 3, 4, L1, L2, R1, and R2")
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 0 and z == 1:#buttons 1, 2, 4, L1, L2, R1, and R2
            print("1, 2, 4, L1, L2, R1, and R2")
    #-----------------------------------------------------------All Mixed 4 trigger Combos with 4---------------------------------------------------------
    #           L1         L2         R1         R2         1          2          3          4
        if a == 1 and c == 1 and b == 1 and d == 1 and x == 1 and y == 1 and w == 1 and z == 1:#buttons 1, 2, 3, 4, L1, L2, R1, and R2
            print("1, 2, 3, 4, L1, L2, R1, and R2")

def bird():
    while True:
        """
        pygame.event.pump()
        BV=[1,2,3,4,5,6,7,8]
        for s in range(0,6):
            BV[s] = j.get_button(s)
            if BV[s] == 1: 
                print(s + 1)
                
                if BV[1] == 1 and s != BV[2]:
                    print(BV[1],BV[2])
        """
        pygame.event.pump()
        TextV=[1,2,3,4,"L1","R1","L2","R2","S1","S2"]
        BV=[0,0,0,0,0,0,0,0,0,0]
        BV2=[0,0,0,0,0,0,0,0,0,0]
        
        for s in range(0,10):
            BV[s] = j.get_button(s)
            if BV[s] == 1:
                print(TextV[s])
                
        
        """        
        for b in range(0,10):
            BV2[b] = j.get_button(s)
            if BV2[b] == 1 and BV2[b] != BV[s]:
                print("  ,TextV[s]")
        """
def catdog():
    while True:
        pygame.event.pump()
        TextV=[1,2,3,4,"L1","R1","L2","R2","S1","S2"]
        BV=[0,0,0,0,0,0,0,0,0,0]
        #TextV2=[1,2,3,4,"L1","R1","L2","R2","S1","S2"]
        #BV2=[0,0,0,0,0,0,0,0,0,0]

        for s in range(0,10):
            BV[s] = j.get_button(s)
        for s in range(0,10):
            if BV[s] == 1:
                c ,= BV[s],
                print(c)
            
        
        """
        for b in range(0,10):
            BV2[b] = j.get_button(b)
            print(TextV[s],TextV2[b])
        """
def duck():
    while True:
        pygame.event.pump()
        TextV=["1","2","3","4","L1","R1","L2","R2","S1","S2"]
        BV=[0,0,0,0,0,0,0,0,0,0]
        Q=","
        for y in range(0,10):
            BV[y] = j.get_button(y)
        for x in range(0,10):
            if BV[x] == 1:
                Q += TextV[x]
        print(Q)

def thing():
    while True:
        print("hi")
        
        
def test():
    while True:
        print( bob())
        
    
