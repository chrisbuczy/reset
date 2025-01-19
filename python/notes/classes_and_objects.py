
class things:
    def boggi(self):
        print('boggi rocks')
        pass
class inanimate(things):
    pass
class animate(things):
    pass
class sidewalks(inanimate):
    pass
class animals(animate):
    def breath(self):
        print('breathing')    
        pass
    def move (self):
        print('moving')
        pass
    def eat_food(self):
        print('eating food')
        pass
class mammals(animals):
    def feed_young_with_milk(self):
        print('feeding young')
        pass
class giraffes(mammals):
    def find_food(self):
        self.move()
        print("i've found food!")
        self.eat_food()
        pass
    def eat_leaves_from_trees(self):
        self.eat_food()
        pass
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
        pass
    def left_foot_forward(self):
        print('left foot forward')
        pass
    def rightfootforward(self):
        print('right foot forward')
        pass
    def leftfootback(self):
        print('left foot back')
        pass
    def rightfootback(self):
        print('right foot back')  
        pass  
    def dance(self):
        self.left_foot_forward()
        self.rightfootforward()
        self.leftfootback()
        self.rightfootback()
    def test(self, name):
        print (f'hello {name}')
        pass
harold = giraffes()
reginald = giraffes()

reginald.test('christian')

