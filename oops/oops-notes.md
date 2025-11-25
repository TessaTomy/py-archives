# 📋 _OOP's Log_

**Notes from the edge of object logic—what broke, what got rewritten, and what’s still unclear. Saved for future remixers, and for the version of me that needs a reminder.**

---

## 💥 Object Theory: State, Behavior, Identity

Every object in Python is fundamentally characterized by three things:

* **State (Attributes):** The data or properties of the object. These are the **variables** defined within the object (`self.x`, `self.__y`). *Example: A car's state includes its color, speed, and fuel level.*
* **Behavior (Methods):** The actions the object can perform. These are the **functions** defined within the class. *Example: A car's behavior includes starting, stopping, and accelerating.*
* **Identity:** A unique marker (like an address in memory) that distinguishes one object from another.

---

## 1. 🏗️ Classes and Objects Fundamentals

* **Class:**
    > A **blueprint** or **template** for creating objects. It defines a set of **attributes** (data) and **methods** (functions).
    * *Syntax Example:* `class A:`
* **Object (Instance):**
    > A specific entity created from the class blueprint. It is a **concrete instantiation** of the class.
    * *Instantiation Example:* `obj1 = A(1, 2, 3)` creates an object named `obj1` from the class `A`.

---

## 2. 🧱 The `__init__` Constructor

The `__init__` method is the **constructor** in Python.

* **Primary Purpose:** It's automatically called right after object creation to **initialize** the object's attributes (set their initial values).
* **Core Syntax:**
    ```python
    def __init__(self, arg1, arg2, ...):
        # Initialization logic
        self.attribute = arg1
    ```
* **The `self` Keyword:**
    > The first parameter in any class method. It is a reference to the **instance** of the class being operated on.
* **Default Arguments:** Highly useful for allowing object creation without requiring every parameter to be explicitly passed.

---

## 3. 🛡️ Encapsulation & Access Control

**Encapsulation** is the practice of bundling data (attributes) and the methods that operate on that data, often restricting direct access. Python uses naming conventions to define access levels:

| Access Type | Naming Convention | Accessibility | Notes (The Python Way) |
| :--- | :--- | :--- | :--- |
| **Public** | `attribute_name` (`x`) | Accessible **from anywhere**. | **Default** in Python. No special prefix needed. |
| **Protected** | `_attribute_name` (`_z`) | Accessible within the class and its **subclasses**. | **Convention only.** A hint to external users not to touch it. |
| **Private** | `__attribute_name` (`__y`) | Accessible *only* within the class. | Achieved via **Name Mangling** to prevent accidental external access. |

### Accessor Methods (The Public Interface)

Accessor methods are public methods that control access to private or protected attributes.

* **Getter:** A method used to **read/retrieve** the value of an attribute (e.g., `get_y()`).
* **Setter:** A method used to **modify/set** the value of an attribute. This is where you add **validation logic**.

---

## 4. 🔗 Inheritance (Code Reusability)

Inheritance allows a new class (**subclass** or **child**) to inherit attributes and methods from an existing class (**superclass** or **parent**).

* **Concept:** Establishes an **`is-a` relationship**.
* **`super()` Function:** Used inside the subclass to call methods (especially `__init__`) from its direct parent class.

### 💡 Inheritance Example

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def display_brand(self):
        return f"This is a {self.brand} vehicle."

class Car(Vehicle): # Car inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand) # Calls the parent's constructor
        self.model = model
```

---

## 5. 🔄 Polymorphism & Method Variations

**Polymorphism** means "many forms." 

### 🐍 Python-Specific Note on Polymorphism

> In Python, we primarily utilize **Method Overriding** (changing a parent's method behavior in a child class) and **Operator Overloading** (defining how built-in operators like `+` work with custom objects). **True Method Overloading** (having multiple methods with the same name but different argument counts/types) is **not natively supported** like it is in Java or C++.

* **Method Overriding:** A subclass provides its own specific implementation of a method that is already defined in its superclass.
* **Operator Overloading:** Implementing special **Dunder Methods** (e.g., `__add__` for `+`) to make custom objects work with standard operators.
  
---

## 6. 💡 `@property` Decorators (Pythonic Accessors)

The `@property` decorator provides a clean, Pythonic way to define **getters**, **setters**, and **deleters** for attributes. It allows you to use methods to manage attribute access while treating the attributes as simple variables from the outside.

This achieves **encapsulation** (validation, computation, etc.) without sacrificing the simplicity of dot-notation access.

### 🐍 Practical `@property` Example

```python
class Person:
    def __init__(self, initial_age):
        self._age = initial_age 

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value):
        self._age = new_value

    @age.deleter
    def age(self):
        del self._age

# --- Usage Demonstration ---

person = Person(30)

person.age = 45
print(person.age)

del person.age #remove attribute for the object
```
## 7. 🔮 Built-in Attribute Management Functions

| Function | Purpose | Equivalent Operator/Syntax | Example Usage |
| :--- | :--- | :--- | :--- |
| `getattr(obj, name, [default])` | Retrieves the value of the named attribute from `obj`. | `obj.name` | `value = getattr(obj, "color", "blue")` |
| `setattr(obj, name, value)` | Assigns `value` to the named attribute of `obj`. | `obj.name = value` | `setattr(obj, "speed", 50)` |
| `hasattr(obj, name)` | Checks if `obj` has a named attribute. Returns `True` or `False`. | (No direct operator) | `if hasattr(obj, "model"):` |
| `delattr(obj, name)` | Deletes the named attribute from `obj`. | `del obj.name` | `delattr(obj, "temp_data")` |

-----

## 8\. 🪄 Dunder Methods: Object Representation (`__repr__` & `__str__`)

The Dunder Methods allow custom objects to integrate with Python's built-in functions (`print`, `str`, `repr`) and operators (`+`, `-`, etc.).

### A. `__repr__` (The Official/Debugging Representation)

  * **Need:** Primarily for **debugging** and **logging**. Goal is to be **unambiguous**.
  * **Called By:** The built-in `repr()` function.
  * **Shell Behavior:** It is automatically called when an object's variable name is typed in the **interactive shell (REPL)**.
  * **Convention:** Should ideally be a constructor-like string (e.g., `Point(x=3, y=5)`).

### B. `__str__` (The Readable/End-User Representation)

  * **Need:** For **displaying** the object to the end-user. Goal is to be **readable**.
  * **Called By:** The built-in `print()` and `str()` functions.
  * **Fallback:** If `__str__` is not defined, `print()` uses `__repr__`.

### C. 💡 Example and Explicit Call

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})" 
    def __str__(self):
        return f"({self.x}, {self.y})"
        
p = Point(3, 5)

print(p)          # Calls __str__ -> Output: (3, 5)
print(repr(p))    # Explicitly calls __repr__ -> Output: Point(x=3, y=5)
# In the REPL, just typing 'p' calls __repr__.
```

-----

## 9\. ➕ Operator Overloading & The Destructor

### A. Common Operator Overloading Dunder Methods

By implementing these methods, you define how your custom objects behave with standard Python operators.

| Operator | Dunder Method | Purpose |
| :--- | :--- | :--- |
| `+` | `__add__(self, other)` | Addition |
| `*` | `__mul__(self, other)` | Multiplication |
| `**` | `__pow__(self, other)` | Exponentiation (Power) |
| `==` | `__eq__(self, other)` | Equality Test |
| `!=` | `__ne__(self, other)` | Inequality Test |
| `<` | `__lt__(self, other)` | Less Than |
| `<=` | `__le__(self, other)` | Less Than or Equal To |
| `>` | `__gt__(self, other)` | Greater Than |
| `>=` | `__ge__(self, other)` | Greater Than or Equal To |
| `-` | `__neg__(self)` | Unary Negation (e.g., `-p1`) |
| `~` | `__invert__(self)` | Bitwise Inversion (Unary `~`) |
| `^` | `__xor__(self, other)` | Bitwise XOR |

### B. The Destructor: `__del__`

The `__del__` method is the **destructor** in Python.

  * **Purpose:** It defines cleanup actions to be executed when an object is about to be **destroyed** (i.e., when its reference count drops to zero and it is being garbage collected).
  * **Usage:** It's rarely used, as Python's **Garbage Collector** typically handles memory management automatically. It is useful for releasing **external resources** like file handles, network connections, or database cursors.
  * **Key Difference from `__init__`:** While `__init__` is guaranteed to run right after creation, `__del__` is **not guaranteed** to run at a predictable time, or even at all (e.g., if the program crashes or the object creates a circular reference).
  * **When it's called:** When the last reference to the object is deleted (`del obj`) or when the object is otherwise garbage collected.

<!-- end list -->

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"Resource '{self.name}' created (e.g., File Opened).")

    def __del__(self):
        print(f"Resource '{self.name}' destroyed (e.g., File Closed).")

# --- Usage ---
r1 = Resource("LogFile") 
# ... do work with r1 ...

# When the last reference is removed, __del__ is called.
del r1
# Output: Resource 'LogFile' destroyed (e.g., File Closed).
```
-----

## 12\. 🔗 Inheritance (Code Reusability)

Inheritance is a mechanism where a new class (**subclass** or **child**) derives attributes and methods from an existing class (**superclass** or **parent**), establishing an **`is-a` relationship**.

### A. The `super()` Function

The `super()` function is used inside the subclass to call the next method in the **Method Resolution Order (MRO)**, which often means calling the method from the parent class. This enables **cooperative inheritance**.

  * **Syntax:** `super().__init__(arg1, arg2, ...)`

-----

### B. Types of Inheritance

#### 1\. Single Inheritance

A child class inherits from only one parent class.

| Class | Role |
| :--- | :--- |
| `Vehicle` | Parent |
| `Car` | Child (inherits from `Vehicle`) |

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
class Car(Vehicle): # Single Inheritance
    def __init__(self, brand, model):
        super().__init__(brand) # Call Vehicle's __init__
        self.model = model
```

-----

#### 2\. Multilevel Inheritance (Calling Second-Level Parent Function)

A child class inherits from a parent, which in turn inherits from another grandparent class.

| Class | Relationship |
| :--- | :--- |
| `Vehicle` | Grandparent |
| `Car` | Parent (inherits from `Vehicle`) |
| `Sedan` | Child (inherits from `Car`) |

```python
class Sedan(Car): # Sedan inherits methods/attributes from both Car and Vehicle
    def __init__(self, brand, model, color):
        super().__init__(brand, model) # Calls Car's __init__, which calls Vehicle's __init__
        self.color = color
        
    def start_engine(self):
        return "Engine started."

    def sedan_info(self):
        # Calling a function (start_engine) within another function
        engine_status = self.start_engine()
        return f"This {self.color} {self.brand} {self.model} is a Sedan. Status: {engine_status}"
```

-----

#### 3\. Multiple Inheritance (Using `super()` and Class Name Access)

A single child class inherits from **two or more** parent classes.

| Class | Role |
| :--- | :--- |
| `Swimmer` | Parent 1 |
| `Walker` | Parent 2 |
| `Amphibian` | Child (inherits from `Swimmer` AND `Walker`) |

```python
class Swimmer:
    def __init__(self, gills):
        print("Initializing Swimmer.")
        self.gills = gills
    def swim(self):
        print("Can swim.")
    
class Walker:
    def __init__(self, legs):
        print("Initializing Walker.")
        self.legs = legs 
    def walk(self):
        print("Can walk.")
        

class Amphibian(Swimmer, Walker): # MRO: Amphibian -> Swimmer -> Walker -> object
    def __init__(self, gills, legs):
        
        # 1. Initialize Parent 1 (Swimmer) using super()
        # This is the recommended Pythonic way for the FIRST class in the MRO.
        super().__init__(gills) 
        
        # 2. Initialize Parent 2 (Walker) using explicit Class Name call
        # You MUST pass 'self' explicitly when calling a class method directly.
        Walker.__init__(self, legs) 

    def move(self):
        # Accessing elements: Use 'self' to access attributes/methods from any parent.
        print(f"Moving: {self.gills} gills, {self.legs} legs.")
        self.walk() # Calls Walker.walk() via self and MRO
        self.swim() # Calls Swimmer.swim() via self and MRO

# --- Usage ---
frog = Amphibian(gills=2, legs=4)
# Note: The prints from the __init__ methods show Swimmer initializes first, then Walker.
frog.move() 
```

-----

## 13\. 🔄 Method Overriding

**Method Overriding** is a core concept of polymorphism and inheritance. It occurs when a **subclass provides its own specific implementation** of a method that is already defined in its superclass.

  * **Purpose:** To change or specialize the behavior inherited from the parent class without modifying the parent class itself.
  * **Mechanism:** When the method is called on the child object, Python executes the child's version of the method instead of the parent's.
  * **Accessing Parent:** You can still call the original parent method from inside the overridden child method using `super()`.

### 💡 Method Overriding Example

```python
class Animal:
    def make_sound(self):
        return "Generic Animal Sound"

class Dog(Animal): # Dog overrides make_sound
    def make_sound(self):
        # Use super() to call the original parent method before or after specialization
        generic_sound = super().make_sound()
        return f"Bark! (Override of: {generic_sound})"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# --- Usage Demonstration ---

a = Animal()
d = Dog()
c = Cat()

print(a.make_sound()) # Output: Generic Animal Sound
print(d.make_sound()) # Output: Bark! (Override of: Generic Animal Sound)
print(c.make_sound()) # Output: Meow!
```
