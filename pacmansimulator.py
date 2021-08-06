
import unittest


class Pacman:

    def __init__(self):
        self.grid = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
        self.x = 0
        self.y = 0
        self.placed = False
        self.maxX = 4
        self.maxY = 4
        self.direction = ""

    def place(self,command):
        command_parts = command.split(",")
      
        
        if(self.maxX < int(command_parts[0][-1]) or self.maxY < int(command_parts[1])):
            print("Invalid command as it will take pacman out of grid.")
            return
        self.x = self.x + int(command_parts[0][-1])
        self.y = self.y + int(command_parts[1])
        self.direction = command_parts[2].strip()
        self.maxX = 4-self.x
        self.maxY = 4-self.y


    def report(self):
        return "Output: "+str(self.x)+","+str(self.y)+","+self.direction

    def move(self):
        if self.direction=="NORTH" and self.maxY<4:
            self.y = self.y+1
            self.maxY = 4-self.y
        elif self.direction=="EAST" and self.maxX<4:
            self.x = self.x+1
            self.maxX = 4-self.x

        elif self.direction == "WEST" and self.maxX>0:
            self.x = self.x -1
            self.maxX = 4-self.X

        elif self.direction =="SOUTH" and self.maxY>0:
            self.y = self.y-1
            self.maxY = 4-self.y

            
    def left(self):
        if self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "EAST":
            self.direction = "NORTH"
        elif self.direction == "WEST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
    def right(self):
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "WEST":
            self.direction = "NORTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        
        
        

class PacmanTests(unittest.TestCase):
      
    def test1(self):        
        pacman = Pacman()


        pacman.place("PLACE 0,0, NORTH")
        pacman.move()
        self.assertEqual(pacman.report(),'Output: 0,1,NORTH')
        print("*************** Test 1 passed ***************\n")

    def test2(self):
        
        pacman = Pacman()
        pacman.place("PLACE 0,0, NORTH")
        pacman.left()
        self.assertEqual(pacman.report(),'Output: 0,0,WEST')
        print("*************** Test 2 passed ***************\n")
    def test3(self):        
        pacman = Pacman()


        pacman.place("PLACE 1,2, EAST")
        pacman.move()
        pacman.move()
        pacman.left()
        pacman.move()
        pacman.report()
        self.assertEqual(pacman.report(),'Output: 3,3,NORTH')
        print("*************** Test 3 passed ***************\n")

if __name__ == '__main__':
    unittest.main()   
            
