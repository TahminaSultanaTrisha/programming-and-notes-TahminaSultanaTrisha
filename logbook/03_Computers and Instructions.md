
# 3. Computer Programming: Computers and Instructions - Enhanced Notes

## 1. Introduction to Python

### What is Python?
- **High-level, interpreted, general-purpose programming language**
- **Scripting language** - Python programs are called *scripts*

### Strengths & Weaknesses
| Strength | Weakness |
|----------|----------|
| Rapid development | Not optimal for speed |
| Experimentation | Not memory efficient |
| Easy to learn |  |

###  Deep Dive
- **High-level** = No direct memory management (unlike C/C++)
- **Interpreted** = Code executes line-by-line (flexible but slower than compiled languages)

###  Mnemonic: "Python P.R.I.D.E."
- **P**rototyping-friendly
- **R**apid development  
- **I**nterpreted
- **D**ynamic typing
- **E**asy syntax

---

## 2. Computer Architecture - Simplified Model

### Core Components
```
┌─────────────┐    ┌──────────┐    ┌──────────┐
│    CPU      │    │  Memory  │    │I/O Module│
│ ┌─────────┐ │    │          │    │          │
│ │ PCU     │ │    │ Program  │    │  Input   │
│ │ ALU     │ │◄──►│   &      │◄──►│  Output  │
│ │Registers│ │    │  Data    │    │          │
│ └─────────┘ │    │          │    │          │
└─────────────┘    └──────────┘    └──────────┘
        ▲                 ▲
        └───── Buses ─────┘
```

### Component Functions
- **Memory**: Stores data and programs
- **CPU**: Processes data
  - **ALU**: Performs calculations
  - **Registers**: Fast internal memory
  - **PCU**: Manages instruction execution
- **Buses**: Data transfer pathways
- **I/O Module**: Handles input/output

###  Kitchen Analogy
| Component | Kitchen Equivalent |
|-----------|-------------------|
| CPU | Chef |
| ALU | Chef's hands |
| Registers | Counter space |
| Memory | Refrigerator/pantry |
| Buses | Kitchen assistants |
| I/O | Delivery/serving window |

**Key Insight**: Data copying between memory and CPU is slow!

---

## 3. Data Representation in Memory

### Variable Creation: `spam = 42`
```
Name    Address     Value     Type
spam → 0x00000001 → 0b101010 → int
```

### Data Types
- **Primitive**: Integers, booleans, characters, floats
- **Compound**: Strings, arrays, objects

### String Storage Example
```python
product = 'spam'
```
```
Address    Value       Type
0x00000001 0b01110011  char 's'
0x00000002 0b01110000  char 'p'  
0x00000003 0b01100001  char 'a'
0x00000004 0b01101101  char 'm'
0x00000005 0b00000000  None (terminator)
```

###  Mnemonic: "Variables are Labels"
- **Name** = Label on mailbox
- **Address** = Physical mailbox location  
- **Value** = Letter inside mailbox

---

## 4. Limitations and Performance

### Data Restrictions
| Data Type | Limitation |
|-----------|------------|
| Integer | Limited by bit size (8-bit: -128 to 127) |
| Float | Limited precision and size |
| String | Limited by available memory |

###  Bit Limits Deep Dive
- **8-bit integer**: -128 to 127
- **32-bit integer**: ~-2.1 billion to ~2.1 billion  
- **64-bit integer**: ~±9.2 quintillion

### ⚠ Performance Warning
Processing large files (e.g., 1GB log files) can challenge memory limits!

---

## 5. Program Execution

### How Programs Run
1. **Instructions stored in memory** (like data)
2. **Program Counter (PC)** tracks next instruction address
3. **Instructions encoded as binary** values
4. **ALU executes** basic operations

###  Mnemonic: "PC Points to Next Chapter"
Program Counter = Bookmark in recipe book, always pointing to next step.

---

## 6. Thinking Like a CPU - ALU Operations

### Basic Operations
The ALU can only perform fundamental operations - complex tasks are built from these!

### Level 1: Count, Add, Negate
| Complex Operation | Implementation |
|-------------------|----------------|
| Subtraction | `A - B = A + (-B)` |
| Multiplication | Repeated addition |
| Division | Repeated subtraction |

###  Mnemonic: "ALU's SAN"
- **S**ubtract via Add+Negate
- **A**dd (directly)  
- **N**egate (for creating negatives)

### Level 2: Add Comparison to Zero
| Task | Implementation |
|------|----------------|
| Equality | `(A - B) == 0` |
| Less Than | `(A - B) < 0` |
| Greater Than | `(A - B) > 0` |
| Even/Odd | Check `(number % 2) == 0` |

###  Deep Dive
This is exactly how **assembly language** works! Programmers combine basic CPU instructions.

---

## 7. Programming Errors

### Two Main Error Types

#### Syntax Errors
- **What**: Violates language rules
- **Result**: Program fails to run
- **Example**: Missing colon, typos

#### Logic (Semantic) Errors  
- **What**: Valid code, wrong result
- **Result**: Runs but incorrect output
- **Example**: Wrong formula, incorrect condition

###  Mnemonic: "Syntax vs. Logic"
- **Syntax Error** = Grammar mistake ("I are hungry")
- **Logic Error** = Factual mistake ("The sky is green")

### Cooking Analogy
| Error Type | Cooking Equivalent |
|------------|-------------------|
| Syntax Error | "Add 2 cups flour" (missing what to do) |
| Logic Error | "Add 2 cups salt instead of sugar" |

---

## Key Takeaways

1. **Abstraction is Powerful**: Python hides hardware complexity
2. **Everything is Binary**: Data, instructions, addresses = 1s and 0s  
3. **CPU Speaks Simple Language**: Complex programs built from basic operations
4. **Computers are Literal**: Do exactly what you tell them, not what you *mean*


---
*Notes from: Computer Programming 3 - Computers and Instructions (7th & 9th October 2025)*