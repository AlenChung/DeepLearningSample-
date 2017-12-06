class Boat:
    color = "white"
    distance = 0

    def __init__(self):
        self.distance = 0
    
    def __del__(self):
        print("Boat deleted")

    def run(self, distance):
        self.start = 0
        self.distance += distance / 10
    #endref
