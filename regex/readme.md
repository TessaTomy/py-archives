# 🔍 Regex in Python

*Regular expressions are the foundational tool for complex text analysis, parsing, and data cleaning. Mastering them shifts text processing from being a brute-force approach to an algebraic one.*

-----

## 1\. 🎯 Definition and the Python `re` Module

A **Regular Expression** defines a formal pattern (a miniature programming language) used to search, locate, and manipulate specific sequences of characters within larger texts.

  * **Python Integration:** All regex functionality is implemented via the built-in **`re` module**.

-----

## 2\. 📝 Fundamental Pattern Components

Regex patterns are constructed using three primary building blocks: **Literals**, **Metacharacters**, and **Quantifiers**.

### A. Metacharacters (Positional & Structural)

These are reserved symbols that instruct the regex engine on the structure of the pattern:

| Metacharacter | Description | Technical Role |
| :--- | :--- | :--- |
| **`.`** | Matches **any single character** (wildcard, except newline by default). | General character matching. |
| **`^`** | Matches the **start of the string**. | Anchor: Ensures the match begins at position 0. |
| **`$`** | Matches the **end of the string**. | Anchor: Ensures the match ends at the last position. |
| **`[]`** | **Character Set:** Defines a custom range of accepted characters. | `[A-Za-z0-9]` matches any letter or digit. |
| **`|`** | **OR Operator:** Matches the expression before or after the pipe. | `(error|fail)` matches either word. |

### B. Quantifiers (Frequency Control)

Quantifiers define the number of times the preceding component (character, set, or group) must occur:

| Quantifier | Description | Technical Meaning |
| :--- | :--- | :--- |
| **`*`** | **Zero or more** (Greedy). | $0 \le n < \infty$ |
| **`+`** | **One or more** (Greedy). | $1 \le n < \infty$ |
| **`?`** | **Zero or one** (Optional or Non-Greedy). | $n = 0$ or $n = 1$ |
| **`{m,n}`**| Between **$m$ and $n$** occurrences. | $m \le n \le n$ (Used for fixed lengths, e.g., `\d{4}` for a year). |

-----

## 3\. 🐍 Special Sequences (Shorthands)

These sequences are used with the backslash (`\`) and serve as highly common, predefined character sets.

| Sequence | Description | Equivalent Character Set |
| :--- | :--- | :--- |
| **`\d`** | Any **digit** (0-9). | `[0-9]` |
| **`\D`** | Any **non-digit** character. | `[^0-9]` |
| **`\w`** | Any **word character** (alphanumeric + underscore). | `[a-zA-Z0-9_]` |
| **`\s`** | Any **whitespace** character (space, tab, newline). | |
| **`\b`** | Matches the empty string at a **word boundary**. | Used to isolate whole words. |

-----

## 4\. 🔗 The `re` Module Functions (Hands-On Examples)

The `re` module provides specialized functions for applying patterns to strings. Understanding the return type of each function is crucial for practical implementation.

*Let's use the text: `text = "Email: user@domain.com, Phone: 555-123-4567, ID: 987-AB"`*
*And the pattern: `pattern = r"(\d{3})-(\d{3}-\d{4})"` (Matches a phone number, capturing the area code and the rest of the number).*

| Function | Behavior | Return Type | Example & Output |
| :--- | :--- | :--- | :--- |
| **`re.search(p, s)`** | Finds the **first occurrence** anywhere in the string. | **Match Object** or `None`. | **Example:** `match = re.search(pattern, text)`<br>**Output:** `match.group(0)` returns **`555-123-4567`** |
| **`re.match(p, s)`** | Looks for a match **only at the beginning** of the string. | **Match Object** or `None`. | **Example:** `match = re.match(pattern, text)`<br>**Output:** `None` (as the text starts with "Email: ", not a number). |
| **`re.findall(p, s)`** | Finds **all non-overlapping matches**. | **List** of strings or tuples. | **Example:** `re.findall(pattern, text)`<br>**Output:** `[('555', '123-4567')]`<br>(Returns tuples because the pattern contains capturing groups `()`). |
| **`re.finditer(p, s)`** | Finds all matches and returns them as an **iterator** of Match Objects. | **Iterator** of Match Objects. | **Example:** `for m in re.finditer(pattern, text): print(m.group(1))` <br>**Output:** `555` |
| **`re.sub(p, r, s)`** | Substitutes all matches found by the pattern with the replacement string (`r`). | Modified **String**. | **Example:** `re.sub(r"ID: \d{3}-\w+", "ID: XXX", text)`<br>**Output:** `"Email: user@domain.com, Phone: 555-123-4567, ID: XXX"` |
| **`re.split(p, s)`** | Splits the string by occurrences of the pattern. | **List of Strings**. | **Example:** `re.split(r",\s*", text)`<br>**Output:** `['Email: user@domain.com', 'Phone: 555-123-4567', 'ID: 987-AB']`|

-----

## 4.5 💡 The Dual Role of Parentheses (`()`)

In Regular Expressions, parentheses serve two crucial and distinct functions: **Grouping** (for structure) and **Capturing** (for data retrieval).

### A. Grouping (Structural Use)

Parentheses treat a sequence of characters or sub-patterns as a single, indivisible **unit**. This is primarily needed to apply **quantifiers** (like `+`, `*`, or `{n}`) to the entire sequence.

| Pattern | Description | Matches |
| :--- | :--- | :--- |
| **`(ha)+`** | Matches the entire sequence "ha" **one or more times**. | `ha`, `haha`, `hahaha` |
| **`(ab|cd)`** | Matches either the sequence **"ab"** or **"cd"**. | `ab` or `cd` |

### B. Capturing (Data Retrieval Use)

Any text matched by the expression inside the parentheses is **captured and saved** in a numbered group. This allows you to retrieve specific subsets of information from a successful overall match.

  * **Usage:** Groups are retrieved using methods like `match.group(1)`, `match.group(2)`, etc.

#### 💡 Example: Retrieving Captured Groups

*Pattern: `r"(\w+)\s+(\w+)"`* (Applied to "Alice Smith")

| Match Group Index | Content Captured by `()` | Retrieved Value (Example) |
| :--- | :--- | :--- |
| **Group 0** (`match.group(0)`) | The entire overall match. | `"Alice Smith"` |
| **Group 1** (`match.group(1)`) | The content of the first `()` group. | `"Alice"` |
| **Group 2** (`match.group(2)`) | The content of the second `()` group. | `"Smith"` |

### C. The OR Operator (`|`) and Precedence

The **OR operator (`|`)** allows alternation (match Pattern A OR Pattern B). It has the **lowest precedence**, meaning it attempts to match the largest possible expression on either side.

  * **Precedence Rule:** To correctly limit the scope of the `|` operator (e.g., to only alternate two small words), you **must use parentheses** to define the boundaries of the choices.
  * **Order Rule (Ambiguity):** When options are ambiguous (one is a substring of the other, e.g., "cat" and "catastrophe"), always place the **most specific or longest pattern choice on the LEFT side of the `|`**. The engine uses a "First Match Wins" approach.

### 🧠 Example: Ordering and Scoping

```python
import re

# Order matters: If "cat" is first, "catastrophe" is never matched at the same position.
pattern_A = r"(cat|catastrophe)"
results_A = re.findall(pattern_A, "A catastrophe is coming.") 
# Output: ['cat'] (Incorrect, matched the shorter prefix)

# Correct Order: Longer/Specific word first.
pattern_B = r"(catastrophe|cat)"
results_B = re.findall(pattern_B, "A catastrophe is coming.")
# Output: ['catastrophe'] (Correct)
```

-----

### D. Capturing vs. Non-Capturing Groups (`(...)` vs. `(?:...)`)

When grouping the OR choices or applying quantifiers, you must decide whether to **Capture** (save the content) or just **Group** (structure the pattern).

| Syntax | Role | Purpose | Saves to `match.groups()`? |
| :--- | :--- | :--- | :--- |
| **`(...)`** | **Capturing Group** | Used for both structural grouping and **data extraction**. | **YES** |
| **`(?:...)`**| **Non-Capturing Group** | Used **only** for structural grouping (e.g., controlling `|` or a quantifier). | **NO** |

### 💡 Code Example: Controlling Output

```python
import re
text = "The quick cat runs."

# 1. Capturing Pattern: Captures the color choice and the animal choice.
pattern_capturing = r"(quick|slow)\s+(cat|dog)"
results_capturing = re.findall(pattern_capturing, text)
# Output: [('quick', 'cat')] 
# Analysis: Both color and animal are saved.

# 2. Non-Capturing Pattern: Groups the color choice but only captures the animal.
pattern_non_capturing = r"(?:quick|slow)\s+(cat|dog)"
results_non_capturing = re.findall(pattern_non_capturing, text)
# Output: ['cat']
# Analysis: The color choice was used to match but was discarded, only the animal is saved.
```

-----

### E. Lookaheads for Complex Validation

A **Lookahead** (`(?=...)`) is a zero-width assertion that checks for a condition ahead in the string **without consuming characters**. This allows you to check multiple, independent constraints (like character types and length) simultaneously at the start of the string.

### Pattern: Contains Upper, Lower, Digit, and Length is 9

**Pattern:** `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{9}$`

### Breakdown:

| Component | Technical Name | Role |
| :--- | :--- | :--- |
| **`^`** | Start Anchor | Position the engine at the start. |
| **`(?=.*[a-z])`** | **Lookahead 1 (Lowercase)** | Asserts that **one lowercase letter** exists somewhere (`.*`). |
| **`(?=.*[A-Z])`** | **Lookahead 2 (Uppercase)** | Asserts that **one uppercase letter** exists somewhere (`.*`). |
| **`(?=.*\d)`** | **Lookahead 3 (Digit)** | Asserts that **one digit** exists somewhere (`.*`). |
| **`.{9}`** | **Main Match** | Consumes **exactly 9** characters, enforcing the length after all assertions pass. |
| **`$`** | End Anchor | Ensures the string ends here. |

### Example Logic

| Text | Match Result | Reason for Success/Failure |
| :--- | :--- | :--- |
| **`Abc123456`** | **Match** | Passes all three lookaheads and is exactly 9 characters. |
| **`abc123456`** | **No Match** | Fails Lookahead 2: Missing `[A-Z]`. |
| **`Abc12345`** | **No Match** | Fails the final length constraint: Length is 8. |

-----

## 5\. 🛠️ Optimization and Best Practices

### A. Raw Strings (`r""`)

  * **Crucial Practice:** Always use **raw strings** (prefix the pattern with `r`, e.g., `r"\d{3}"`).
  * **Rationale:** This prevents Python from interpreting the backslash (`\`) for its own escape sequences (`\n`, `\t`), ensuring the pattern is passed to the regex engine exactly as written (`\d` instead of just `d`).

### B. Pattern Compilation

For patterns that will be applied to multiple different strings or used within a loop, **compilation** is essential for performance.

  * **Syntax:** `compiled_regex = re.compile(pattern)`
  * **Benefit:** The pattern is pre-processed into an internal automaton representation, avoiding the parsing step on every subsequent search operation.

<!-- end list -->

```python
# Compilation for performance
PHONE_REGEX = re.compile(r"(\d{3})-(\d{3}-\d{4})") 

match = PHONE_REGEX.search(text) 
```
