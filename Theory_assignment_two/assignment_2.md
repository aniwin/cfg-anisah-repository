
## 1. How does Object Oriented Programming differ from Process Oriented Programming? 

Procedural oriented programming is based on subroutines or procedure calls. Consist of sequential steps to perform specified tasks.

Object oriented programming is a programming paradigm that uses objects and classes in programming.

Main differences:

| Process Oriented programming                                             | Object oriented programming                               |   |
|--------------------------------------------------------------------------|-----------------------------------------------------------|---|
| Top-down approach                                                        | Bottom up approach                                        |   |
| Program is subdivided into objects                                       | Program is subdivided into objects                        |   |
| It is less secure because it doesn’t have a way of hiding data           | It is more secure because it has a way of hiding data     |   |
| Doesn’t have concept of access specifiers                                | Uses access specifiers for encapsulation                  |   |
| Languages that use procedure-oriented programming: FORTRAN, ALGOL, COBOL | Languages that use OOP programming: Python, Java, C++, C# |   |
| Overloading is not possible                                              | Overloading is possible                                   |   |
| No dating hiding and inheritance                                         | Has data hiding and inheritance                           |   |
| Uses the concept of procedure abstraction                                | Uses concept of data abstraction                          |   |
| Adding new data and functions is not easy                                | Adding new data and functions is easy                     |   |


## 2. What's polymorphism in OOP? 

Polymorphism is the condition of occurrence in different forms. It is the use of a single type entity (method, operator or object) to represent different scenarios.

Example of an inbuilt function with polymorphism is the len() function.
```python
# #inbuilt function len() with polymorphism
#
len("hello")
len(["Dog","Cat","Mouse"])

```

Polymorphism is implemented through method overloading and method overriding.

Method overriding is a method that uses the same name in both the parent and child class. 

Example:
```python
# class Animal:
#     def print_details(self):
#         print("This is parent Animal class method")
#
#
# class Horse(Animal):
#     def print_details(self):
#         print("This is child Horse class method")
#
#
# class Cat(Animal):
#     def print_details(self):
#         print("This is child Cat class method")
#
#
# animal_a = Animal()
# animal_a. print_details()
#
# horse_b = Horse()
# horse_b.print_details()
#
# cat_c = Cat()
# cat_c.print_details()
#
```
Method overloading is a property of a method to behave differently depending on number and types of parameters.

Example:

```python
 # method overloading
#
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def sum(self, a=None, b=None, c=None):
#         s = 0
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#         elif a!=None and b!=None:
#             s = a + b
#         else:
#             s = a
#         return s
#
# studentsum_2 = Student(50,12)
#
# print(studentsum_2.sum(4,6,5))
#

```

## 3. What's inheritance in OOP? 

It is the transfer of the characteristics of a class to other classes that are derived from it.

The types of inheritance in python are:

- Single inheritance – when a derived (child) class inherits from a single parent (base) class
```python
#
# class Animal:
#     def print_details_1(self):
#         print("This is parent Animal class method")
#
#
# class Horse(Animal):
#     def print_details_2(self):
#         print("This is child Horse class method")
#
# object = Horse()
# object.print_details_1()
# object.print_details_2()
```
- Multiple inheritance – this is where a class is derived from more than one base class

```python

#
# class Mother:
#     def mother_method(self):
#         print("This is parent Mother class method")
#
# class Father:
#     def father_method(self):
#         print("This is parent Father class method")
#
# class Child(Mother, Father):
#     def child_method(self):
#         print("This is child Child class method")
#
# child_a = Child()
# child_a.mother_method()
# child_a.father_method()
# child_a.child_method()
#
```
- Multilevel inheritance- inheritance when a derived (child) class inherits another derived (child) class

```python
# # multi-level inheritance when a derived (child) class inherits another derived (child) class
#
# class Organism:
#
#     alive = True
#
# class Animal(Organism):
#
#     def eat(self):
#         print("Animal is eating")
#
# class Dog(Animal):
#
#     def bark(self):
#         print("This dog is barking")
#
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()
```

Hierarchical inheritance - more than one derived (child) class is created from a single parent (base) class

```python
class Animal:
    def run(self, name):
        self.name = name
        print(f'{self.name} is running')

class Dog(Animal):
    def jumping(self):
        print("Dog is jumping")

class Cat(Animal):
    def sleeping(self):
        print("Cat is sleeping")

d = Dog()
d.run("Dog")
d.jumping()
c = Cat()
c.run("Cat")
c.sleeping()
```

## 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people? 

Each person in the office should be only to vote for one person each. They shouldn't be able to vote multiple times. 

\1) Create a model class for Employee. This class should contain class variables such as employee id, name, Voted employee and Vote count. Voted Employee is again an instance to the Employee class and it is used to contain the object of which person an employee is voting. Vote count is used later to store the number of votes each employee received for being the funniest 

\2) The program should create and populate the list of employees. This will include employee id and name of the employee 

\3) After creating all the employee details, the program will get the vote of each employee. The votedEmployee field will be set for each employee. 

\4) Since votedEmployee is an instance to Employee itself, the voteCount will be set for the votedEmployee object. 

\5) The program will iterate through the list of employees and find the employees who have the top 3 vote count. To do this, the program will store the first 3 employee ids and vote count in a temp list of objects, traverse through the list and update the list as it finds an employee with a higher vote count. 

\6) The top 3 funniest people chosen based on votes must be displayed to the user.

## 5. What's the software development cycle? 

It is a methodology used to build software. It defines responsibilities for team members during each step of phase. The software development cycle has distinct stages.

The stages of the software development cycle are:

1) Planning- In this stage project leaders look at labor, material costs, creating timetable and including feedback from stakeholders. The purpose of the project is clearly defined.
1) Requirements – What the project is meant to do and its requirements are determined. The resources also needed for the project are decided.
1) Design – In this stage system and software design  documents are prepared as per requirement specification. 2 types of design documents are developed in this phase:

High-level Design(HLD)

- Description and name of each module
- Outline of functionality of every module
- Interface relationship and dependencies between modules
- Database tables identified along with key elements
- Complete architecture diagrams with technology details
-
-
Low-Level Design (LLD)

- Functional logic of modules
- Complete detail of interface
- Dealing with all types of dependency issues
- Inputs and outputs for every module
- Listing of error messages


4)Implementation

This is where the developers code using chosen programming languages. Tasks are devided into units or modules and assigned to different developers. The implementation phase os the longest phase of the SDLC process.


5)Testing

Once the software is completed it is deployed in the testing environment. The testing team check the functionality of the entire system. This is to verify that the entire application works to the customers needs. Testing involves:

-Unit Testing
-Module Testing
-Sub-system Testing
-System Testing
-Acceptance Testing


6)Evaluation

Once a system has been delivered to the end user/client it undergoes a post-implementation review. The delivered system should then fully evaluate on the basis of its
-effectiveness, usability and maintainability


7)Maintenance 

Once the software is deployed and is used by customers.

The software will be maintained by fixing bugs, undergoing upgrades and enhancement through the addition of new features.


## 6.What's the difference between agile and waterfall? 

|     Agile                                                      |     Waterfall                                    |   |   |   |
|----------------------------------------------------------------|--------------------------------------------------|---|---|---|
|     Multiple lifecycle phases can run in   parallel            |     Isolated phases that flow into each other    |   |   |   |
|     Continuous iteration of development and   testing          |     Structured software development process      |   |   |   |
|     Not as useful for small development   projects             |     Better suited for smaller sized projects     |   |   |   |
|     Incremental approach                                       |     Sequential design process                    |   |   |   |
|     Testing occurs concurrently with software   development    |     Testing comes after the building phase       |   |   |   |
|                                                                |                                                  |   |   |   |







## 7. What is a reduced function used for? 

Reduce() is used for applying a function to an iterable and reducing it to a single cumulative value. It performs function on first two elements and repeats process until 1 value remains.

```python
#example of a reduced function
import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y, :x + y,letters)
print(word)
```

## 8. How does merge sort work 

A merge sort is a sorting algorithm that is based on divide and conquer. An array is divided into two. The subarray are then divided again and again until the arrays only have one element each.  Then pairs of one-element arrays are sorted and are merged with other pairs until the initial array is sorted.

```python
# example of merge sort function taken from https://www.geeksforgeeks.org/merge-sort/

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)
```
## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case? 

A use case for generators can be for reading very large files instead of reading files line by line.

```python

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
 ```


## 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator? 

A decorator is a function which takes another function as an argument and returns a modified version of it, enhancing its functionality in some way.

Types of decorators include simple decorators, chaining decorators and universal decorators.

Simple decorators – uses a single decorator, function and wrapper
```python
# example for simple decorator

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")


        func()

        print("After function has been executed")

    return inner1



def sleeping():
    print("I'm sleeping")


function_to_be_used = hello_decorator(sleeping)

# calling the function
function_to_be_used()

# you can also use the decorator using the @ symbol along with the name of the decorator function

@hello_decorator
def sleeping():
    print("I'm sleeping")
```
Universal decorators that can work with any number of parameters

```python
# example of a universal decorator

def run_func_twice_decorator(func):
    def wrapper_run_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_run_twice


@run_func_twice_decorator
def divide(a, b):
    print(a/b)

```
Chaining decorators is when you are decorating a function with multiple decorators

```python
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())
```
