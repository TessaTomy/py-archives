# 📦 Variables and Object References in Python

### 1. Variables as Names
- In Python, a variable is **not a memory box** but a **name bound to an object**.  
- Assignment (`=`) creates or rebinds a name to an object.  
- Example:  
  ```python
  x = 10   # 'x' is a name bound to the integer object 10
  ```

---

### 2. Objects
- Every value in Python is an **object**.  
- Each object has:
  - **Identity** → its unique address in memory (`id()` function).  
  - **Type** → the class it belongs to (`type()` function).  
  - **Value** → the actual data stored.  

---

### 3. Assignment Semantics
- `x = 10` → binds the name `x` to the integer object `10`.  
- Reassignment (`x = 20`) → binds `x` to a new object `20`.  
- Old objects are automatically cleaned up by **garbage collection** if no names refer to them.

---

### 4. Mutability
- **Immutable objects**: integers, strings, tuples. Once created, their value cannot change. Reassignment creates a new object.  
- **Mutable objects**: lists, dictionaries, sets. Multiple names can point to the same object, and changes affect all references.  
  ```python
  a = [1, 2]
  b = a
  b.append(3)
  print(a)  # [1, 2, 3] → both names point to the same list
  ```

---
# ✨ Operators in Python

**Definition**:  
Operators in Python are special symbols or keywords that perform operations on operands. They provide a concise way to express computations, comparisons, and logical reasoning. Internally, operators map to special methods (e.g., `+` calls `__add__()`).

---

### Categories of Operators

1. **Arithmetic Operators**  
   - Perform mathematical operations.  
   - Examples: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation). 
   ```python
   7 + 2   # 9
   7 // 2  # 3
   ```

2. **Relational (Comparison) Operators**  
   - Compare values, return Boolean results.  
   - Examples: `==`, `!=`, `>`, `<`, `>=`, `<=`.  
   ```python
   5 > 3   # True
   ```

3. **Logical Operators**  
   - Combine Boolean expressions.  
   - Examples: `and`, `or`, `not`.  
   ```python
   True and False  # False
   ```

4. **Assignment Operators**  
   - Assign values, with optional operation.  
   - Examples: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.  
   ```python
   x = 5
   x += 2   # 7
   ```

5. **Bitwise Operators**  
   - Operate at binary level.  
   - Examples: `&`, `|`, `^`, `~`, `<<`, `>>`.  
   ```python
   5 & 3   # 1
   ```

6. **Identity Operators**  
   - Compare object identity (memory reference).  
   - Examples: `is`, `is not`.  
   ```python
   a = [1,2]; b = a
   a is b   # True
   ```

7. **Membership Operators**  
   - Test membership in sequences.  
   - Examples: `in`, `not in`.  
   ```python
   "a" in "cat"   # True
   ```
   
### 🔑 Chained Comparisons in Python
- Python supports **chained comparisons** (e.g., `a < b < c`, `0 <= x <= y`).  
- Expression `0 <= x <= y` is evaluated as:  
  ```python
  (0 <= x) and (x <= y)
  ```  
- **Core Idea**: It checks multiple relational conditions in a single, readable statement.  
- **Advantages**: Improves clarity, avoids repetition (`0 <= x and x <= y`).  
- **Extension**: Works with numbers, strings, dates, and can chain more than two comparisons (`1 < x < 10 < y`).  
---

# 📃 The `input()` Function in Python
- **Definition**: `input()` is a built‑in function used to read user input from the keyboard. It always returns the input as a string.  
- **Syntax**: `variable = input("Prompt message: ")` → displays the prompt, waits for user input, and stores the result.  
- **Type Conversion**: Since `input()` returns a string, numeric input must be converted explicitly:  
  ```python
  age = int(input("Enter your age: "))
  pi  = float(input("Enter a value for pi: "))
  ```
----
# ✨ Data Types in Python

**Definition**:  
Data types in Python define the nature of values that objects can hold and the operations that can be performed on them. Python is dynamically typed, meaning the type of a variable is determined at runtime when a value is assigned. Every value in Python is an object with identity, type, and value. This object‑oriented model makes Python flexible, powerful, and consistent across all types.

---

### 1. Numeric Types  
Python provides three distinct numeric types:  
- **int**: Represents whole numbers of arbitrary size. For example, `x = 42`. Integers can be positive, negative, or zero, and Python automatically manages their size without overflow issues. They support arithmetic operations (`+`, `-`, `*`, `/`), bitwise operations (`&`, `|`, `^`), and comparisons (`==`, `<`, `>`).  
- **float**: Represents real numbers with decimal points. For example, `pi = 3.14159`. Floats support scientific notation (`1.2e3` equals 1200.0) and are widely used in mathematical and scientific applications. They can suffer from precision issues due to binary representation, which is important to note in numerical analysis.  
- **complex**: Represents numbers with real and imaginary parts. For example, `z = 2 + 3j`. Complex numbers support arithmetic operations and are useful in engineering, physics, and advanced mathematics. Python provides built‑in functions like `z.real` and `z.imag` to access components.

---

### 2. Sequence Types  
Sequences are ordered collections that allow indexing and iteration.  
- **str**: Immutable sequence of Unicode characters. For example, `s = "Python"`. Strings support slicing (`s[0:3] → "Pyt"`), concatenation (`"Py" + "thon"`), repetition (`"Hi" * 3 → "HiHiHi"`), and numerous methods like `.upper()`, `.lower()`, `.replace()`.  
- **list**: Ordered, mutable collection. For example, `nums = [1, 2, 3]`. Lists can hold heterogeneous elements, be nested (`matrix = [[1,2],[3,4]]`), and resized dynamically. They support methods like `.append()`, `.remove()`, and slicing.  
- **tuple**: Ordered, immutable collection. For example, `t = (1, "a", 3.5)`. Tuples are often used for fixed data structures, function returns, and as dictionary keys since they are hashable.  
- **range**: Represents an arithmetic progression of integers. For example, `range(1, 10, 2)` produces 1, 3, 5, 7, 9. Ranges are memory‑efficient because they generate values lazily.

---

### 3. Mapping Type  
- **dict**: A dictionary is a collection of key‑value pairs. For example, `student = {"name": "Tessa", "age": 22}`. Keys must be immutable types (like strings, numbers, or tuples), while values can be of any type. Dictionaries support fast lookups, updates, and methods like `.keys()`, `.values()`, and `.items()`. They are widely used for structured data, configuration, and JSON‑like storage.

---

### 4. Set Types  
Sets are collections of unique elements.  
- **set**: An unordered, mutable collection. For example, `s = {1, 2, 3}`. Sets automatically remove duplicates and support mathematical operations like union (`s1 | s2`), intersection (`s1 & s2`), and difference (`s1 - s2`).  
- **frozenset**: An immutable version of a set. For example, `fs = frozenset([1, 2, 3])`. Frozensets are hashable and can be used as dictionary keys or stored inside other sets.

---

### 5. Boolean Type  
- **bool**: Represents logical values `True` and `False`. For example, `flag = (5 > 3)` evaluates to `True`. Booleans are internally subclasses of integers, where `True == 1` and `False == 0`. This allows them to participate in arithmetic (`True + True → 2`), though they are primarily used in conditional logic.

---

### 6. Binary Types  
Python provides types for handling raw binary data.  
- **bytes**: Immutable sequence of bytes. For example, `b = b"hello"`. Useful for representing binary data like files or network streams.  
- **bytearray**: Mutable sequence of bytes. For example, `ba = bytearray([65, 66, 67])`. Supports in‑place modification, making it suitable for low‑level operations.  
- **memoryview**: Provides a view of another object’s buffer without copying. For example, `mv = memoryview(b"data")`. This is efficient for large data handling, as it avoids duplication.

---
