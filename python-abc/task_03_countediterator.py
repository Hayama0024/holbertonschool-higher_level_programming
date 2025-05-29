#!/usr/bin/env python3


class CountedIterator:
    """An iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with any iterable and a counter set to zero."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over so far."""
        return self.count
