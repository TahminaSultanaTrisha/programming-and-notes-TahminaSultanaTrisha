## Week 05:  
## **5. Bugs (and Ducks)**

Computer Programming Notes 5: 23rd October 2025

1. Understanding Programming Errors

Two Main Types of Errors:

Syntax Errors  
- When your code doesn’t follow the language rules.  
- The program just won’t run or even compile.  
- Think missing semicolons, a typo, or messing up the indentation.

Logic (Semantic) Errors  
- The code runs, but the results are just wrong.  
- The program executes, but something’s off with its behavior.

Mnemonic for Error Types: S.L.I.P.  
S – Syntax: Broke the rules.  
L – Logic: Flawed thinking.  
I – Intention versus reality.  
P – Program runs but fails.

2. Deep Dive: Semantic Errors

Two Types of Logic Errors:

# Example: Calculator Division Function

# ERROR TYPE 1: Totally missed the point  
def divide_wrong(a, b):  
    return a * b  # Meant to divide, but wrote multiplication instead

# ERROR TYPE 2: Right code, wrong plan  
def divide_incorrect_intention(a, b):  
    return a / b  # Divides, but forgot to check for zero

Breakdown:  
- Wrong Implementation: The code doesn’t match what you actually meant.  
- Wrong Intention: What you meant was wrong from the start.

3. How Bugs Show Up

Two Ways Bugs Pop Up:

Stealth Bugs  
- The program seems fine... until it isn’t.  
- Wrong answers sneak in only for certain inputs.  
- Example: Calculator messes up only with negative numbers.

Crash Bugs  
- The app just gives up and crashes.  
- Example: Tries to open a weird file type and boom, it’s gone.

Error Probability Spectrum

error_handling_priority = {  
    "high_priority": ["user_input", "file_operations", "network_requests"],  
    "medium_priority": ["memory_usage", "edge_cases"],  
    "low_priority": ["cosmic_ray_bit_flips", "hardware_failures"]  
}

Engineering Principle: You want strong, reliable code, but don’t make it so complex you can’t handle it.

4. Bug Prevention Strategies

Proactive Moves

Code Reviews  
- Rule: “No code goes live without someone else checking it.”  
- Why? Catches mistakes, spreads knowledge, and keeps quality up.  
- Best way: Make reviews regular and keep the feedback helpful, not harsh.

Pair Programming  
- Two people, one keyboard.  
- Came from Extreme Programming (XP).  
- The perk? Instant feedback, double the perspective.

Mnemonic for Prevention: P.A.I.R.  
P – Peer review, every time  
A – Always work together  
I – Instant feedback  
R – Reduce bugs by teaming up

5. Debugging Techniques

Method 1: Dry Running  
- It’s just you and the code. Read it out or write it down, step by step.  
- Use printouts, a whiteboard, or just your head.  
- Before you start, know where it fails.  
- Walk through, track what changes.

Method 2: Debugger Tools  
- Use the debugger in your editor (PyCharm, VS Code, whatever).  
- You get breakpoints, step-by-step execution, watch variables, see the call stack.  
- Takes a bit to learn, but super useful.

Method 3: Rubber Duck Debugging

The Duck Trick:

def debug_with_duck(problem, duck):  
    print(f"Hey Duck, here’s my problem…")  
    print(f"I want my function to {problem['expected']}")  
    print(f"But it actually {problem['actual']}")  
    print(f"I’ll walk through my code, line by line…")  
    # That’s usually when you spot the bug.

Why does it work?  
You have to slow down and explain every step.  
You catch things you skipped in your head.  
It gets you thinking differently.  
Simple, but surprisingly powerful.

6. Philosophical Foundations

Linus’s Law  
“Given enough eyeballs, all bugs are shallow.”  
– Eric S. Raymond, The Cathedral and the Bazaar

What does it mean?  
If lots of people look, bugs stand out and get fixed faster.

The Engineering Trade-off  
- Nobody ships perfect software.  
- You have to weigh effort versus actual benefit.  
- Focus on making obvious errors safe for users.

7. Practical Debugging Workflow

Found a bug? Here’s what you do:

1. Reproduce it, every time.
2. Isolate the part of code causing trouble.
3. Analyze it – maybe with the duck, maybe by hand, maybe with a debugger.
4. Fix it, but make sure you know why it happened.
5. Test your fix, not just once.
6. Review the whole thing with a teammate.

Mnemonic for Debugging: D.U.C.K.S.  
D – Describe the problem (to the duck, or anyone)  
U – Understand the flow  
C – Check every variable  
K – Know what should happen  
S – Solve it, step by step

8. Key Takeaways

Here’s the bottom line:
1. Every program has bugs. It’s just part of the deal.
2. You can stop a lot of them early with reviews and pairing up.
3. Systematic debugging works. Random guessing doesn’t.
4. The duck is your friend. Really.
5. Always balance fixing bugs with actually getting things done.


