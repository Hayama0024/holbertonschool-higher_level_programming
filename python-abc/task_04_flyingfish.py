#!/usr/bin/env python3


class Fish:
    """Base class representing fish behavior."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Base class representing bird behavior."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class demonstrating multiple inheritance.
    Combines behaviors of both Fish and Bird.
    """

    def swim(self):
        """Overrides swim behavior from Fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides fly behavior from Bird."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides habitat to combine characteristics of both parents."""
        print("The flying fish lives both in water and the sky!")
