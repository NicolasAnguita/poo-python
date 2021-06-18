class Auto:
    def __init__(self, rendimiento):
        self.x = 0
        self.km = 0
        self.rendimiento= rendimiento
        self.combustible=0
#haz que el auto cargue combustible
    def petrolear(self, combustible):
        self.combustible += combustible
        return self


    def mover(self, x):
        if x > (self.combustible*self.rendimiento):
            print("No tiene bencina suficiente")
        else:
            self.x = x
            self.km += x
            self.combustible -= x/(self.rendimiento)  
        return self
    
suzuki = Auto(12)
suzuki.mover(1000)
suzuki.petrolear(200).mover(10).mover(40)
print(f"El auto tiene {suzuki.combustible} lts de combustible y su km actual es {suzuki.km}")
suzuki.mover(20).mover(400)
print(f"El auto tiene {suzuki.combustible} lts de combustible y su km actual es {suzuki.km}")



