class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self) -> bool:
        print(f"Starting {self.brand} {self.model} {self.year}")
        return True
    
    def stop(self) -> bool:
        print(f"Stopping {self.brand} {self.model} {self.year}")
        return True
    
    
class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_seats: int):
        super().__init__(brand, model, year)
        self.num_seats = num_seats

    def drive(self) -> bool:
        print(f"Driving {self.brand} {self.model} {self.year}")
        return True
    
    def lock_doors(self) -> bool:
        print(f"Locking doors of {self.brand} {self.model} {self.year}")
        return True
    
    def unlock_doors(self) -> bool:
        print(f"Unlocking doors of {self.brand} {self.model} {self.year}")
        return True
    
    def __str__(self) -> str:
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, num_seats={self.num_seats})"
        
        
car = Car("Toyota", "Corolla", 2020, 5)

print(car.start())
print(car.stop())

print(car.num_seats)
