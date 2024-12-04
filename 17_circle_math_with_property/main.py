import math


class Circle:
    """
    A class representing a circle with properties to calculate its area and circumference.

    Attributes:
        radius (float): The radius of the circle.
        area (float): The area of the circle, calculated as π * radius^2.
        circumference (float): The circumference of the circle, calculated as 2 * π * radius.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self._radius = radius
        self.area = math.pi * radius ** 2
        self.circumference = 2 * math.pi * radius

    def get_radius(self):
        """
        Returns the radius of the circle.

        Returns:
            float: The radius of the circle.
        """
        return self._radius

    @property
    def radius(self):
        """
        The radius property getter.

        Returns:
            float: The current radius of the circle.
        """
        return self.get_radius()

    @radius.setter
    def radius(self, new_radius):
        """
        The radius property setter. Updates the radius and recalculates the area and circumference.

        Args:
            new_radius (float): The new radius to set for the circle.
        """
        self._radius = new_radius
        self.area = math.pi * new_radius ** 2
        self.circumference = 2 * math.pi * new_radius


circle = Circle(99)
print("Radius:", circle.radius)
print("Area:", circle.area)
print("Circumference:", circle.circumference)

circle.radius = 77
print("Radius:", circle.radius)
print("Area:", circle.area)
print("Circumference:", circle.circumference)
