class A:
    name = None
    age = None
    happiness = None

    def set_data(self, name, age, happiness):
        self.name = name
        self.age = age
        self.happiness = happiness
    
    def get_data(self):
        print(self.name, self.age, self.happiness)
    
    def __init__(self, name=None, age=None, happiness=None):
        self.set_data(name, age, happiness)
        self.get_data()
    
Sasha = A("Sasha", 19, 1)

