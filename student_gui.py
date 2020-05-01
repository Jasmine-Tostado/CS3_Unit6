""" Assignment A6-05 - Jasmine Tostado """
import tkinter as tk
from student import Student

# Is this supposed to be inside a class
student1 = tk.Tk()
header = tk.Message(text="Creating a Student. A student has a name, "
                         "year, gpa, and classes.")
header.config(bg="lightpink", width=1000)
name1_label = tk.Label(text="Student Name:")
name1_entry = tk.Entry()
name1 = name1_entry.insert(0, str())
# do I use properties instead?
name1_button = tk.Button(text="Enter", command=Student(name1))

year_label = tk.Label(text="Student Grade:")
year_entry = tk.Entry()
year = year_entry.insert(0, int())
# do I use properties instead?
year_button = tk.Button(text="Enter", command=Student(8, year))

header.grid(row=0, column=0, columnspan=3, pady=10, sticky=tk.EW)
name1_label.grid(row=1, column=0, sticky=tk.E)
name1_entry.grid(row=1, column=1, sticky=tk.W)
name1_button.grid(row=1, column=2, pady=2)

year_label.grid(row=2, column=0, sticky=tk.E)
year_entry.grid(row=2, column=1, sticky=tk.W)
year_button.grid(row=2, column=2, pady=2)


student1.mainloop()
