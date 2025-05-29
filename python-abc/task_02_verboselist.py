class VerboseList(list):
    """A custom list that prints messages when modified."""

    def append(self, item):
        """Add a single item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list with multiple items and print a message."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove a single item from the list and print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index (default last), print a message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
