
## Week 07:  
## **6.Handling Errors: How Programming Develops**

Computer Programming Notes 6 — November 6, 2025

Modern Error Handling — Full Notes

Python • Happy Path • LBYL • EAFP

1. The Happy Path

The “happy path” is when everything goes right in your code. Inputs are good, every file’s where you expect, nothing weird happens, and the output makes sense.

Why does it matter? Most people use your program the way you intended. That’s where your program shines. This is the main part you usually build first.

Quick way to remember H.A.P.P.Y.:

Happens all the time  
Assumes valid stuff  
Produces what you expect  
Primary logic—the “main story”  
You always start here

2. When Things Go Off the Rails

But let’s be real—sometimes things break. People type in letters when you want numbers. Maybe they enter a negative number of students, which makes no sense. Sometimes they even try to break your program on purpose.

Two things can happen:

1. Your program crashes
2. Or worse, it gives the wrong answer, and nobody notices

Honestly, the second one is sneakier and can cause way more trouble.

3. What Can Go Wrong with Inputs?

Type Error  
 Try to turn something into a type it just can’t be. Like:

int("hello")  # Blows up with ValueError

Domain Error  
 Get the right type, but the value makes no sense.Like:

class_size = -5  # Sure, it’s an integer, but it’s not a real class size

Quick trick to remember: T.D.O. — Type, Domain, Outcome (crash or wrong answer)

4. LBYL — Look Before You Leap

This is where you check everything before you actually do anything.

Example:

user_input = input("How many students? ")

if user_input.isdigit():
    class_size = int(user_input)
else:
    print("Invalid input.")

Why do people use it?

- It stops exceptions before they happen.
- Great for simple, obvious checks.

What’s not so great?

- You end up writing the same checks over and over.
- It gets messy fast with more complicated inputs (like floats).

Mnemonic: LOOK  
Look first  
Only act if it’s safe  
Overhead (lots of checking)  
Keeps errors away

5. EAFP — Easier to Ask Forgiveness than Permission

This is the “just try it and deal with problems if they come up” way. Python programmers love it.

Example:

try:
    class_size = int(input("How many students? "))
except ValueError:
    print("Invalid number.")

Why bother?

- Code looks clean and simple
- Handles tricky cases you didn’t even think of
- It’s the Python way

Mnemonic: TRY  
Try it  
React if it fails  
Yield simpler code

6. Mixing LBYL and EAFP — Real Life

You’ll probably end up using both. For example:

try:
    class_size = int(input("How many students? "))
    if class_size <= 0:
        print("Class size must be positive.")
    else:
        print("Processing...")
except ValueError:
    print("Please enter a valid integer.")

LBYL is great for the quick, obvious checks. EAFP steps in when things get unpredictable.

7. try/except/else — Cleaner Structure

Here’s a tidy way to mix both styles:

try:
    class_size = int(input("How many students? "))
except ValueError:
    print("Invalid number.")
else:
    if class_size > 0:
        print("Valid class size.")
    else:
        print("Must be greater than zero.")

Mnemonic: T.E.E.  
Try  
Except  
Else

8. Raising Custom Exceptions

Sometimes, you want to enforce the rules yourself. That’s where raise comes in.

def get_class_size():
    class_size = int(input("How many students? "))
    if class_size <= 0:
        raise ValueError("Class size must be positive.")
    return class_size

This is super important for background tasks or scripts—when there’s no user around to see error messages.

Mnemonic: RAISE  
Report  
Abnormal  
Input  
Stop execution  
Explicit error

9. LBYL vs. EAFP at a Glance

| Approach  | Idea                    | Pros                | Cons                 |
| --------- | ----------------------- | ------------------- | -------------------- |
| LBYL      | Check before acting     | Stops errors early  | Gets wordy, messy    |
| EAFP      | Try and handle errors   | Clean, Pythonic     | Exceptions happen    |
| raise     | Trigger your own errors | Good validation     | Needs handling       |

10. Analogies You’ll Remember

LBYL? Like checking the weather before you leave home.  
EAFP? Just step outside with an umbrella, just in case it rains.
