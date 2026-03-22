# 🎓 Student Python Project Intro to Computer Science

A beginner-friendly collection of Python mini-projects.  
Students write the **logic functions** — the GUI and game engine are already built and waiting.

---

## 📁 Project Structure

```
Parent_Folder(Project_Computer_Science)/
├── main.py                 ← START HERE — the project launcher
├── calculator_project.py   ← Project 1: Calculator with GUI
├── treasure_game.py        ← Project 2: Treasure Hunt Game with GUI
└── README.md               ← This file
```

---

## ▶️ How to Run

Make sure all four files are in the **same folder**, then open a terminal and run:

```bash
python main.py
```

You will see a menu like this:

```
=============================================
   🎓  STUDENT PROJECT LAUNCHER
=============================================

  Which project would you like to open?

  [1]  🧮  Calculator
  [2]  🗺️   Treasure Hunt Game
  [3]  ❌  Quit
```

Type `1` or `2` to launch a project. The GUI will open in a new window.  
When you close the window, you'll return to this menu.

---

## 🧮 Project 1 — Calculator

**File:** `calculator_project.py`

A working calculator with a graphical interface.  
Your job is to fill in the math functions that power the buttons.

### What You Write

Find the **STUDENT SECTION** near the top of the file and complete these four functions:

| Function | What it does | Concepts used |
|---|---|---|
| `add(a, b)` | Returns the sum of two numbers | `return` statement |
| `subtract(a, b)` | Returns the difference | arithmetic |
| `multiply(a, b)` | Returns the product | arithmetic |
| `divide(a, b)` | Returns the quotient — handles divide by zero | `if/else` |

### Tips

- Every function needs a `return` statement — without it, the GUI will warn you
- Start with `add` — it's just one line!
- For `divide`, think about what happens when someone types `0` as the second number

### Example

```python
def add(a, b):
    return a + b
```

---

## 🗺️ Project 2 — Treasure Hunt Game

**File:** `treasure_game.py`

A clickable room-exploration game.  
You navigate through 8 rooms trying to find a key and then the treasure — without hitting too many traps.

Your job is to write the **decision functions** that control what happens in each room.

### What You Write

Find the **STUDENT SECTION** near the top of the file and complete these four functions:

| Function | What it decides | Concepts used |
|---|---|---|
| `check_for_trap(room_number)` | Is there a trap in this room? | `if/elif/else` |
| `check_for_treasure(room_number, has_key)` | Did the player find the treasure? | `and` condition |
| `pick_up_key(room_number, already_has_key)` | Does the player pick up a key? | compound condition |
| `calculate_score(rooms, treasure, traps)` | What is the final score? | arithmetic, `max()` |

### Game Rules (read before coding!)

- 🔑 The **key** is hidden in **Room 2**
- 🏆 The **treasure** is in **Room 5** — but you need the key first
- 💥 **Rooms 3 and 7** contain traps — each trap costs 30 points
- 🧮 **Score formula:** `100 + (rooms visited × 10) + (200 if treasure) - (traps hit × 30)`

### Tips

- The status bar at the top of the game window updates live as you test
- If a function isn't done yet, the game will tell you with a ⚠️ warning
- Use the **New Game** button to reset and test different paths
- `calculate_score` is the hardest — save it for last

---

## ✅ Requirements

- **Python 3.6 or higher**
- **Tkinter** — comes pre-installed with Python on most systems

To check your Python version, run:

```bash
python --version
```

If Tkinter is missing (rare on Linux), install it with:

```bash
sudo apt-get install python3-tk
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| `python` not found | Try `python3` instead of `python` |
| Window doesn't open | Make sure all `.py` files are in the same folder |
| Function says "returned None" | You forgot the `return` keyword in your function |
| Game shows ⚠️ | That function isn't complete yet — keep going! |

---

## 💡 Key Concepts You'll Practice

- Writing and calling **functions**
- Using **`return`** to send a value back
- **`if / elif / else`** decision making
- Combining conditions with **`and`**
- Basic **arithmetic** and the **`max()`** built-in
- Understanding how **modules** work — `main.py` launches the others as separate programs

---

## 🏆 Stretch Goals

Finished early? Try these:

- **Calculator:** Add a square root or power (`**`) operation
- **Calculator:** Make the result show fewer decimal places using `round()`
- **Treasure Game:** Add a new room (Room 9) with your own trap/treasure rules
- **Treasure Game:** Change the scoring formula and see how it affects strategy
- **Both:** Read through the GUI code at the bottom — can you figure out how it works?

---

*Happy coding! Remember: every expert was once a beginner.* 🚀
