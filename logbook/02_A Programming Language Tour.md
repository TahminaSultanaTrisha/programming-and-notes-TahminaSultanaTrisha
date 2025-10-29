
---

# 2.A Programming Languages Tour– Master Study Guide  
**Computer Programming 2: 30th September & 2nd October 2025**

---

## Why Do We Program Computers?

Imagine a smartphone that only makes calls — useful, but limited. Now imagine one that runs apps, browses the web, plays music, and controls smart devices. That’s the power of programming.

- **Fixed-function computers**: Designed for one task (e.g., calculators, washing machines).
- **Programmable computers**: Can be reconfigured to perform many tasks — from gaming to data analysis.

> Mnemonic: **P.U.R.E.** – *Programmable, Useful, Reusable, Efficient*

> Noted: The word “computer” originally referred to people who performed calculations. Programming transformed machines into modern “computers.”

---

##  Historical Foundations of Programming:

> “You have to know the past to understand the present.” – Carl Sagan  
> “The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.” – Ada Lovelace

- **Ada Lovelace** (1843): First to recognize that machines could follow symbolic instructions — not just crunch numbers.
- **Charles Babbage**: Designed the Analytical Engine, a mechanical precursor to modern computers.
- **Colossus** (1940s): Used during WWII to break codes. Programmed with switches and plugs — no software as we know it.

> Mnemonic: **A.D.A.** – *Analytical, Deterministic, Algorithmic*

> Noted: Ada Lovelace Day (2nd Tuesday of October) celebrates women in STEM.

---

##  Computer Architecture – The Blueprint of a Machine

Think of a computer as a city:

| Component | Role | Analogy |
|----------|------|---------|
| **ALU** | Performs calculations | Calculator |
| **PCU** | Controls program flow | Traffic controller |
| **Registers** | Temporary storage | Sticky notes |
| **Memory** | Stores data | Filing cabinet |
| **I/O Modules** | Interfaces with devices | Doors and windows |
| **Buses** | Data pathways | Roads and highways |

> Mnemonic: **C.A.R.P.I.O.** – *Control, ALU, Registers, Pathways, Input/Output*

> Noted: Modern CPUs have billions of transistors — tiny switches that make logic possible.

---

##  First Generation Programming – The Age of Wires

- **Manual programming**: Using physical switches, punch cards, or plugboards.
- **Machine-specific**: No standardization — each computer had its own quirks.
- **Tedious and error-prone**: Required deep hardware knowledge.

> Mnemonic: **W.I.R.E.** – *Wired, Individualized, Rigid, Error-prone*

> Noted: The ENIAC (1945) took days to reprogram for a new task.

---

##  Second Generation Programming – Assembly Language

- **Assembly Language**: Uses mnemonics like `MOV`, `ADD`, `JMP` to represent machine instructions.
- **Still low-level**: One instruction = one CPU operation.
- **Hardware-dependent**: Code written for one CPU won’t work on another.

###  Example: Assembly Code Breakdown
```assembly
LD HL, MSG      ; Load address of message
LD A, (HL)      ; Load character
CP 0            ; Compare with null
JR Z, END       ; Jump if null
RST 10H         ; Print character
INC HL          ; Move to next character
JR LOOP         ; Repeat
RET             ; Return
MSG: DB 'Hello World!', 0
```

> Mnemonic: **A.S.S.E.M.B.L.Y.** – *Addressing, Symbolic, Specific, Efficient, Machine-Based, Low-level, Yet readable*

> Noted: Assembly is still used in embedded systems and performance-critical code.

---

##  Third Generation Programming – High-Level Languages

- **Human-readable syntax**: Like English sentences.
- **Portable**: Can run on different machines with the right translator.
- **Abstracted from hardware**: Focuses on logic, not circuitry.

> Mnemonic: **H.I.G.H.** – *Human-like, Interpreted/Compiled, General-purpose, Helpful*

> Noted: Languages like FORTRAN and COBOL were among the first high-level languages in the 1950s.

---

##  Compilers vs Interpreters – Translators of Code

| Feature | Compiler | Interpreter |
|--------|----------|-------------|
| Translation | Entire program at once | Line-by-line |
| Speed | Fast execution | Slower |
| Debugging | Harder | Easier |
| Output | Machine code file | No separate file |

> Mnemonic:  
- **C.O.D.E.** – *Compiled, Optimized, Delivered, Executed*  
- **I.D.E.A.** – *Interpreted, Debuggable, Executed, Adaptive*

> Noted: Some languages (e.g., Java) use both — compiling to bytecode, then interpreting via a virtual machine.

---

##  Popular Programming Languages – What’s in Your Toolbox?

| Language | Strengths | Use Cases |
|---------|-----------|-----------|
| **C / C++** | Speed, control | Systems, games, embedded |
| **Python** | Simplicity, readability | Data science, web, automation |
| **Rust** | Safety, concurrency | Systems, performance-critical apps |
| **Java / PHP** | Portability, web | Enterprise, backend development |

> Mnemonic: **C.P.R.J.** – *Control (C++), Pythonic, Reliable (Rust), Java-ready*

> Noted: Python is often used to teach beginners due to its clean syntax.

---

##  Why Python?

- **High-level**: Abstracted from hardware.
- **Interpreted**: Runs line-by-line.
- **General-purpose**: Versatile across domains.
- **Readable syntax**: Easy to learn and use.

> Mnemonic: **P.Y.T.H.O.N.** – *Powerful, Yet Tiny, Human-Oriented, Neat*

> Noted: Python was named after *Monty Python*, not the snake!

---

##  Core Concepts in All Languages

Every programming language boils down to three core ideas:

1. **Sequence** – Instructions executed in order.
2. **Selection** – Decisions using conditions (`if`, `switch`).
3. **Iteration** – Repeating actions (`for`, `while` loops).

> Mnemonic: **S.S.I.** – *Sequence, Selection, Iteration*

> Noted: These are the building blocks of *structured programming*, a paradigm that avoids spaghetti code.

---

##  Final Thought – The Language of Logic

> “Once you know one language, maybe you know them all?”

Learning programming is like learning to cook. Once you understand ingredients (data), recipes (algorithms), and techniques (syntax), you can switch cuisines (languages) with ease.

> Mnemonic: **L.O.G.I.C.** – *Learn Once, Grow In Code*

---

