
---
# Week 08:
## 7. How does AI fit in?

**Computer Programming Notes 7: 13th November 2025**


---

##  1. Introduction

Artificial Intelligence (AI) is now a core part of modern software development.
Tools like **GitHub Copilot** act as an *AI pair programmer*, helping with:

* Code suggestions
* Docstrings
* Tests
* Debugging help
* Refactoring
* Explanations



---

##  2. Why AI Matters in Programming?
Universities were initially concerned about cheating when tools like ChatGPT arrived.
But in **Computer Science**, AI became a *power tool*, similar to search engines.

AI helps with:

* Faster prototyping
* Cleaner code
* Reduced typing effort
* Better documentation
* Automated testing ideas

What it **cannot** replace:

* Understanding
* Logic
* Debugging
* Security awareness

---

##  3. Developer Mindset Shift

Developers traditionally solved problems by Googling.
Now the workflow evolves to:

> "Ask the AI → Review the output → Modify → Test"


 **Mnemonic:**
**T.R.U.S.T.**

* **T**est everything
* **R**ead suggestions carefully
* **U**nderstand before using
* **S**implify unclear code
* **T**hink critically

---

##  4. What GitHub Copilot Does

GitHub Copilot can:

### ✔ Code Completion

Suggest entire lines or full functions as you type.

### ✔ Docstring Generation

Write documentation from short descriptions.

### ✔ Test Suggestions

Generate pytest-style test cases.

### ✔ Refactoring

Improve variable names and code clarity.

### ✔ Debugging Help

Explain why code fails and propose fixes.

---

##  5. Installing Copilot in VS Code

1. Install **GitHub Copilot** extension
2. Sign in with GitHub (Student Pack = FREE full access)
3. Enable inline suggestions
4. Customize shortcuts (Tab, Ctrl+Enter)
5. Adjust privacy settings

---

##  6. Prompt Engineering Basics

Your prompts control AI output quality.

**Mnemonic: P.R.O.M.P.T.**

* **P**urpose
* **R**equirements
* **O**utput format
* **M**inimal example
* **P**lan or constraints
* **T**one / clarity

### Example Prompt

```python
def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignore case and non-letters)."""
```



---

## 7. Example: Prime Number Function

Copilot might propose:

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

 ## Task:

Check logic, check edge cases, add tests.

---

##  8. Example: Fibonacci Function

```python
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

Copilot typically prefers readable iterative solutions — good for beginners.

---

##  9. Test-Driven Development (TDD)

A powerful workflow:

1. Write tests first
2. Ask Copilot to implement code
3. Review and refine

### Example Test

```python
def test_fib():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
```

---

## 10. Debugging With Copilot

Show the AI human failing code and test.
Example:

```python
def sum_to(n):
    total = 0
    for i in range(1, n):  # Off-by-one error
        total += i
    return total
```

Copilot may suggest:

> “Use `range(1, n+1)` to include n.”

But **human decide** if the fix is correct.

---

##  11. Refactoring Suggestions

Copilot may rewrite:

**Before:**

```python
def s(x):
    return [i*i for i in x if i % 2 == 0]
```

**After:**

```python
def squared_evens(values: list[int]) -> list[int]:
    return [x * x for x in values if x % 2 == 0]
```

Clear names = better code and better AI suggestions.

---

##  12. Security Rules

Never accept AI suggestions that include:

* API keys
* Passwords
* Tokens
* Private data
* Sensitive configuration

These should always be manually created and stored securely.

---

##  13. Licensing & Attribution

AI-generated output **may resemble** open-source code.

Safe practice:

* Review licenses
* Cite use of Copilot if your course requires
* Ensure your submission is your own work

---

##  14. Academic Integrity

Using AI: ✔ allowed
Submitting AI-generated code blindly: ✘ cheating
Submitting code you don’t understand: ✘ cheating

Recommended comment:

```text
# Used GitHub Copilot for suggestions; all code reviewed and modified by me.
```

---

## 15. What we gonna do to enhance productivity 

* Use **short** and **clear** prompts
* Write good names and docstrings
* Combine AI with tools like:

  * `flake8` (linting)
  * `black` (formatting)
  * `mypy` (type checking)
* Always, always test AI-suggested code

---
