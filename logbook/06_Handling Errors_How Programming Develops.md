## 6. Handling Errors: How Programming Develops

**Computer Programming Notes 6 : 6th November 2025**

---

# Modern Error Handling — Complete Notes

### *Python • Happy Path • LBYL • EAFP*

---

## 1. The Happy Path

The **Happy Path** is the situation where everything in a program works exactly as expected:

* Inputs are valid
* No files or devices are missing
* No unexpected behaviour occurs
* Output is correct and predictable

**Why it matters:**
Most users follow the Happy Path most of the time, so this is the part of the program that delivers the most value.

**Memory Trick — H.A.P.P.Y.:**

* **H**appens frequently
* **A**ssumes valid inputs
* **P**roduces expected results
* **P**rimary logic
* **Y**ou implement it first

---

## 2. When We Leave the Happy Path

Programs can fail when:

* Input is invalid (letters instead of numbers)
* Type is incorrect
* Value is unrealistic (e.g., negative students)
* Users intentionally or accidentally misuse the program

Two possible results:

1. The program **crashes**
2. The program gives **incorrect output**

Incorrect output is often worse because it may go unnoticed.

---

## 3. Types of Input Issues

### Type Error

Input cannot be converted into the expected type.

Example:

```python
int("hello")   # causes ValueError
```

### Domain Error

Input is the correct type but the wrong value.

Example:

```python
class_size = -5
```

**Quick Mnemonic — T.D.O.:**

* **T**ype
* **D**omain
* **O**utcome (crash or wrong result)

---

## 4. LBYL — Look Before You Leap

**Description:**
Check conditions *before* performing an operation.

Example:

```python
user_input = input("How many students? ")

if user_input.isdigit():
    class_size = int(user_input)
else:
    print("Invalid input.")
```

**Advantages:**

* Avoids exceptions
* Useful for simple checks

**Disadvantages:**

* Creates repetitive, cluttered code
* Hard to handle complex rules (e.g., floats)

**Mnemonic — LOOK:**

* **L**ook first
* **O**nly act if safe
* **O**verhead of checks
* **K**eeps errors away

---

## 5. EAFP — Easier to Ask Forgiveness than Permission

**Description:**
Attempt an operation and handle problems *if* they occur.

Preferred style in Python.

Example:

```python
try:
    class_size = int(input("How many students? "))
except ValueError:
    print("Invalid number.")
```

**Advantages:**

* Clean, readable code
* Works well with complex operations
* Pythonic

**Mnemonic — TRY:**

* **T**ry the operation
* **R**eact if it fails
* **Y**ield cleaner code

---

## 6. Mixing LBYL and EAFP (Practical Approach)

Real-world programs often combine both:

```python
try:
    class_size = int(input("How many students? "))
    if class_size <= 0:
        print("Class size must be positive.")
    else:
        print("Processing...")
except ValueError:
    print("Please enter a valid integer.")
```

LBYL checks *simple* conditions.
EAFP handles *unpredictable* conditions.

---

## 7. Using `try / except / else`

Cleaner structure:

```python
try:
    class_size = int(input("How many students? "))
except ValueError:
    print("Invalid number.")
else:
    if class_size > 0:
        print("Valid class size.")
    else:
        print("Must be greater than zero.")
```

**Mnemonic — T.E.E.:**

* **T**ry
* **E**xcept
* **E**lse

---

## 8. Raising Custom Exceptions

Use `raise` to enforce rules inside your program.

Example:

```python
def get_class_size():
    class_size = int(input("How many students? "))
    if class_size <= 0:
        raise ValueError("Class size must be positive.")
    return class_size
```

This is essential when there is no user present to read error messages (e.g., background services).

**Mnemonic — RAISE:**

* **R**eport
* **A**bnormal
* **I**nput
* **S**top execution
* **E**xplicit error

---

## 9. LBYL vs EAFP Summary Table

| Approach  | Idea                    | Pros                | Cons                 |
| --------- | ----------------------- | ------------------- | -------------------- |
| **LBYL**  | Check before acting     | Prevents errors     | Verbose, messy       |
| **EAFP**  | Try and handle errors   | Cleaner, Pythonic   | Exceptions may occur |
| **raise** | Trigger your own errors | Good for validation | Must be handled      |

---

## 10. Analogies to Remember

* **LBYL** → Checking the weather before you go outside
* **EAFP** → Going out and carrying an umbrella just in case


---
