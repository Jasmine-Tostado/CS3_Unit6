""" Test: Advanced OOP - Jasmine Tostado """
from array import Array


class Student:
    # class constants
    DEFAULT_NAME = "No Name"
    ORIGINAL_DEFAULT_YEAR = 6
    NAME_LEN_MAX = 20
    CLASS_NAME_MAX = 25
    MIN_YEAR = 6
    MAX_YEAR = 12
    ORIGINAL_GPA_DEFAULT = 0
    MIN_GPA = 0
    MAX_GPA = 4

    # class variables aka class attributes
    next_id = 1
    default_year = ORIGINAL_DEFAULT_YEAR
    default_gpa = ORIGINAL_GPA_DEFAULT

    def __init__(self, name=DEFAULT_NAME, year=None, gpa=None):
        if year is None:
            year = self.default_year
        if gpa is None:
            gpa = self.default_year
        try:
            self.name = name
        except ValueError:
            self._name = self.DEFAULT_NAME
        except TypeError:
            self._name = self.DEFAULT_NAME
        try:
            self.year = year
        except ValueError:
            self._year = self.ORIGINAL_DEFAULT_YEAR
        try:
            self.gpa = gpa
        except ValueError:
            self._gpa = self.ORIGINAL_GPA_DEFAULT
        self._classes = Array()
        self._id = self.next_id
        self.update_next_id()
        self._phone = self.PhoneNumber()
        self._address = self.Address()
        self._date = self.Date()

    def __str__(self):
        """Returns a print statement about the info. of each student"""
        print_info = f"\nStudent ID: {self._id}, Name: {self._name}, " \
                     f"Year: {self._year} \nPhone: {str(self._phone)}, " \
                     f"Address: {str(self._address)} " \
                     f"\nClasses: {str(self._classes)}" \
                     f"\nBirth Date: {self._date}"
        return print_info

    def display(self):
        """ Calls __str__ when client wants student displayed"""
        print(self)

    def __gt__(self, other):
        """ Compares which student should comes earlier based on birth dates.
        Returns True whenever self is greater than other."""
        if self.date > other.date:
            return True
        else:
            return False

    def same_grade(self, other):
        """ Checks if the students are in the same grade. """
        if self._year == other.year:
            return True
        else:
            return False

    @classmethod
    def valid_year(cls, new_year):
        """Checks if years entered are within the minimums and maximums."""
        if cls.MIN_YEAR <= new_year <= cls.MAX_YEAR:
            return True
        else:
            return False

    @classmethod
    def set_default_year(cls, new_default_year):
        """Sets default year."""
        if cls.valid_year(new_default_year):
            cls.default_year = new_default_year
        else:
            raise ValueError

    @classmethod
    def get_default_year(cls):
        """ Return default year."""
        return cls.default_year

    @classmethod
    def update_next_id(cls):
        """Updates the next id for next student."""
        cls.next_id += 1

    @property
    def name(self):
        """Returns Student's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Initializes name or raises exceptions."""
        if type(new_name) != str:
            raise TypeError
        elif len(new_name) > self.NAME_LEN_MAX:
            raise ValueError
        else:
            self._name = new_name

    @property
    def year(self):
        """Returns Student's year."""
        return self._year

    @year.setter
    def year(self, new_year):
        """After valid_year called, year is initialized or exception raised."""
        if self.valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError

    @property
    def classes(self):
        """ Returns list of classes."""
        return str(self._classes)

    def add_class(self, period_num, class_name):
        """ Sets the class_name into the array.  """
        self._classes[period_num] = class_name

    @classmethod
    def set_default_gpa(cls, default_gpa):
        """ Sets the new default gpa if it is valid. """
        if cls.MIN_GPA <= default_gpa <= cls.MAX_GPA:
            cls.default_gpa = default_gpa
        else:
            raise ValueError

    @classmethod
    def get_default_gpa(cls):
        """ Returns the default_gpa"""
        return cls.default_gpa

    @property
    def gpa(self):
        """Returns gpa."""
        return self._gpa

    @gpa.setter
    def gpa(self, new_gpa):
        """Initializes gpa or raises exceptions when necessary."""
        if self.MIN_GPA <= new_gpa <= self.MAX_GPA:
            self._gpa = new_gpa
        else:
            raise ValueError

    def id_getter(self):
        """ Returns the student's id. """
        return self._id

    @property
    def phone(self):
        """ Returns student's phone number """
        return self._phone

    @phone.setter
    def phone(self, new_number):
        """ Calls number property inside Phone Class to set phone number. """
        self._phone.number = new_number

    @property
    def address(self):
        """ Returns a string of the student's address"""
        return str(self._address)

    @address.setter
    def address(self, new_address):
        """ Unpacks the new_address tuple in order to set address. """
        house_num, street_name, apt_num = new_address
        self._address.house_num = house_num
        self._address.street_name = street_name
        self._address.apt_num = apt_num

    @property
    def date(self):
        """ Returns self._date"""
        return self._date

    @date.setter
    def date(self, new_date):
        """ Calls date property inside Date class to set birth date. """
        self._date.date = new_date

    """ DATE CLASS """

    class Date:
        # class constants
        DEFAULT_DATE = "1/1/2000"

        def __init__(self, date=DEFAULT_DATE):
            try:
                self._date = date
            except ValueError:
                self._date = self.DEFAULT_DATE

        def __str__(self):
            """ Returns self._date so it can be printed as a string. """
            return self._date

        def __gt__(self, other):
            """ Checks which student was born first.
             Returns True whenever self is greater than other. """
            self_list = self.date.split("/")
            other_list = other.date.split("/")
            if self_list[2] > other_list[2]:
                return True
            else:
                if self_list[2] == other_list[2]:
                    if self_list[1] > other_list[1]:
                        return True
                    elif self_list[1] == other_list[1]:
                        if self_list[0] > other_list[0]:
                            return True
            return False

        @property
        def date(self):
            """ Returns the birth date. """
            return self._date

        @date.setter
        def date(self, new_date):
            """ Sets the birth date of a student after sanity checking."""
            date_list = new_date.split("/")
            if 1 > int(date_list[0]) or int(date_list[0]) > 31:
                raise ValueError
            elif 1 > int(date_list[1]) or int(date_list[1]) > 12:
                raise ValueError
            elif 1900 > int(date_list[2]) or int(date_list[2]) > 2020:
                raise ValueError
            else:
                self._date = new_date

    """ ADDRESS CLASS """

    class Address:
        # class constants
        MIN_HOUSE_NUM = 0
        MIN_APT_NUM = 0
        MAX_APT_NUM = 1000
        DEFAULT_HOUSE_NUM = 0
        DEFAULT_STREET_NAME = "No Street Name"
        DEFAULT_APT_NUM = 0

        def __init__(self, house_num=DEFAULT_HOUSE_NUM,
                     street_name=DEFAULT_STREET_NAME, apt_num=DEFAULT_APT_NUM):
            try:
                self.house_num = house_num
            except ValueError:
                self._house_num = self.DEFAULT_HOUSE_NUM
            try:
                self.street_name = street_name
            except TypeError:
                self._street_name = self.DEFAULT_STREET_NAME
            try:
                self.apt_num = apt_num
            except ValueError:
                self._apt_num = self.DEFAULT_APT_NUM

        @property
        def house_num(self):
            """ Returns the house number."""
            return self._house_num

        @house_num.setter
        def house_num(self, new_house_num):
            """ Sets the house number after sanity checking. """
            if self.MIN_HOUSE_NUM < new_house_num:
                self._house_num = new_house_num
            else:
                raise ValueError

        @property
        def street_name(self):
            """ Returns the street name."""
            return self._street_name

        @street_name.setter
        def street_name(self, new_street_name):
            """ Sets the street name after sanity checking. """
            if type(new_street_name) == str:
                self._street_name = new_street_name
            else:
                raise TypeError

        @property
        def apt_num(self):
            """ Returns the apartment number. """
            return self._apt_num

        @apt_num.setter
        def apt_num(self, new_apt_num):
            """ Sets the apartment number after sanity checking. """
            if self.MIN_APT_NUM < new_apt_num <= self.MAX_APT_NUM:
                self._apt_num = new_apt_num
            else:
                raise ValueError

        @staticmethod
        def which_address_closer(address1, address2):
            """Compares 2 addresses and returns the one that is ahead
             alphabetically."""
            if address1.street_name < address2.street_name:
                return address1
            else:
                return address2

        def __str__(self):
            """ Returns the address in correct format. """
            if self._street_name != self.DEFAULT_STREET_NAME and \
                    self._house_num != self.DEFAULT_HOUSE_NUM and \
                    self._apt_num != self.DEFAULT_APT_NUM:
                address = f"\n{self._house_num} {self._street_name} Street, " \
                          f"#{self._apt_num}"
                return address
            else:
                return "<None>"

    """" CLASS PHONE NUMBER """

    class PhoneNumber:
        # class constants
        MAX_NUM_LEN = 20
        NUM_OF_DIGITS = 10
        DEFAULT_PHONE = "0000000000"
        INTEGER_STRING = "0123456789"

        def __init__(self, phone_number=DEFAULT_PHONE):
            try:
                self.number = phone_number
            except TypeError:
                self._phone_number = self.DEFAULT_PHONE
            except ValueError:
                self._phone_number = self.DEFAULT_PHONE

        @property
        def number(self):
            """ Returns instance variable phone_number. """
            return str(self._phone)

        @number.setter
        def number(self, new_phone):
            """ Sets instance variable phone_number. """
            returned_num = self.get_valid_num(new_phone)
            if returned_num is None:
                raise ValueError
            self._phone = returned_num

        @classmethod
        def get_valid_num(cls, phone_number):
            """ Checks if string of the number entered is valid and returns it. """
            if type(phone_number) != str:
                return None
            elif cls.MAX_NUM_LEN < len(phone_number):
                return None
            else:
                extracted_num = cls.extract_digits(phone_number)
                if len(extracted_num) != cls.NUM_OF_DIGITS:
                    return None
            return extracted_num

        @classmethod
        def extract_digits(cls, phone_number):
            """ Removes the non-digit characters from the string. """
            extracted_num = ""
            for ch in phone_number:
                if ch in cls.INTEGER_STRING:
                    extracted_num += ch
            return extracted_num

        def __str__(self):
            """ Prints the phone number in the correct format. """
            phone_string = "("
            first_three_digits = ""
            next_three_digits = ""
            last_four_digits = ""
            for i in range(self.NUM_OF_DIGITS):
                if i <= 2:
                    first_three_digits += self._phone[i]
                elif 3 <= i <= 5:
                    next_three_digits += self._phone[i]
                else:
                    last_four_digits += self._phone[i]
            phone_string += first_three_digits + ") " + \
                            next_three_digits + "-" + last_four_digits
            return phone_string


class StudentListUtilities:
    # class constants
    NOT_FOUND = -1

    @staticmethod
    def to_string(student_list):
        """ Prints the info. for each student in a list of student objects. """
        student_info = ""
        for student in student_list:
            student_info += f"{str(student)}\n"
        return student_info

    @staticmethod
    def sort(student_list):
        """ Sorts through the list of students alphabetically. """
        for i in range(len(student_list) - 1):
            for x in range(len(student_list) - 1):
                if student_list[x] > student_list[x + 1]:
                    student_list[x], student_list[x + 1] = \
                        student_list[x + 1], student_list[x]

    @classmethod
    def linear_search(cls, student_list, name):
        """ Returns the index of the name in the list through linear search."""
        for i in range(len(student_list)):
            if name == student_list[i].name:
                return i
        return cls.NOT_FOUND

    @classmethod
    def binary_search(cls, student_list, name):
        """ Returns the index of the name in the list through binary search."""
        index = cls.binary_search_h(student_list, name, 0,
                                    len(student_list) - 1)
        return index

    @classmethod
    def binary_search_h(cls, student_list, name, start, end):
        """ Returns the index of the student in the list using recursion. """
        midpoint = (start + end) // 2
        mid_name = student_list[midpoint].name
        if name == mid_name:
            return midpoint
        elif abs(end - start) == 1:
            return cls.NOT_FOUND
        else:
            if name > mid_name:
                start = midpoint + 1
                return cls.binary_search_h(student_list, name, start, end)
            else:
                end = midpoint - 1
                return cls.binary_search_h(student_list, name, start, end)

    @classmethod
    def selection_sort(cls, student_list):
        """ Sorts through a list of Student objects using selection sort. """
        end_index = len(student_list) - 1
        for i in range(len(student_list) - 1):
            large_index = cls.get_largest_index(student_list, end_index + 1)
            student_list[large_index], student_list[end_index] = \
                student_list[end_index], student_list[large_index]
            end_index -= 1

    @staticmethod
    def get_largest_index(student_list, length):
        """ Returns the index of the largest item in the list. """
        largest_index = 0
        for i in range(length):
            if student_list[i] > student_list[largest_index]:
                largest_index = i
        return largest_index

    @staticmethod
    def insertion_sort(student_list):
        """ Sorts the list through insertion sort. """
        length = len(student_list)
        for i in range(1, length):
            unsorted = student_list[i]
            sorted_index = i - 1
            while sorted_index >= 0 and student_list[sorted_index] > unsorted:
                student_list[sorted_index + 1] = student_list[sorted_index]
                sorted_index -= 1
            sorted_index += 1
            student_list[sorted_index] = unsorted

    @classmethod
    def merge_sort(cls, num_list):
        """ Sorts a list using merge sort. """
        if len(num_list) > 1:
            first_half = num_list[:len(num_list) // 2]
            second_half = num_list[len(num_list) // 2:]
            cls.merge_sort(first_half)
            cls.merge_sort(second_half)
            first_index = 0
            second_index = 0
            list_index = 0

            while first_index < len(first_half) and \
                    second_index < len(second_half):
                if first_half[first_index] > second_half[second_index]:
                    num_list[list_index] = second_half[second_index]
                    second_index += 1
                else:
                    num_list[list_index] = first_half[first_index]
                    first_index += 1
                list_index += 1

            for i in range(first_index, len(first_half)):
                num_list[list_index] = first_half[first_index]
                list_index += 1
                first_index += 1

            for x in range(second_index, len(second_half)):
                num_list[list_index] = second_half[second_index]
                list_index += 1
                second_index += 1
