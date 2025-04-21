# *args
def add(*args):
    print(args[1])
    
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs 
def caculate(n, **kwagrs):
    # print(kwagrs)
    n += kwagrs["add"]
    n *= kwagrs["multiply"]
    # print(n)
caculate(2, add=3, multiply=5)



# E.g
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model= kw["model"]
        self.colour = kw["colour"]
        self.seats= kw["seats"]
my_car = Car(make="Nissan", model="GT-R", colour="red", seats=4)
print(my_car)