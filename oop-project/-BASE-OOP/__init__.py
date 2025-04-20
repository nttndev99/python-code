class Reactangle:
    def __init__(self, side_a, side_b): # Constructor
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self):
        return self.side_a * self.side_b

r1 = Reactangle(10, 4)

print(r1.side_a, r1.side_b) # 10  4
print(r1.area()) # 40

r2 = Reactangle(7, 3) 
print(r2.area()) # 21

