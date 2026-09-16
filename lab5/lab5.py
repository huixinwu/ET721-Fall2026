"""
student's full name
lab 5: review of class, object, methods, and attributes
Sep 16, 2026
"""
print("\n---- Example 1: class Circle ------")
class Circle():
    # values that need to pass to the object of class Circle
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    # attributes 
    pi = 3.14157

    # method
    def circumference(self):
        return 2*self.pi*self.r

    

# create instance object of the class
c1 = Circle(2, "red")
print(c1.c)
print(c1.circumference())

print("\n---- Example 2: class Rectangle ------")


class Rectangle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    # method to calculate the area
    def area(self):
        return self.w * self.h

    # method to calculate the perimeter
    def perimeter(self):
        return 2*self.w + 2*self.h

    # method to draw the rectangle
    """
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0),self.w, self.h, fc=self.c))
        plt.axis('scaled')
        plt.show()
        """

# create instance object of the class
r1 = Rectangle(2,3, "olive")
print(f"The perimeter of rectangle with height = {r1.h} and width = {r1.w} is {r1.perimeter()}")

"""
Car dealership's inventory management system
You are working on a Python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately
Task 1: create a class to represent each vehicle. Each car should have attributes for maximum speed and mileage
Task 2: update the class with the default color for all vehicles, "white"
Task 3: create a class method to assign seating capacity to a vehicle
Task 4: create a class method to display all the properties of an object class --> "The ___(color) car has ___ seats, with ___ miles and a maximum speed of ___"
Task 5: create two instance objects of the car. One car will have a max speed of 200kph and mileage of 50000 kmpl with five seating capacity. The other car max speed = 180 kph, mileage = 75000kmpl, four-seating
"""