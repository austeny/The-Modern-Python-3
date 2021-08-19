## Variables & Data Types
Goals: 
* Understand how to assign and use variables
* Python variable name restrtctions/conventions
* Why Python is dynamically typed language

Restrictions
- Variables must startwith letter or underscore (_cats)
- Only consist of letters, numbers, and underscores
- Names are case-sensitive (cat != Cat)

Conventions
- snake_case (test_id), lowercase
- UPPER_SNAKE_CASE (cpnstants)
- UpperCamelCase (refers to class)
- dunder (double underscore means leave alone should be private)

Data Types
- Bool
- int
- str
- list: linked list
- dict: map/object

Dyanmic Typing
- Python is flexible about reassigning variables to different types
- variable can change datatype based on how its set (unlike Java)

Special Value (None)
- None: is Pythons version of null

For Loops
- for item in iterable_object:
- iterable_object( range(start, end, increment), ... )
- range(8) prints 0-7
- range(1, 8) prints 1-7
- range(1, 8, 2) prints 1, 3, 5, 7

While Loops
- while conditional_statement:
- Continues to loop while conditional_statement is Truthy

Styling
- PEP8 style guide
- autopep8 tool will auto format

Lists and Objectives
- Lists - Collection or grouping of items
- Objectives - Describe, create and accesss a list of data structure
- Built in methods to modify and copy lists
- Iterate over lists using loops and list comprehensions
- Work with nested lists to build more complex data structures

## Lists
Create
- tasks = ["item1", "item2", "item3"]
- len() - returns item length eg. len(tasks) = 3
- list() - returns created list eg. list(range(1, 5)) = list [1, 2, 3, 4]

Access
- Lists start at 0 index
- print(items[1]) -> "item2"
- Negative index works backwards
- in keyword, check if value in list eg. "item1" in tasks = True

Iterating
- for n in [1, 2, 3, 4]
- while i < len(numbers)

Methods
- append(item), adds 1 item to END of list eg. append(1)
- extend(item, ...), adds * item(s) to END of list eg. extend([1, 2, 3, 4])
- insert(index, item), define position to insert eg. insert(1, "test")
- clear(), removes all items from list
- pop(opt. index), returns and removes last item, or at index
- remove(value), removes passed in value from list will only remove first found if multiple found
- index(val, start, end), returns index of val after start index and before end index
- count(val), returns # of times val exists in list
- sort(), sorts list (in-place)
- reverse(), reverse order of list (in-place) doesn't create new instance
- join(), joins list with first object eg. ' '.join(words) 'Coding is Fun'
- some_list[start:end:step], create copy of portion of list 
    - start or end is required
    - some_list[start:]
    - some_list[:end] (exclusive counting)
    - some_list[start::step]
    - some_list[::step] (can use negative steps) some_list[::-1] will copy a reversed list
    - Reversing List, string[::-1]
    - Modifying poritons of list numbers[1:3] = ['a', 'b', 'c'] updates list values
Swap values in List
- shuffling, sorting, algorithms
- names = ["Austen", "Caroline"]
- names[0], names[1] = names[1], names[0] -> ["Caroline", "Austen"]

List Comprehension
- Shorthand syntax to generate new list based on modification defined
- [ ___ for ___ in ___ ]
- Manipulate based on for and in
```
nums = [1, 2, 3] 
[ x*10 for x in nums ]
[10, 20, 30]
```
- List Comprehension with Conditional Logic
```
numbers = [1, 2, 3, 4, 5, 6]
[num for num in numbers if num % 2 == 0] returns even numbers in list
[2, 4, 6]
[num*2 if num%2==0 else num/2 for num in numbers]
[0.5, 4, 1.5, 8, 2.5, 12]
```
```
with_vowels = "This is so much fun!"
''.join(char for char in with_vowels if char not in "aeiou")
"Ths s s mch fn!"
```
Nested List
- nested_list = [[1, 2, 3], [4, 5, 6]]
- nested_list[0][1] = 2
```
nested_list = [[1, 2, 3], [4, 5, 6]]
for i in nested_list:
    for val in i:
        print(val)
        
--Nested List Comprehension
[[print(val) for val in l] for i in nested_list]
1
2
3
...
```
Dictionaries
- Dictionary Comprehension
- Consists of Key Value pair, hash map
- Declare using { } or dict()
```
cat = {'name': 'blue', 'age': '10'}
cat2 = dict(name="blue", age=10)
```
- Access Data in Dictionary using key
```
cat['name'] -> blue
```
- Iterate over Dictionary (difficult cause not ordered)
- .values() .keys() .items() is loopable
```
for v in cat.values() -> prints values
for k in cat.keys() -> prints keys
for k, v in cat.items() -> returns list of tuples both key value
    print(f"key is {k} and value is {v}")
```
- Check if key in dictionary ( in )
- Check if value in dictionary ( in )
```
"name" in cat -> true
"austen" in cat.values() -> false
```
Dictionary Methods
- clear(), removes all values from dictionary
- copy(), makes a clone of a dictionary
- fromkeys(), sets keys to specified value (used to generate default values)
- get(), gets value from key, if DNE returns None
```
{}.fromkeys(['name', 'age'], 'unknown') -> {'name': 'unknown', 'age': 'unknown'}
cat.get('name') -> 'blue'
cat.get('dne') -> None 
```
- pop(key), removes item from list and returns value
- popitems(), randomly removes from dictionary
- update(), takes key/value pairs from list1 and adds/updatese to list2
```
list1.update(list2) -> list2 will overwrite list1 properties
```
Dictionary Comprehension
```
{ __ : __ for __ in __ }

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
# {'first': 1, 'second': 4, 'third': 9}

{num: num**2 for num in [1,2,3,4,5]}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
# {"A": "1", "B": "2", "C": "3"}

Conditional Logic
num_list = [1, 2, 3, 4]
{ num:("even" if num%2==0 else "odd") for num in num_list}
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```

Tuples
- Ordered collection or grouping of items
- ( ), immutable (can never be changed)
```
alphabet = ('a', 'b', 'c')
alphabet[1] = 'b'
```
Why use Tuple?
- Faster than list since it won't change
- It makes code faster
- Use when you have a list of items you know will not change
- Use tuples as keys for dictionary
```
Stores tuple key
location = {
    (35.12, 29.34): "Tokyo",
    (45.23, 75.23): "New York,
    ...
}
location[(35.12, 29.34)] -> Tokyo
```
- dictionary .items() method returns list of tuples (key, value)
- Tuple Looping
```
for letter in alphabet:
    ...
i = len(alphabet) - 1
while i >= 0:
    i-=1
```
- count(val), returns # of times value appears in tuple
- index(val), returns index of value in tuple
- Possible to have nested tuples

Sets
- Formal mathematical sets
- Collection of data which does not have duplicate values
- Elements aren't ordered
- Use with don't care about order, and you don't want duplicates
```
s = set({1, 2, 3, 4, 5, 5, 5}) -> {1, 2, 3, 4, 5}
s[0] -> Error sets don't have indexing
1 in s -> True
```
- Access all elements in Set using For loop
```
for thing in s:
    ...
```
- list(set) -> convert set to list
- Convert List to Set to remove duplicates and reconvert to List
- add(val), adds elements to set (will only add if value unique from set)
- remove(val), removes element in set (throws error if value not in set)
- discard(val), removes element in set (does NOT throw error)
- copy(set), copys set to new set with new address in memory
- clear(), removes all elements from set
- Set Math, intersection, symmetric_difference, union
- | , union returns unique set of elements between 2 sets
- & , returns elements shared between sets
```
math_students = {"Austen", "Caroline", "Ashley"}
bio_students = {"Austen", "Bob", "Joe", "Caroline}
math_students | bio_students ->  {"Austen", "Caroline", "Ashley", "Bob", "Joe"}
math_students & bio_students -> {"Austen", "Caroline", "Ashley"}
```
- Set Comprehension
- { ___ for ___ in ___ }
```
{x**2 for x in range(10)}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
{char.upper() for char in 'hello}
{'O', 'L', 'E', 'L', 'H'}
```
Recap
- Tuples -> ORDERED collections of data which are IMMUTABLE
- Faster than lists and useful for protecting data
- Created with tuple() or ()
- Sets -> UNORDERED & UNIQUE collections of data
- Created with set(), or {}

Functions
```
def name_of_function():
    print('Hi')
name_of_function() -> "Hi"

--Return
def square_of_7():
    return 7**2
result = square_of_7() -> 49

--Parameter
def square_num(num):
    return num**2
def add(a, b):
    return a+b

--Default Parameters
def exponent(num, power=2):
    return num**power
exponent(2, 2) -> 4
exponent(power=3, num=2) -> 8, order of parameters doesn't matter if we pass in param name
```
- Parameters is method definition
- Arguments are values you pass into method Parameters
- Make sure be aware of indentation

Scope
- Function scope, variables created in function only available in that function
- Global scope, if trying to modify global variable with '+=' value in function use 'global' keyword
- Nonlocal scope, use nonlocal keyword if attempting to use variable not scoped in function and not scoped globally
```
--global
total = 0
def increment():
    global total --global keyword
    total += 1
    return total

total = 0
def increment():
    total = 5 -- okay since totally rewriting value
    return total

--nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count+= 1
        return count
    return inner()
```
Documenting Functions
- line after def add,  """ documentation here """
```
def say_hello():
    """A simple function that returns string hello"""
    return "Hello"
    
say_hello().__doc___ -> spits out function documentation
```

Functions II
- Use * and ** parameters to a function and outside of functions
- Leverage dictionary and tuple unpacking to create more flexible functions
- *args, special operator to gather remaining args are tuple
```
def sum_all(*args):
    total = 0
    for v in args:
        total += v
    return total
sum_all(1, 2, 3, 4) -> 10
```
- **kwargs, parmeter for function
- Gathers remaining keyword args as a dictionary
```
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person} likes {color}")
fav_colors(colt="purple", ruby="red", ethel="teal")
"colt likes purple"...
```
Parameter Ordering
1. parameters
2. *args
3. default parameters
4. **kwargs

Tuple Unpacking
- Using * before Tuple/List will pass in those data structures as individual items
- Does what the JS spread ... operator does
```
def sum_all_vals(*args):
    total = 0
    for num in args:
        total += num
    print(total)
sum_all_values(nums) -> breaks since code in fn looking for individiual values not list of values
sum_all_values(*nums) -> destructures list nums and passses in as seperate int
```
Dictionary Unpacking
- Using ** before dictionary to pass key:value pairs to fn
```
def display_names(first, second):
    print(f"{first} says hello to {second})
names = {"first": "Austen", "second", "Caroline"}
display_names(**names)
"Austen says hello to Caroline"
```
Lambda
- No name functions
- Used when passing function into another function
```
def squire(num):
    print num**2
square = lambda num: num*num
```
Map
- function that accepts 2 args (fn, iterable)
- fn is run on every iterable and returns map object (cast map object to list() to see)
```
nums = [2, 4, 8, 10]
doubles = map(lambda x: x*2, nums)
list(doubles) -> [4, 8, 16, 20]
```
Filter
- function that accepts 2 args (fn, iterable)
- filters iterable based on fn
```
n = [1, 2, 3, 4]
evens = list(filter(lambda x: x%2==0, n))
return [2, 4]
```
Built-in Functions
- all(iterable), return Boolean based on if ALL items in iterable are Truthy
- any(iterable), return Boolean based on if ANY items in iterably is Truthy
```
people = ['Austen', 'Ashley', 'Caroline']
all(name[0]=='A' for name in people) -> False, since Caroline does not start with A
any(name[0]=='A' for name in people) -> True, since Austen/Ashley start with A
```
Generator Expressions
- using () vs [] for list comprehension is called generator expression
- Used when only needs to be iterated once to save on memory eg. any() or all()
- sys.getsizeof(data), returns size of data in bytes

Sorted
- sorted(iterable), returns returns copy of sorted iterable as list
- sort on list, tuple, dictionary
```
nums = [2,1,3]
sorted(nums) -> [1,2,3]
prints(nums) -> [2, 1, 3]
sorted(nums, reverse=True)  -> [3, 2, 1]

//sorts dictionary based on username
sorted(users, key=lambda user: user['username'])
```
Min Max
- max(a, b, iterable...), return max value
```
max('c', 'b', 'd') -> 'd'd
max([10,30,45]) -> 45

names = ['Austen', 'Caroline', 'Joe']
min(names, key=lambda n: len(n)) -> 'Joe'
```
Reversed
- reversed(iterator), returns reversed iterator
- use "hello"[::-1] to reverse strings
```
for x in reversed(range(0, 10)) -> loops from 9 -> 0
```
Length
- len(iterable), returns length of iterable

Math Fn's
- abs(num), returns absolute value of num which can be float or int
- sum(iterable, opt. start), returns sum of iterable
- round(ndigits), returns rounded number based on ndigits
```
abs(-2.3) -> 2.5
sum([1, 2, 3, 4],) -> 10
round(3.542) -> 4
round(3.542, 2) -> 3.54
```
Zip
- zip(), returns iterable of tuples where it zips 2 or more iterators together and stops when shortest iterable is exhaused
```
first_zip = zip([1, 2, 3], [4, 5, 6])
zip2 = list(first_zip) -> [(1, 4), (2, 5), (3, 6)]
dict(first_zip) -> {1: 4, 2: 5, 3: 6}

list(zip(*zip2)) -> [(1, 2, 3), (4, 5, 6)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['austen', 'caroline', 'ashley']
{'austen': 98, 'caroline': 91, 'ashley': 78}

final_grades = [pair for pair in zip(midterms, finals)]
# [(80, 98), (91, 89), (78, 53)]

final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
# { 'austen': 98, 'caroline': 91, 'ashley': 78 }

scores = map(
    lambda pair: max(pair),
    zip(midterms, finals)
)
list(scores) -> [98, 91, 78]

zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)
# (('austen', 98), ('caroline': 91), ('ashley': 78))
```
Debugging
- Commons errors an how they occur in Python
- Use pdb, set break points
- Try Except blocks to handle errors

Commons Errors
- SyntaxError, bad syntax
- NameError, variable not defined
- TypeError, wrong datatype
- IndexError, trying to access index in list that doesn't exist
- ValueError, function recieves a arg with right type but bad value eg. int("f")
- KeyError, occurs when trying to access key in dictionary that doesn't exist
- AttributeError, variable doesn't have attribute

Raising Our Own Errors
- Give custom error messages
- raise ValueError('message here'), like Throw in Java
```
raise NameError('this is an error message')

def colorlize(text, color):
    color = ('red', 'blue')
    if type(text) is not str:
        raise TypeError('text must be string')
    if color not in colors:
        raise ValueError('color is invalid')
    ...
```

Try and Except Blocks
- Handle errors and do code
- try/except
```
try:
    foobar
except NameError as err:
    print(err)

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
```
- try/except/else/finally
- else: run when except hasn't run
- finally: runs every time at the end
- divide.py
```
while True:
    try:
        num = int(input('please enter a number'))
    except ValueError:
        print('thats not a number')
    else:
        print('good job you entered an int')
        break
    finally:
        print('runs no matter what')
```
Debugging with pdb
- pdb: Python Debugger
- step through code
- PDB Commands
- l (list)
- n (next line)
- p (print)
- c (continue - finishes debugging)
- normally added import and set_trace() together since import should not always be in code
- if variable is same as pdb command prefix variable name with 'p ' -> 'p l'
```
import pdb; pdb.set_trace()
```

Modules
- Import code from built-in modules
- Import code from other files
- Import code from external modules using pip
- Describe common module patterns
- Module is just a python file

Why use Modules?
- Keep python files small
- Reuse code across multiple files

Built-in modules
- as, rename module to custom name
- from, only import specific methods
```
from random import choice as ch, randint as rint 
ch(...)
rint(...)
```
Custom Modules
- Import own code
- import python file
```
#file1
def fn():
    return "some string"

#file2
import file1
file1.fn() -> "some string"
```
External Modules
- Modules downloaded from the internet
- pypi.org (pip - python package index)
```
python3 -m pip install NAME_OF_PACKAGE
```
ASCII Art Exercise
- pyfiglet
- autopep8, formats code to pep8 standard

The Mysterious __name__ variable
- ___...___, dunder (double under) special properties that shouldn't be touched
- ___name___, if main file executed name is '__main__' else its the file name
- Ignore code in import
```
# use when only want specific code to run if file is main file
if ___name___ == "__main__":
```

Object Oriented Programming (OOP)
- Understand encapsulation and abstraction
- Create clases/instances with methods and properties

Defining Classes/Objects
- Use class/objects to represent real thing
- Class, blueprints for objects contain methods and attributes
- Instance, objects that are constructed from class blueprint

Why OOP?
- Logical human way of thinking to define things
- Encapsulation
    - grouping of public/private attributes and methods into a class making abstraction possible
    - break down code into logical, hierarchical groupings using classes tp make it easier to use
    - _attribute, use _ to define private variable
- Abstraction
    - Expose only relevent data in class interface
    - Hide code away from outside world to make implementation easier
```
# CamelCase when creating class names
class User:
    pass

user1 = User()
```
- __init__() is the constructor method
```
class User:
    def __init__(self, first, age):
        self.name = first
        self.age = age

user1 = User("austen", 25)
```
Underscores Explained
```
_name       convention to say this attribute is supposed to be private variable
__name      name mangling, changes name of attribute (_Person__msg) used with interheritence
__name__    dunder method, don't define or change these. Do not make dunder methods
```
Instance Methods
- need to pass 'self' as parameter
```
class User:
    def __init__(self): ...

    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"
```
Class Attributes
- static variable, only 1 instance of attribute which will be shared on all instances
- can have validations 
```
class Pet:
    allowed = ['cat', 'dog', 'fish']        //static Class attribute
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have that pet")
        self.name = name
        self.species = species
```
Class Methods
- Not very common
- static methods, 1 instance for a all instances
- @classmethod decorator to say its static
- parameter of 'cls' vs 'self'
- can be used to validate data before constructor is called
```
class Person:
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, age)

User.from_string("Tom, Jones, 89")
```
\__repr\__ method
- prints representaion of instance of class
- called when trying to print class
- turns class into readable format and then prints what is in __repr__
```
class Person:
    def __init__(self):

    def __repr__(self):
        print
```
OOP Part 2
- Inheritance
    - Define a class that inherits from another base class
    - Pass parent class as an arg to the definition of a child class
    ```
    class Animal:
        def make_sound(self, sound):
            print(sound)
    class Cat(Animal):              # Cat inherits make_sound() from Animal class
        pass
    ```
- Properties
    - Getter and Setter but in Python
    - Don't need to setup Getter/Setter methods just use annotation and call attribute normally
    - @property decorator
    - @_attr.setter decorator
    ```
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("...")
    
    jane.age    # 0
    jane.age = 20
    jave.age    # 20
    ```
- Super()
    - Way to set attributes of base class when instantiating child class
    - super().__init__(attr, attr2)
    ```
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species

    class Cat(Animal):
        def __init__(self, name, breed, toy):
            super().__init__(name, species = "Cat")
            self.breed = breed
            self.toy = toy
    
    new_cat = Cat("Blue", "Siamese", "Yarn")
    ```
- Multiple Inheritence
    - Not very common but helps understand inheritence overall
    - Explains a bit into how pyhon works underneath
    - If base classes share same name of intance method uses the first passed in base class
    ```
    class Penguin(Ambulatory, Aquatic)      # pass in 2 base classes
        def __init__(self, name):
            # since Ambulatory is first in base class order super() points to it
            Ambulatory.__init__(self, name) or super().__init__(name)
            Aquatic.__init__(self, name)
    ```
- Method Resolution Order (MRO)
    - Whenever class is created Python sets MRO to that class
    - What is the order that python will look for methods on instances of class
    ```
    __mro__ attribute on class
    mro() method
    help(cls) method
    ```
- Polymorphism
    - Object can take on many forms
    - Idea to reuse bits of code in different ways
    - Same class method works in similar ways for different classes
    - Same method (operation) works for different kinds of objects
    - Common implementation is method in base class overriden by subclass
    - Interface kinda, tell classes they need to implement certain attributes / methods
    ```
    class Animal:
        def speak(self):
            raise NotImplementedError("Subclass needs to implement this method")

    class Dog(Animal):
        def speak(self):
            return "woof"'

    class Cat(Animal):
        def speak(self):
            return "meow"
    ```
- Special Magic Methods
    - Idea of polymorphism with add operator ( + )
    - Example of how to use magic dunder methods
    ```
    Special operation methods
    8 + 2 = 10
    "8" + "2" = 82'

    __repr__
    __len__
    __add__ -> +
    __mul__ -> *
    __reversed__
    ...
    from copy import copy
    class Human:
        def __init__(self, first, last, age):
            self.first = first
            self.last = last
            self.age = age

        def __repr__(self):
            return f"Human named {self.first} {self.last}
        
        def __len__(self):
            return self.age
        
        def __add__(self, other):
            if isinstance(other, Human)
                return Human(first='Newborn', last=self.last, age=0)

        def __mul__(self, num):
            if isinstance(num, int)
                return [copy(self) for i in range(num)]
            return TypeError("can't multiply")
    
    j = Human("Jen", "Larsen", 47)
    k = Human("Joe", "Jones', 50)
    print(j + k) -> "Human named Newborn Larsen aged 0"
    ```

Iterators
- Define iterator and interable
- iter() and next() methods
- Build own for loop
Iterator vs Iterable
- Iterator
    - An object which can be interated upon using next() method
    - iter(string) -> returns a string iterator which has next() method
- Iterable
    - An object that returns an iterator when iter() is called on it
```
"HELLO" is an iterable
iter("HELLO"), returns an iterator
nums = [1,2,3,4]
it = iter(nums)
it.next()
```
Custom For Loop
- would never do normally but understand interable and iterators better
```
def my_for(iterable, fn):
    iterator = iter(iterable)
    while True:
        try:
            thing = print(next(iterator))
        except:
            print('end of iterator')
            break
        else:
            fn(thing)
my_for('lol', print) -> prints 'l', 'o', 'l'
```
Custom Iterator
- use iter and next dunder method
```
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration
```
Generators
- Generators are iterators, subset of iterator
- Quick easy short way of creating iterators
- Use Generator functions with yield keyword
- Generators can be created with generator expressions
- Just use 'yield' keyword to return generator and leverage next(...)
```
Functions                               Generator Functions
uses 'return'                           uses 'yield'
return once                             can yield multiple times
when invoked returns the return value   when invoke returns a generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count     - stops logic and returns until next() is called
        count += 1

# returns generator object with next() method
counter = count_up_to(5)    
# moves to code after yield until yield or StopIteration encountered
next(counter) -> 1
next(counter) -> 2
next(counter) -> 3 ...
```
- Memory usage
    - Using a generator is easier on memory instead of storing things in list to spit out
```
def fib_list(max):
    nums = []
    a,b = 0,1
    while lens(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x,y = y, x+y
        yield x
        count+=1
```
Generator Expressions
- like List Comprehensions but for generators
- use (), instead of []
```
def nums():
    for num in range(10):

g = (num for num in range(1,10))

#Sum with Generator Expressions
# Adds each iteration yield result to sum to its quicker and better memory consumption
print(sum(n for n in range(100000)))
#Sum with List Comprehension
# this is longer it creates entire list and then sums the list together
print(sum([n for n in range(100000)]))
```
Higher Order Functions (HOF)
- Idea of being able to pass functions as arguments to other functions
- Nesting functions inside of other functions
- Functions are first class citizens and can be used as such
- Closure/scoping args passed to base function are accessible in nested function
```
# pass function to another function as arg
def sum(n, fn):
    total = 0
    for num in range(n):
        total += fn(num)
    return total
def square(n):
    return n*n

print(sum(3, square)) -> 15

#create function in another function (nested functions)
def greet(person):
    def get_mood():
        return 'happy'
    return get_mood() + person
```
Decorators
- simply functions that wrap other functions to enhance behavior
- uses '@' to wrap another function
- wrapper() functoin in decorator is what is executed
- *args, **kwargs will be the args passed to function which is wrapped by @decorator
Decorator Syntax
```
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*arms, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

print(greet("todd")) # "Hi, I'm TODD."
```
Preserving Metadata
- unable preserve metadata when using decorators
- metadata -> dunder docstring, name
- use 'from functools import wraps' import @wraps
```
def log_fn_data(fn):
    @wraps(fn)              <--- use to keep meta data
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@log_fn_data
def add(x, y):
    ...
print(add.__doc__) -> without @wraps displays document for wrapper in log_fn_data func
```
- speed_test.py, shows how to use @decorator to wrap code needed to test performance
- interesting real world implementation
- ensure.py, shows validation with decorators
- ensure_first_arg.py, shows how to write decorator with argument
    - need to add another nested inner() to take fn and base func definition will take decorator args. Review python file to get more information
- Enforce arguemnt Data Types with a Decorator @enforce (custom decorator)
- enforce.py, this is code snippet found online# The-Modern-Python-3
