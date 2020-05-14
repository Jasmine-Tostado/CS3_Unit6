""" Assignment A6-05 - Jasmine Tostado """
import tkinter as tk
from student import Student
from student import StudentListUtilities


class StudentGUI:
    ORIGINAL_NAME = ""
    ORIGINAL_YEAR = 0

    def __init__(self):
        self._students = []
        self._name = self.ORIGINAL_NAME
        self._year= self.ORIGINAL_YEAR
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

        # self._name_button = tk.Button(self._root, text="Enter",
        #                               command=Student(self._name))
        # self._year_button = tk.Button(self._root, text="Enter",
        #                               command=Student(8, self._year))
        self._add_button = tk.Button(self._root, text="Add Student",
                                     command=self.add_student())
        self._display_button = tk.Button(self._root, text="Display Students",
                                         command=self.display_students())
        self._remove_button = tk.Button(self._root, text="Remove Student",
                                        command=self.remove_students())

        self._header.grid(row=0, column=0, columnspan=3, pady=10, sticky=tk.EW)
        self._name_label.grid(row=1, column=0, sticky=tk.E)
        self._name_entry.grid(row=1, column=1, sticky=tk.W)
        self._year_label.grid(row=2, column=0, sticky=tk.E)
        self._year_entry.grid(row=2, column=1, sticky=tk.W)
        self._display_label.grid(row=1, column=0, sticky=tk.W)

        self._add_button.grid(row=3, column=0, pady=1)
        self._display_button.grid(row=3, column=1, pady=1)

    @property
    def root(self):
        return self._root

    def add_student(self):
        # display info on screen
        # update self._students
        self._name = str(self._name_entry.get())
        self._year = int(self._year_entry.get())

        print(f"name: {self._name} year: {self._year}")
        student = Student(self._name, self._year)
        self._students.append(student)
        # self._label (' you've entered a student with name: self.name and age self.age')

    def display_students(self):
        student_string = StudentListUtilities.to_string(self._students)
        # print(student_string)
        # yb self._display_label.config(tk.Label(text=str(f"{student_string}")))
        # self._display_label.grid(row=0, column=0, sticky=tk.W)

    def remove_students(self):
        name_removed = ""
        name_removed_label = tk.Label(self._root, text="Name of Student You "
                                                       "want to remove:")
        name_removed_entry = tk.Entry(self._root)
        name_removed_entry.insert(0, str(name_removed))
        self._students.remove(name_removed)


    """
    def show_all_student(self):
        pass

    def delete_student(self):
        # remove that student from self._students
    """


def main():
    student = StudentGUI()
    # breakpoint()
    student.root.mainloop()
    # breakpoint()
    # print(student.root)


main()