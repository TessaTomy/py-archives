# 🛡️ Exception Handling Notes

*Understanding exception handling isn't about avoiding crashes; it's about writing code that **degrades gracefully** when faced with **runtime anomalies**. This is non-negotiable for production-grade systems.*

-----

## 1\. 🛑 Exception Mechanics and Degradation

An **Exception** is a runtime event that interrupts the normal, sequential instruction flow. Our goal is to handle this interruption to ensure the program doesn't halt abruptly but continues operating or shuts down cleanly. This process is called **graceful degradation**.

  * **Runtime Anomaly:** Any event (like division by zero, network loss, or invalid data access) that occurs during execution and raises an `Exception` object.

-----

## 2\. 🧩 The Exception Handling Structure

The standard structure for handling exceptions is the `try...except...else...finally` sequence, which defines the complete execution path for success, error, and cleanup.

| Block | Execution Condition | Technical Role | Syntax |
| :--- | :--- | :--- | :--- |
| **`try`** | Always executes first. | Contains the code **under surveillance** for runtime anomalies. | `try:` |
| **`except ExceptionType:`** | Executes **only if** a specified anomaly is raised in `try`. | **Handler:** Defines the resolution logic (e.g., fallback value, logging). | `except ValueError as e:` |
| **`else`** | Executes **only if** `try` completes **without an anomaly**. | Contains code strictly **dependent on the success** of the primary operation. | `else:` |
| **`finally`** | Executes **always**, regardless of success, anomaly, return, or jump. | **Finalizer:** Contains **mandatory cleanup** operations (e.g., closing file descriptors). | `finally:` |

### 💡 Core Syntax Example (Best Practice)

```python
def process_data(data):
    # Attempt high-risk I/O operation
    try:
        data_int = int(data) 
        result = 100 / data_int
    except ValueError:
        print("Anomaly: Data type mismatch (non-numeric input).")
        return None
    except ZeroDivisionError:
        print("Anomaly: Attempted division by zero.")
        return None
    else:
        # Runs ONLY if BOTH int() and division succeeded
        print("Success: Processing complete.")
        return result
    finally:
        # Guaranteed execution path—essential for resource cleanup.
        print("--- Resource check completed ---") 
```

-----

## 3\. 🐍 Exception Resolution and Call Stack Unwinding

This section addresses how an anomaly is resolved, emphasizing the **runtime jump** (non-local exit) from a function.

### A. Local Resolution

1.  **Immediate Search:** When an exception is raised, the interpreter immediately checks the surrounding **`except`** blocks for a type match.
2.  **Match $\rightarrow$ Resolution:** If a handler is found, the exception is considered **resolved**. Execution continues after the `try...finally` structure.
3.  **No Match $\rightarrow$ Jump:** If no handler matches locally, the exception is propagated, and the interpreter **jumps out** of the current function.

### B. Call Stack Unwinding

The exception proceeds up the **call stack** to the calling function, a process known as **unwinding**.

1.  **Propagation:** The interpreter checks the `except` blocks in the calling function's scope.
2.  **Resolution:** This continues until a matching handler is found *or* the interpreter reaches the top level of the program.
3.  **Termination:** If unresolved at the top level, the program terminates, and the **traceback** is printed to standard error.

### C. The Role of `finally` During Jumps

  * **Mandatory Execution:** If the exception causes a jump out of the function (up the call stack), the **`finally`** block of the exiting function **always executes immediately before the jump occurs**. This ensures resource closure *even when control leaves the function abruptly*.

-----

## 4\. 🔥 Raising, Customization, and Catching Syntax

### A. Explicit Raising and Re-raising

The **`raise`** keyword is used to manually trigger an exception, crucial for validating data constraints.

  * **Syntax (Raise Instance):** `raise ValueError("Invalid parameter value.")`
  * **Syntax (Re-raise):** `except CustomError: # ... logging ... raise` (Used inside an `except` block to pass the original anomaly up the stack after local cleanup).

### B. General Catch Syntax

While specific handling is paramount, sometimes a broader catch is necessary (always place last):

  * **Discouraged (Too Broad):** `except:` (Catches all exceptions, including control-flow interrupts like `SystemExit`).
  * **Recommended Catch-All:** **`except Exception as e:`** (Catches nearly all conventional runtime errors, leaving critical system interruptions unhandled).

### C. Custom Exceptions (Inheritance)

For enterprise-level clarity, use **custom exceptions** by inheriting from the base **`Exception`** class.

  * **Benefit:** Allows users of your API to catch your domain-specific errors precisely.

| Syntax (Class Definition) | Usage Example |
| :--- | :--- |
| `class CustomError(Exception): pass` | `try: # ... risky operation ... except CustomError: # ... retry logic ...` |

### D. Usage Example

```python
class LowValueInputError(Exception):
    """Custom exception when input fails a minimum threshold check."""
    pass

def check_value(x):
    # Function enforcing a simple rule
    if x < 10:
        # Manually raise the custom exception
        raise LowValueInputError(f"Value {x} is too low. Must be >= 10.")
    print("Value passed check.")

# --- Handling the Error ---
try:
    check_value(5) # This will fail
except LowValueInputError as e:
    # We catch the custom error type specifically
    print(f"Caught Custom Error: {e}") 
except Exception as e:
    # Catches all other unexpected errors
    print(f"Caught unexpected error: {e}")
```

### D. Common General Exceptions

| Exception | Technical Meaning | Typical Postgraduate Context |
| :--- | :--- | :--- |
| **`ValueError`** | Data value is invalid for the type (e.g., non-positive integer for a factorial function). | Data validation failure in numerical analysis or schema checks. |
| **`TypeError`** | Operation applied to incompatible types (e.g., heterogeneous operand types). | Matrix addition with a list and an array. |
| **`FileNotFoundError`**| Attempted access to a resource via an invalid path. | Failure to load configuration files or dataset archives. |
| **`KeyError`** | Invalid dictionary key or hash-map access. | Accessing a non-existent column in a Pandas DataFrame or configuration lookup. |

