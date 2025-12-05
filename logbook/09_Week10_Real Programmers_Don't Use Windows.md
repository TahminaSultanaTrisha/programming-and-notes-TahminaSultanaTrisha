## Week 10: 

## **9. Real Programmers Don't Use Windows**

Computer Programming notes 09: 27th November 2025  

Why the Command Line Still Matters  
At first glance, the command line looks ancient—just plain text and a blinking cursor. But it’s still a big deal, and here’s why:

- **It’s fast.** One quick command does the work of endless clicking.
- **It’s flexible.** You can chain commands, automate boring stuff, and script your own workflows.
- **It lasts.** Commands from the ‘70s still work now, and they’ll probably outlive you.
- **It’s everywhere.** Linux, macOS, Windows, even cloud servers—they all get it.

A Lamentation  
Every year, students wrestle with Git in the command line. Every year, some still cling to the “find the button” approach in their IDEs. And honestly? That’s frustrating. The command line is easier, faster, and gives you more options. Once you get the hang of it, you won’t want to go back.

The Command Line Basics  
- It’s a text-based way to talk to your computer.
- The “shell” (like bash or fish) interprets what you type.
- The “terminal” is just the window where you type.
- The wild part? Stuff from the 70s and 80s still works today.

IDEs vs GUIs (WIMP Interfaces)  
WIMP stands for Windows, Icons, Menus, and Pointer.

- Left-click to select.
- Right-click for a menu.
- Click X to close.
- Start menu to launch apps.

These metaphors—desktop, folders, windows—make life simple for most people. But programmers need to go deeper. GUIs hide the real guts of your system, and sometimes that gets in the way.

Cloud & Files  
Running a cloud server? Nine times out of ten, you’ll use the command line. Knowing where your files actually live—local or cloud—matters. Windows tries to tie files to one app, but as a programmer, you might want to use different tools on the same file. The command line makes that easy.

Git Example  
“Point-and-click” Git in an IDE? Menus everywhere, steps hidden away. With the command line, it’s clear:

$ cd focp-projects  
$ git status  
$ git add main.py  
$ git commit -m "Updated main.py"  
$ git push  

You see every step, you’re in control, and it’s always the same.

Pointy-Clicky vs Command-Line Tasks

| Task | GUI Struggle | CLI Solution |
|------|--------------|--------------|
| Compare two versions | IDE plugins | diff main_v1.py main_v2.py |
| Create nested folders | Click, drag | mkdir -p ~/focp-projects/project/src |
| Delete 10,000 logs | Select all, hope for the best | rm ~/focp-projects/project/src/log*.txt |
| Find TODOs | Dig through search menus | grep -rl "TODO" ~/focp-projects/project/src |
| Count TODOs | Manual counting | grep -rl "TODO" ~/focp-projects/project/src | wc -l |

Essential Commands Cheat Sheet  

File Operations  
- ls: list files  
- cd: move between folders  
- cp: copy files  
- mv: move or rename files  
- rm: delete files  
- mkdir: make new folders  
- rmdir: remove empty folders  

Finding Things  
- find: hunt down files or folders  
- grep: search inside files  
- locate: find files by name  
- which: see where programs live  

Working with Files  
- cat: show file contents  
- less: read one page at a time  
- head: see the top of a file  
- tail: see the end of a file  
- Editors: nano, vim, emacs  

Mnemonics to Remember

CRUD for files:  
- Create: mkdir  
- Read: cat, less, head, tail  
- Update: mv, cp  
- Delete: rm, rmdir  

FGLW for finding stuff:  
- Find: find  
- Grep: search inside files  
- Locate: search by name  
- Which: find executables  

Git 4-step mantra:  
- Status: see what’s changed  
- Add: stage files  
- Commit: save your snapshot  
- Push: upload to the repo  
Think: “Some Angry Cats Push.” Easy.

Analogy  
Think of the command line like learning guitar. At first, hitting the right “strings” (commands) feels clunky. With practice, we;ll start playing riffs—writing little scripts. Before we know it, we’re improvising full-blown symphonies, automating stuff no GUI can touch.

Conclusion  
The command line isn’t some dusty old tool—it’s  superpower. It gives speed, control, and skills that won’t go out of style. Learn it, use it.
