""" A5-08 - Jasmine Tostado"""


class Array:

    # class constants
    DEFAULT_SIZE = 6
    DEFAULT_VALUE = "Tutorial"

    def __init__(self, list_size=DEFAULT_SIZE, initial_value=DEFAULT_VALUE):
        if list_size > 0:
            self._list_size = list_size
        else:
            self._list_size = self.DEFAULT_SIZE
        self._data = [initial_value for _ in range(self._list_size)]

    def __getitem__(self, index):
        """ Returns the item in the array located at the given index. """
        if self.valid_index(index):
            return self._data[index]
        else:
            return IndexError

    def __setitem__(self, index, value):
        """ Sets the value of the array at the given index. """
        if self.valid_index(index):
            if type(value) == str:
                self._data[index] = value
            else:
                raise TypeError
        else:
            raise IndexError

    def valid_index(self, index):
        """ Checks if the index given is valid. """
        if 0 <= index < self._list_size:
            return True
        else:
            return False

    def __str__(self):
        """ Returns a string of the class in the correct format. """
        list_string = ""
        for item in self._data:
            list_string += item + ", "
        return list_string

    def __len__(self):
        """ Returns the size of the list. """
        return self._list_size
