# 🧮 NumPy Reference Note: Foundational Concepts

## 1\. 🌟 Core Concepts and Structure

### What is NumPy?

  * **NumPy** (Numerical Python) is the foundational library for scientific computing in Python.
  * **Purpose:** Provides fast, memory-efficient data structures and operations for numerical data.

### The `ndarray` Object

  * **Definition:** A **homogeneous**, N-dimensional array. All elements must be of the same data type (`dtype`).
  * **Key Attributes:**

| Attribute | Definition | Example (2D Array) |
| :--- | :--- | :--- |
| **`ndim`** | **Rank** (number of axes/dimensions). | `2` |
| **`shape`**| Tuple of dimensions (size along each axis). | `(Rows, Columns)` e.g., `(3, 4)` |
| **`size`** | Total number of elements (product of `shape`). | `12` |
| **`dtype`**| Data type of elements (e.g., `int64`, `float64`). | `float64` |

### Understanding Axes

The **Axis** (or dimension) is the direction along which an operation occurs.

| Dimensions | Shape Example | Axes Count | Axis 0 (Primary) | Axis 1 (Secondary) |
| :--- | :--- | :--- | :--- | :--- |
| **1D** | `(5,)` | 1 | The single line of values | N/A |
| **2D** | `(3, 4)` | 2 | **Rows** (Vertical) | **Columns** (Horizontal) |
| **3D** | `(2, 3, 4)` | 3 | Depth | Rows | Columns |

-----

## 2\. 📦 Array Creation and Initialization

### Basic Creation and Properties

```python
import numpy as np
a = np.array([1, 2, 3])
# type(a) -> <class 'numpy.ndarray'>
```

**🚨 Edge Note:** If input array has **mixed types** (e.g., `[1, 2.5]`), NumPy performs **auto-upcasting** (e.g., to `float64`) to maintain homogeneity.

### Functions for Initialization

| Function | Syntax & Description | Example Output |
| :--- | :--- | :--- |
| **`np.zeros()`**| Creates an array filled with **`0.0`**. | `np.zeros((2, 3))` $\to$ `[[0. 0. 0.], [0. 0. 0.]]` |
| **`np.full()`** | Creates an array filled with a **constant** value. | `np.full((2, 2), 7)` $\to$ `[[7 7], [7 7]]` |
| **`np.loadtxt()`**| Loads an array from a text file (e.g., CSV, delimited text).| `np.loadtxt('data.txt', delimiter=',')` |

### Detailed Range Functions

| Function | Primary Use Case | Syntax | Edge Notes |
| :--- | :--- | :--- | :--- |
| **`np.arange()`** | Generate values by a **`step` size** over an interval. | `np.arange(start, stop, step)` | The **`stop`** value is **exclusive**. May suffer from floating-point errors with non-integer steps. |
| **`np.linspace()`**| Generate a **fixed number** of evenly spaced values. | `np.linspace(start, stop, num)` | The **`stop`** value is **inclusive** by default (`endpoint=True`). Preferred for precise array size. |

#### `arange` Example

```python
np.arange(0, 10, 2)    # start=0, stop=10 (exclusive), step=2
# Output: [0 2 4 6 8] 
```

#### `linspace` Example

```python
np.linspace(0, 1, 5)   # 5 points between 0 and 1 (inclusive)
# Output: [0.  0.25 0.5 0.75 1. ] 
```

-----

## 3\. ✂️ Indexing, Slicing, and Filtering

### Standard Indexing and Slicing

  * **Slicing:** `a[start:stop:step]`
      * Example: `a[2::2]` $\to$ Starts at index 2, takes every 2nd element.
  * **Indexing:** `a[row_index, col_index]` for 2D arrays.
  * **🚨 Edge Note:** Using an index that is too large raises an **`IndexError`**.

### Boolean (Mask) Filtering

Selects elements based on a logical condition (where the condition evaluates to `True`).

```python
a = np.array([1, 4, 3, 6])
odd_values = a[a % 2 != 0] # Filter for odd numbers
# odd_values Output: [1 3]
```

**🚨 Edge Note:** The **Boolean Mask array** (the result of `a % 2 != 0`) **must match the shape** of the array being filtered.

### Conditional Index Retrieval

  * **`np.where(condition)`:** Returns the **indices** where the condition is true.
      * Example: `np.where(a > 3)` $\to$ returns a tuple of index arrays (one array per dimension).

-----

## 4\. 🔄 Reshaping and Dimension Control

### `a.reshape(new_shape)`

Returns a new view of the array data with the specified dimensions.

  * **Syntax:** `a.reshape((dim1, dim2, ...))`
  * **Automatic Dimension:** Use **`-1`** as a placeholder for one dimension, and NumPy will calculate the size based on the array's total size.

#### Example: Automatic Dimension

```python
data = np.arange(12)  # Size 12
matrix = data.reshape((-1, 4)) # 4 columns, NumPy calculates 3 rows
# matrix.shape: (3, 4)
```

**🚨 Edge Note (Size Mismatch):** Reshape fails with a **`ValueError`** if the product of the new dimensions does not equal the original array's `size`.

### `a.flatten()`

Returns a **copy** of the array collapsed into one dimension.

  * **Usage:** `a.flatten()`
  * **Result:** Always returns a 1D array.

-----

## 5\. ➕ Arithmetic and Matrix Operations

### Element-wise Operations (Vectorization)

All standard operators (`+`, `-`, `*`, `/`) are applied **element-wise**.

```python
a + 5     # Add 5 to every element
a * 2     # Multiply every element by 2
```

### Broadcasting

The set of rules NumPy uses to perform arithmetic on arrays of different shapes.
**🚨 Edge Note (Shape Mismatch):** Operations fail with a **`ValueError`** if arrays are not **broadcastable**.

### Matrix Multiplication

  * **Syntax (Preferred):** `a @ b` (Python 3.5+)
  * **Syntax (Legacy):** `np.dot(a, b)`
    **🚨 Edge Note:** For multiplication, the **inner dimensions must match** (columns of the first array must equal rows of the second).

### Transpose

  * **Syntax:** `a.T`
  * **Purpose:** Reverses the axes (e.g., changes a (2, 3) matrix to a (3, 2) matrix).
    **🚨 Edge Note:** Transpose has **no effect** on a **1D array**.

### 📐 Trigonometric Ops

  * **Input Requirement:** Input values must be in **radians**.
  * **Conversion:** Use `np.radians()` to convert degrees to radians.
      * Example: `r = np.radians([90, 180])`
      * Use: `np.sin(r)`, `np.cos(r)`, `np.tan(r)`
        **🚨 Edge Note:** `tan(90°)` will result in **`inf`** (infinity) due to the vertical asymptote.

-----

## 6\. 📊 Aggregation and Combining

### Aggregation Functions

These functions reduce an array (or slice) to a single value or a smaller array.

| Function | Description | Axis Control Note |
| :--- | :--- | :--- |
| **`np.sum(a)`** | Calculates the total sum of all elements. | |
| **`np.min(a)`, `np.max(a)`** | Finds the minimum/maximum element. | |
| **`np.sum(a, axis=0)`** | Sums elements **along** the specified axis (collapsing that dimension). | `axis=0` sums down the rows (results in a row vector of column sums). |
| **`np.cumsum(a)`** | Returns the **cumulative sum**. | Returns an array of the **same shape** as the input. |

**🚨 Edge Note (Axis):** Using an axis number larger than `ndim-1` raises an **`AxisError`**.

### Combining and Splitting

| Operation | Function | Description | Edge Notes |
| :--- | :--- | :--- | :--- |
| **Sorting** | `np.sort(a, axis=0)` | Returns a **sorted copy** along the axis. | |
| **Combining** | `np.concatenate((a, b), axis=0)` | Joins arrays along a specified axis. | Array shapes must match **except** along the concatenation axis. |
| **Splitting** | `np.split(a, 3)` | Divides the array into $N$ parts. | The array's total size along the split axis **must be divisible** by the split count. |
