class Car: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} has stopped.")

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} is honking.")