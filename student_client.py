""" Test: Advanced OOP - Jasmine Tostado """
from student import Student
from student import StudentListUtilities
import random


def main():
    students = [Student("Jacob", 0),
                Student("JP", 10),
                Student("Jonathan", 8),
                Student("Jasmine", 10),
                Student("Francisco", 11),
                Student("Bresy", 11)
                ]

    print(f"***STUDENT LIST WITH DEFAULT VALUES:***"
          f"{StudentListUtilities.to_string(students)}")

    for i in range(len(students)):
        birth_date = f"{random.randint(1, 31)}/{random.randint(1, 12)}" \
                     f"/{random.randint(1900, 2020)}"
        try:
            students[i].date = birth_date
        except ValueError:
            print(f"Failed to set birth date {birth_date} for "
                  f"{students[i].name}")

    print(f"\n***STUDENT LIST WITHOUT DEFAULT VALUES:***"
          f"{StudentListUtilities.to_string(students)}")

    try:
        students[3].date = "-9/23/122"
    except ValueError:
        print(f"Failed to set birth date -9/23/122 for "
              f"{students[3].name}")

    StudentListUtilities.merge_sort(students)
    print(f"\n***LIST AFTER SORTING:***"
          f"{StudentListUtilities.to_string(students)}")


main()
