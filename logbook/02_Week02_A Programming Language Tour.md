
## Week 02:  
## **2. A Programming Languages Tour**  
Computer Programming Notes 2: 30th September 2025

Why Do We Program Computers?

Fixed-function computers only do one thing—they’re built for a single job. Programmable computers, though, can be told to do just about anything, from running video games to crunching data for science.

Quick way to remember it: P.U.R.E. – Programmable, Useful, Reusable, Efficient.

Fun fact: “Computer” used to mean a person who did calculations. Programming is what turned machines into what we call computers today.

Historical Foundations of Programming

“You have to know the past to understand the present.” – Carl Sagan  
“The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.” – Ada Lovelace

Ada Lovelace was way ahead of her time in 1843. She realized machines could follow instructions—actual symbols and logic—not just do math. Charles Babbage, her collaborator, designed the Analytical Engine, basically the ancestor of modern computers. Fast forward a century, and in the 1940s, the Colossus helped crack secret codes in WWII, programmed not with software, but with switches and plugs.

Remember: A.D.A. – Analytical, Deterministic, Algorithmic.

Ada Lovelace Day (2nd Tuesday in October) celebrates women in STEM fields.

Computer Architecture – The Blueprint of a Machine

Picture a computer as a city. Each part has a job:

ALU: Handles calculations—your calculator.  
PCU: Keeps everything running smoothly—think traffic control.  
Registers: Short-term notes—sticky notes everywhere.  
Memory: Where stuff gets stored—like a giant filing cabinet.  
I/O Modules: Connections to the outside—doors and windows.  
Buses: How it all moves—roads and highways.

C.A.R.P.I.O. helps you remember: Control, ALU, Registers, Pathways, Input/Output.

Modern CPUs? Billions of transistors packed inside—tiny switches making all the logic work.

First Generation Programming – The Age of Wires

Back in the day, programming meant flipping switches, plugging in wires, or punching holes in cards. Each computer was its own beast—no standards, just quirks. It was slow going and mistakes were easy to make, since you needed to know exactly how the hardware worked.

Think W.I.R.E.: Wired, Individualized, Rigid, Error-prone.

The ENIAC (1945) needed days just to switch to a new task.

Second Generation Programming – Assembly Language

Assembly language brought in mnemonics like MOV, ADD, JMP—finally, some readable code. Still, each instruction matched directly to a CPU operation, and programs stayed tightly linked to the hardware. If you wrote code for one kind of CPU, it just wouldn’t run on another.

Here’s a quick assembly example:
LD HL, MSG      ; Load address of message  
LD A, (HL)      ; Load character  
CP 0            ; Compare with null  
JR Z, END       ; Jump if null  
RST 10H         ; Print character  
INC HL          ; Move to next character  
JR LOOP         ; Repeat  
RET             ; Return  
MSG: DB 'Hello World!', 0

A.S.S.E.M.B.L.Y. sums it up: Addressing, Symbolic, Specific, Efficient, Machine-Based, Low-level, Yet readable.

People still use assembly in embedded systems or when performance absolutely matters.

Third Generation Programming – High-Level Languages

High-level languages finally let us write code that looks a bit like English. They’re portable—run them on almost any computer, as long as you’ve got the right tool to translate. You don’t need to care about the hardware details; you just focus on the logic.

H.I.G.H. stands for: Human-like, Interpreted/Compiled, General-purpose, Helpful.

FORTRAN and COBOL kicked things off in the 1950s.

Compilers vs Interpreters – Translators of Code

Compilers and interpreters are like translators for code. Compilers take your whole program and turn it into machine code all at once. Interpreters go line by line, translating as they go.

Compilers: Fast code, but debugging is a pain. Interpreters: Slower, but easier to test and fix mistakes. Compilers spit out a new file; interpreters don’t.

C.O.D.E. helps you remember compilers: Compiled, Optimized, Delivered, Executed.  
I.D.E.A. does the same for interpreters: Interpreted, Debuggable, Executed, Adaptive.

Some languages, like Java, use both: they compile code to bytecode, then interpret it with a virtual machine.

Popular Programming Languages – What’s in Your Toolbox?

C / C++: Super fast, gives you control—great for systems, games, and embedded stuff.  
Python: Simple, easy to read—lots of use in data science, web, or automation.  
Rust: Safe and handles concurrency well—used for systems or performance-heavy programs.  
Java / PHP: Portable, web-friendly—think enterprise apps and backend development.

C.P.R.J. makes it easy: Control (C++), Pythonic, Reliable (Rust), Java-ready.

Python gets used a lot with beginners, mostly because its syntax is so clean.

Why Python?

High-level, so you’re not sweating the hardware details.  
Interpreted, so it runs line by line—easy to test and debug.  
General-purpose, so you can use it for just about anything.  
Readable syntax, so you spend less time fighting the language and more time building things.

P.Y.T.H.O.N. helps sum it up: Powerful, Yet Tiny, Hum...



