
from abc import ABC, abstractmethod
# Abstract class
class Vehicle(ABC):

    def __init__(self, persons):
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass


# Two Wheeler
class TwoWheeler(Vehicle):

    def calculate_toll(self):
        toll = 20

        if self.persons > 2:
            toll += (self.persons - 2) * 10

        return toll


# Three Wheeler
class ThreeWheeler(Vehicle):

    def calculate_toll(self):
        toll = 30

        if self.persons > 3:
            toll += (self.persons - 3) * 20

        return toll


# Four Wheeler
class FourWheeler(Vehicle):

    def calculate_toll(self):
        toll = 40

        if self.persons > 4:
            toll += (self.persons - 4) * 40

        return toll


# Heavy Vehicle
class HeavyVehicle(Vehicle):

    def calculate_toll(self):
        toll = 60

        if self.persons > 6:
            toll += (self.persons - 6) * 100

        return toll


# Main program
def main():

    while True:
        print("----- TOLL MENU -----")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Thank you!")
            break

        persons = int(input("Enter number of persons: "))

        if choice == 1:
            vehicle = TwoWheeler(persons)

        elif choice == 2:
            vehicle = ThreeWheeler(persons)

        elif choice == 3:
            vehicle = FourWheeler(persons)

        elif choice == 4:
            vehicle = HeavyVehicle(persons)

        else:
            print("Invalid choice!")
            continue

        # Polymorphic behavior
        print("Toll Amount = Rs.", vehicle.calculate_toll())
main()