# 5. Bugs (and Ducks) - Master Notes

**Notes from Lecture;Date:** October 23rd, 2025  


---

## 1. Understanding Programming Errors

### Two Main Types of Errors:

####  **Syntax Errors**
- **Definition:** Code that violates language rules
- **Result:** Program fails to compile or run
- **Examples:** Missing semicolons, typos, incorrect indentation

#### **Logic (Semantic) Errors**
- **Definition:** Code runs but produces wrong results
- **Result:** Program executes but behaves incorrectly

###  **Mnemonic for Error Types: S.L.I.P.**
- **S**yntax - Rules broken
- **L**ogic - Wrong thinking
- **I**ntention vs Reality gap
- **P**rogram runs but fails

---

## 2. Deep Dive: Semantic Errors

### Two Types of Logic Errors:

```python
# Example Scenario: Calculator Division Function

# ERROR TYPE 1: Wrong implementation of intention
def divide_wrong(a, b):
    return a * b  # Intended division but implemented multiplication

# ERROR TYPE 2: Correct implementation of wrong intention  
def divide_incorrect_intention(a, b):
    return a / b  # Correctly divides, but should check for zero first
```

**Breakdown:**
-  **Wrong Implementation:** Code doesn't match your mental model
-  **Wrong Intention:** Your mental model itself is flawed

---

## 3. How Bugs Manifest

### Two Manifestation Patterns:

#### **Stealth Bugs**
- Program appears normal
- Produces incorrect results in specific situations
- **Example:** Calculator gives wrong answer only for negative numbers

####  **Crash Bugs**
- Program fails completely
- **Example:** App crashes when loading specific file types

### **Error Probability Spectrum**
```python
error_handling_priority = {
    "high_priority": ["user_input", "file_operations", "network_requests"],
    "medium_priority": ["memory_usage", "edge_cases"], 
    "low_priority": ["cosmic_ray_bit_flips", "hardware_failures"]
}
```

**Engineering Principle:** Balance between robustness and complexity

---

## 4. Bug Prevention Strategies

###  **Proactive Approaches**

####  **Code Reviews**
- **Principle:** "No code enters final system without peer review"
- **Benefits:** Catches bugs, shares knowledge, improves code quality
- **Best Practice:** Regular, constructive feedback sessions

####  **Pair Programming**
- **Definition:** Two developers working together continuously
- **Origin:** Extreme Programming (XP) methodology
- **Advantage:** Real-time code review and knowledge sharing

###  **Mnemonic for Prevention: P.A.I.R.**
- **P**eer review mandatory
- **A**lways collaborate  
- **I**mmediate feedback
- **R**educed bugs through teamwork

---

## 5. Debugging Techniques

###  **Method 1: Dry Running**
- **Definition:** Manual code execution "by hand"
- **Tools:** Printouts, whiteboards, mental execution
- **Prerequisite:** Know failure scenarios
- **Process:** Step through code line by line, track variable changes

###  **Method 2: Debugger Tools**
- **Tools:** IDE debuggers (PyCharm, VS Code, etc.)
- **Features:**
  - Breakpoints
  - Step execution
  - Variable inspection
  - Call stack tracing
- **Learning Curve:** Moderate but highly effective

###  **Method 3: Rubber Duck Debugging**

#### The Famous Duck Technique:
```python
# The Rubber Duck Debugging Process
def debug_with_duck(problem, duck):
    print(f"Hello Duck, I have a problem...")
    print(f"My function should {problem['expected']}")
    print(f"But instead it {problem['actual']}")
    print(f"Let me explain my code line by line...")
    #  REALIZATION OCCURS DURING EXPLANATION!
    return solution
```

**Why It Works:**
- Forces systematic thinking
- Reveals hidden assumptions
- Engages different parts of brain
- Simple but remarkably effective

---

## 6. Philosophical Foundations

###  **Linus's Law**
> "Given enough eyeballs, all bugs are shallow."
> - Eric S. Raymond, The Cathedral and the Bazaar

**Interpretation:** Collective review makes bugs easier to find and fix

###  **The Engineering Trade-off**
- **Perfect vs Practical:** 100% bug-free vs shipping usable software
- **Cost-Benefit:** Weigh debugging effort against impact
- **User Experience:** Handle obvious errors gracefully

---

## 7. Practical Debugging Workflow

###  **When You Find a Bug:**

1. **Reproduce** the issue consistently
2. **Isolate** the problematic code section
3. **Analyze** using appropriate technique (Duck → Dry Run → Debugger)
4. **Fix** with understanding of root cause
5. **Test** the fix thoroughly
6. **Review** the solution with peers

###  **Mnemonic for Debugging: D.U.C.K.S.**
- **D**escribe the problem (to duck)
- **U**nderstand the code flow
- **C**heck variable states
- **K**now the expected behavior
- **S**olve systematically

---

## 8. Key Takeaways

###  **Essential Wisdom:**
1. **All programs have bugs** - it's normal!
2. **Prevention** through reviews and pairing
3. **Systematic debugging** beats random guessing
4. **The duck works** - don't underestimate simple techniques
5. **Balance effort** with practical needs

###  ** Debugging Toolkit:**
-  Rubber Duck (or patient colleague)
-  Dry running skills
-  IDE Debugger proficiency
-  Code review culture
- ️ Systematic approach

---

**Final Thought:** Debugging isn't failure - it's an essential part of the programming craft. Embrace the duck! 

*Notes created from "Computer Programming 5: Bugs (and Ducks)" presentation materials.*