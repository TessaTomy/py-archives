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
