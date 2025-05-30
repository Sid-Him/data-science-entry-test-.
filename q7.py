# Task 1
def __init__(self, make, model, year):
        """
        Initializes a new Car object.

        Args:
            make (str): The make of the car (e.g., "Toyota").
            model (str): The model of the car (e.g., "Corolla").
            year (int): The manufacturing year of the car (e.g., 2020).
        """
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        """
        Prints information about the car in the format "Year Make Model".
        """
        print(f"{self.year} {self.make} {self.model}")
# Task 2
# Create an instance of the Car class
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Call the describe_car method on the instance
my_car.describe_car()
