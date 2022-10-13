"""
TASK 1
Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items
Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""

class CashRegister:

    def __init__(self):
        self.total_items = {}

    def add_item(self, item, price):
        self.item = item
        self.price = price
        self.total_items[item] = price

    def remove_item(self, item):
        self.item = item
        self.total_items.pop(item)

    def apply_discount(self, discount): # discount must be entered as percentage
        self.discount = discount
        for name, price in self.total_items.items():
            self.total_items[name] = self.total_items[name] - round((price * discount)/100, 2)


    def get_total(self):
        total_cost = sum([price for price in self.total_items.values()])
        return total_cost

    def show_items(self):
        return self.total_items

    def reset_register(self):
        self.total_items = {}


# EXAMPLE code run:
basket = CashRegister()
basket.add_item('fish', 10)
basket.add_item('bread', 1.50)
basket.add_item('chocolate', 1)
basket.show_items()
basket.get_total()
basket.apply_discount(50)
basket.show_items()
basket.get_total()
basket.remove_item('bread')
basket.show_items()



"""
TASK 2
Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.
Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 
"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def show(self):
        print(f'Name:{self.name}, Age: {self.age}, id_no: {self.id},subjects taken and grades:{self.subjects}')

class CFGStudent(Student):
    def __init__(self, name, age, id):
        Student.__init__(self, name, age, id)

    def add_subject_grade(self, subject_name, grade):
        self.subject_name = subject_name
        self.grade = grade
        self.subjects[subject_name] = grade

    def remove_subject_grade(self, subject_name):
       self.subject_name = subject_name
       self.subjects.pop(subject_name)

    def view_all_subjects(self):
        return self.subjects

    def overall_marks(self):
        avg_mark = sum(self.subjects.values()) / len(self.subjects)
        return f'Average grade:{avg_mark}'


ani = CFGStudent('hafsa', 23, 3)
ani.show()
ani.add_subject_grade('foundation', 12)
ani.add_subject_grade('project', 16)
ani.show()
ani.view_all_subjects()
ani.overall_marks()
ani.remove_subject_grade('project')
ani.view_all_subjects()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)