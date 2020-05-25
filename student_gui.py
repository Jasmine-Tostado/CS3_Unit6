""" Assignment A6-05 - Jasmine Tostado """
import tkinter as tk
from student import Student
from student import StudentListUtilities


class StudentGUI:
    ORIGINAL_NAME = ""
    ORIGINAL_YEAR = 0
    ORIGINAL_PHONE = "0000000000"
    ORIGINAL_HOUSE_NUM = 0
    ORIGINAL_STREET = "Street Name"
    ORIGINAL_APT_NUM = 0

    def __init__(self):
        self._students = []
        self._name = self.ORIGINAL_NAME
        self._year = self.ORIGINAL_YEAR
        self._phone = self.ORIGINAL_PHONE
        self._house_num = self.ORIGINAL_HOUSE_NUM
        self._street = self.ORIGINAL_STREET
        self._apt_num = self.ORIGINAL_APT_NUM
        self._fetch_index = 0
        self._root = tk.Tk()
        header = "Creating a Student. A student has a name, year, gpa, and " \
                 "classes."
        self._header = tk.Message(self._root, text=header)
        self._header.config(bg="lightpink", width=1000)

        self._name_label = tk.Label(self._root, text="Student Name:")
        self._year_label = tk.Label(self._root, text="Student Grade:")
        self._display_label = tk.Label(self._root, text="-")
        self._name_entry = tk.Entry(self._root)
        self._name_entry.insert(0, str(self._name))
        self._year_entry = tk.Entry(self._root)
        self._year_entry.insert(0, int(self._year))
        self._add_button = tk.Button(self._root, text="Add Student",
                                     command=self.add_student)
        self._display_button = tk.Button(self._root, text="Display Students",
                                         command=self.display_students)
        self._remove_button = tk.Button(self._root, text="Remove Student",
                                        command=self.remove_students)

        self._phone_label = tk.Label(self._root, text="Student Phone #:")
        self._address_label = tk.Label(self._root, text="Student Address:")
        self._phone_entry = tk.Entry(self._root)
        self._phone_entry.insert(0, str(self._phone))
        self._phone_button = tk.Button(self._root, text="Add Phone Number",
                                       command=self.phone_number)

        self._house_num_label = tk.Label(self._root, text="House #:")
        self._street_label = tk.Label(self._root, text="House Street:")
        self._apt_num_label = tk.Label(self._root, text="Apt. #:")
        self._house_num_entry = tk.Entry(self._root)
        self._house_num_entry.insert(0, int(self._house_num))
        self._street_entry = tk.Entry(self._root)
        self._street_entry.insert(0, str(self._street))
        self._apt_num_entry = tk.Entry(self._root)
        self._apt_num_entry.insert(0, int(self._apt_num))
        self._address_button = tk.Button(self._root, text="Add Address",
                                         command=self.address)
        self._fetch_button = tk.Button(self._root, text="Fetch info.",
                                       command=self.fetch_info)

        self._header.grid(row=0, column=0, columnspan=3, pady=10, sticky=tk.EW)
        self._name_label.grid(row=1, column=0, sticky=tk.E)
        self._name_entry.grid(row=1, column=1, sticky=tk.W)
        self._year_label.grid(row=2, column=0, sticky=tk.E)
        self._year_entry.grid(row=2, column=1, sticky=tk.W)
        self._display_label.grid(row=1, column=0, sticky=tk.W)

        self._phone_label.grid(row=3, column=0, sticky=tk.E)
        self._phone_entry.grid(row=3, column=1, sticky=tk.W)
        self._address_label.grid(row=4, column=0, sticky=tk.E)
        self._house_num_label.grid(row=5, column=0, sticky=tk.W)
        self._street_label.grid(row=6, column=0, sticky=tk.W)
        self._apt_num_label.grid(row=7, column=0, sticky=tk.W)
        self._house_num_entry.grid(row=5, column=1, sticky=tk.E)
        self._street_entry.grid(row=6, column=1, sticky=tk.E)
        self._apt_num_entry.grid(row=7, column=1, sticky=tk.E)

        self._add_button.grid(row=8, column=0, pady=1)
        self._address_button.grid(row=8, column=1, pady=1)
        self._phone_button.grid(row=8, column=2, pady=1)
        self._display_button.grid(row=8, column=3, pady=1)
        self._remove_button.grid(row=8, column=4, pady=1)
        self._fetch_button.grid(row=8, column=5, pady=1)

    @property
    def root(self):
        """ Returns self._root """
        return self._root

    def add_student(self):
        """ Adds a student to the student list. """
        self._name = str(self._name_entry.get())
        self._year = int(self._year_entry.get())
        student = Student(self._name, self._year)
        self._students.append(student)
        success_label = tk.Label(self._root, text="Student Added successfully")
        success_label.grid(row=9, column=0, sticky=tk.W)

    def phone_number(self):
        """ Adds the student's phone number"""
        self._phone = str(self._phone_entry.get())
        index = StudentListUtilities.binary_search(self._students, self._name)
        try:
            self._students[index].phone = self._phone
            success_label = tk.Label(self._root,
                                     text="Phone # added successfully")
            success_label.grid(row=9, column=2, sticky=tk.E)

        except ValueError:
            error_label = tk.Label(self._root, text="Invalid Phone Number")
            error_label.grid(row=9, column=2, sticky=tk.E)

    def address(self):
        """ Adds the student's address"""

        self._house_num = int(self._house_num_entry.get())
        self._street = str(self._street_entry.get())
        self._apt_num = int(self._apt_num_entry.get())
        index = StudentListUtilities.binary_search(self._students, self._name)
        try:
            self._students[index].address = self._house_num, self._street, \
                                            self._apt_num
            success_label = tk.Label(self._root,
                                     text="Address added successfully")
            success_label.grid(row=9, column=1, sticky=tk.E)

        except ValueError:
            error_label = tk.Label(self._root, text="Invalid Address")
            error_label.grid(row=9, column=1, sticky=tk.E)
        except TypeError:
            error_label = tk.Label(self._root, text="Invalid Address")
            error_label.grid(row=9, column=1, sticky=tk.E)

    def display_students(self):
        """ Displays the students. """
        student_str = StudentListUtilities.to_string(self._students)
        student_str_label = tk.Label(self._root, text=student_str)
        student_str_label.grid(row=10, column=1, sticky=tk.W)

    def remove_students(self):
        """ Removes a student from the list. """
        name_removed = ""
        name_removed_label = tk.Label(self._root, text="Name of Student Being "
                                                       "removed:")
        name_removed_entry = tk.Entry(self._root)
        name_removed_entry.insert(0, str(name_removed))

        index = StudentListUtilities.binary_search(self._students,
                                                   name_removed)
        remove_button = tk.Button(self._root, text="Remove",
                                  command=self._students.pop(index))
        name_removed_label.grid(row=11, column=1, sticky=tk.W)
        name_removed_entry.grid(row=11, column=1, sticky=tk.E)
        remove_button.grid(row=11, column=2, sticky=tk.E)

    def fetch_info(self):
        """ Fetches info about a student. """
        name = ""
        name_label = tk.Label(self._root, text="Name of Student whose info. "
                                               "you're searching for:")
        name_entry = tk.Entry(self._root)
        name_entry.insert(0, str(name))
        name = str(name_entry.get())
        self._fetch_index = StudentListUtilities.binary_search\
            (self._students, name)
        enter_button = tk.Button(self._root, text="Enter",
                                 command=self.fetch_info_h)
        name_label.grid(row=13, column=0, sticky=tk.W)
        name_entry.grid(row=13, column=1, sticky=tk.E)
        enter_button.grid(row=13, column=2, pady=1)

    def fetch_info_h(self):
        print(self._fetch_index, self._students[self._fetch_index])
        fetch_label = tk.Label(self._root, text=str(self._students[self._fetch_index]))
        fetch_label.grid(row=14, column=1, sticky=tk.W)


def main():
    student = StudentGUI()
    student.root.mainloop()


main()
