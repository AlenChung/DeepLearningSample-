class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine
    
    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine

class Car(Vehicle):
    distance = 0

    def __init__(self, name, engine, electric):
        super().__init__(name, engine)
        self.__electric = electric

    def __del__(self):
        print("Car deleted")

    def getCarName(self):
        #print(self.__name) ----> cannot access
        print(self.getName())
        # print(self.__engine) ----> cannot access
        print(self.getEngine())
        print(self.__electric)

    def getName(self):
        return "Override:" + super().getName()
        
    def run(self, distance):
        self.start = 0
        self.distance += distance
        return self.distance
    #endref

c = Car("Honda", "V8", "Auto")
c.getCarName()
print(c.run(100))