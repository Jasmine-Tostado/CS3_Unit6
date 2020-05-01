""" Assignment A5-09 - Jasmine Tostado """


class Stack:

    # class constants
    MAX_CAPACITY = 1000
    DEFAULT_VALUE = "No value"
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY, initial_value=DEFAULT_VALUE):
        if self.valid_capacity(capacity):
            self._capacity = capacity
        else:
            self._capacity = self.DEFAULT_CAPACITY
        self._stack = [initial_value for _ in range(self._capacity)]
        self._initial_value = initial_value
        self._tos = 0

    def push(self, value):
        """ Pushes an item to the top of the stack. """
        if self._tos + 1 > self._capacity:
            raise OverflowError
        elif type(value) != type(self._initial_value):
            raise TypeError
        self._stack[self._tos] = value
        self._tos += 1

    def pop(self):
        """ Removes the item at the top of the list. """
        if self._tos > 0:
            self._tos -= 1
        else:
            raise IndexError

    def top_item(self):
        """ Returns the item at the top of the list. """
        return self._stack[self._tos]

    @property
    def capacity(self):
        """ Returns the capacity. """
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        """ Sets the new capacity if it is valid. """
        if self.valid_capacity(new_capacity) and self._capacity < new_capacity:
            default_list = [self.DEFAULT_VALUE
                            for _ in range(new_capacity - self._capacity)]
            self._stack += default_list
            self._capacity = new_capacity
        else:
            raise ValueError

    def valid_capacity(self, new_capacity):
        """ Returns True when the new capacity is within the limits. """
        if 0 < new_capacity < self.MAX_CAPACITY:
            return True
        else:
            return False

    def __str__(self):
        """ Returns a string of the stack's items in the correct format. """
        items_str = ""
        for i in range(self._tos):
            items_str += f"'{self._stack[i]}' "

        return items_str

    def __len__(self):
        """ Returns the length of the list without default values. """
        # for _ in range(self._)
        return self._tos
