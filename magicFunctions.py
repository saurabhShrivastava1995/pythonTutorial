
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")


print(len(ford))
print(ford[0])
print(ford[1])