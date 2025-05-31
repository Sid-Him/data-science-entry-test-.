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
            
# I've completed the Car class as per your instructions. Class Definition (Car):
# The __init__ method now correctly initializes the make, model, and year attributes for each Car object created.
# The describe_car method is implemented to print the car's information in the "Year Make Model" format using the object's attributes.

# Task 2
# Create an instance of the Car class
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Call the describe_car method on the instance
my_car.describe_car()

# An instance of the Car class, named my_car, has been created with the specified attributes: Make "Toyota", Model "Corolla", and Year 2020.
# The describe_car() method is then called on this my_car instance, which will print "2020 Toyota Corolla".
