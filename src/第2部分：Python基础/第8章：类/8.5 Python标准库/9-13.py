from random import randint

class Die():
    
    def __init__(self, times, sides=6):
        self.sides = sides
        self.times = times
        
    def roll_die(self):
        for i in range(1, self.times):
            tmp = randint(1,self.sides)
            print(tmp, end=',')
        print("\n")

touzi_1 = Die(10, 6)
touzi_1.roll_die()


touzi_2 = Die(10, 10)
touzi_2.roll_die()

touzi_3 = Die(10, 20)
touzi_3.roll_die()
