#!/usr/bin/env python3

# Mixin class that provides swimming behavior
class SwimMixin:
    def swim(self):
        # Print a swimming message using the instance's name
        print(f"{self.name} swims!")


# Mixin class that provides flying behavior
class FlyMixin:
    def fly(self):
        # Print a flying message using the instance's name
        print(f"{self.name} flies!")


# Dragon class that inherits both swimming and flying capabilities
class Dragon(SwimMixin, FlyMixin):
    def __init__(self, name):
        # Initialize the dragon's name
        self.name = name

    def roar(self):
        # Print a roaring message using the instance's name
        print(f"{self.name} roars!")
