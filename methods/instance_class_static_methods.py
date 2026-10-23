"""Compare instance, class, and static methods using temperature conversion.

Run with: python methods/instance_class_static_methods.py
"""


# PUBLIC_INTERFACE
class Temperature:
    """Store a Celsius temperature and provide conversion helpers."""

    # PUBLIC_INTERFACE
    def __init__(self, celsius):
        """Initialize an instance with a numeric Celsius temperature."""
        self.celsius = celsius

    # PUBLIC_INTERFACE
    def to_fahrenheit(self):
        """Return this instance's temperature in Fahrenheit."""
        # An instance method receives self and uses that object's data.
        return self.celsius * 9 / 5 + 32

    # PUBLIC_INTERFACE
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create a temperature from a numeric Fahrenheit value."""
        # A class method receives cls, so subclasses keep their own type.
        return cls(cls.fahrenheit_to_celsius(fahrenheit))

    # PUBLIC_INTERFACE
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert a numeric Fahrenheit value without creating an object."""
        # A static method needs neither instance state nor class state.
        return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    room = Temperature(20)
    print(f"Instance method: {room.celsius:g} C = {room.to_fahrenheit():g} F")

    freezing = Temperature.from_fahrenheit(32)
    print(f"Class method: 32 F creates a temperature of {freezing.celsius:g} C")

    boiling_celsius = Temperature.fahrenheit_to_celsius(212)
    print(f"Static method: 212 F = {boiling_celsius:g} C (no instance needed)")
