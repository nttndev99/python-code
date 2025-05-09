class Person:
    def __init__(self, age):
        self._age = age   
         
    def get_age(self):
        return self.get_age   
        
    def set_age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Age must be within [18, 99]")
        
class PersonPythonic:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Age must be within [18, 99]")
        
person = PersonPythonic(39)
print(person.age)

person.age = 42
print(person.age)

person.age = 100

