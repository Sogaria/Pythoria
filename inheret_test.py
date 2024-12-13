class Dog:
    def __init__(self):
        self.feet = 4
        self.wuff = 0
    
    def bellen(self):
        print("wuff wuff")
        self.wuff += 1

class DisabledLabrador(Dog):
    def __init__(self):
        super().__init__()
        self.feet = 3

dog = Dog()
labrador = DisabledLabrador()

print(dog.feet)
print(labrador.feet)

print(f"Amount dog speaked so far: {dog.wuff}")
print(f"Labrador speaked so far: {labrador.wuff}")
dog.bellen()
print(f"2. Amount dog speaked so far: {dog.wuff}")
print(f"2. Labrador speaked so far: {labrador.wuff}")