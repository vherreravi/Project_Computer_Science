"""
=============================================
  🗺️  STUDENT PROJECT: Treasure Hunt Game
  Beginner Python + Tkinter GUI
=============================================

YOUR JOB as a student:
  - Complete the functions in the "STUDENT SECTION" below
  - Each function makes a DECISION about what happens in the game
  - Do NOT modify the "GAME ENGINE" or "GUI SECTION"

Run this file with:  python treasure_game.py
"""

import tkinter as tk
from tkinter import font as tkfont
import random


# ============================================================
#  ✏️  STUDENT SECTION — Write your decision functions here!
# ============================================================

def check_for_trap(room_number):
    """
    Decide whether a room contains a trap.

    Rules:
        - Room numbers 3 and 7 ALWAYS have a trap → return True
        - All other rooms are safe              → return False

    Example:
        check_for_trap(3)  →  True
        check_for_trap(5)  →  False

    HINT: Use an if/elif/else statement.

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def check_for_treasure(room_number, has_key):
    """
    Decide whether the player finds the treasure.

    Rules:
        - The treasure is ONLY in room 5
        - AND the player must have a key (has_key == True)
        - If both conditions are true → return True
        - Otherwise                   → return False

    Example:
        check_for_treasure(5, True)   →  True
        check_for_treasure(5, False)  →  False
        check_for_treasure(3, True)   →  False

    HINT: Use 'and' to check both conditions at once.

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def pick_up_key(room_number, already_has_key):
    """
    Decide whether the player picks up a key in this room.

    Rules:
        - A key is found ONLY in room 2
        - AND the player doesn't already have one (already_has_key == False)
        - If both conditions are true → return True  (player now has key)
        - Otherwise                   → return False

    Example:
        pick_up_key(2, False)  →  True
        pick_up_key(2, True)   →  False  (already have one!)
        pick_up_key(4, False)  →  False  (wrong room)

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


def calculate_score(rooms_visited, has_treasure, traps_hit):
    """
    Calculate the player's final score.

    Formula:
        - Start with 100 points
        - Add 10 points for each room visited
        - Add 200 points if the player has the treasure
        - Subtract 30 points for each trap hit
        - Score cannot go below 0 — if it's negative, return 0

    Example:
        calculate_score(4, True, 1)   →  100 + 40 + 200 - 30  = 310
        calculate_score(3, False, 2)  →  100 + 30 +   0 - 60  =  70
        calculate_score(2, False, 4)  →  100 + 20 +   0 - 120 =   0  (not negative!)

    HINT: Use max(0, score) at the end to prevent negative scores.

    TODO: Replace 'pass' with your code.
    """
    pass  # ← DELETE this line and write your solution


# ============================================================
#  ⚙️  GAME ENGINE — Do not edit below this line!
# ============================================================

ROOM_DESCRIPTIONS = {
    1: "🚪 A dusty entrance hall. Cobwebs everywhere.",
    2: "🔑 A dimly lit library. You hear something clinking...",
    3: "💀 A narrow corridor with strange markings on the floor.",
    4: "🪨 A cave room with dripping water.",
    5: "✨ A golden chamber... could this be it?",
    6: "🧱 A dead-end brick room. Nothing here.",
    7: "⚡ A chamber that feels... charged with danger.",
    8: "🌿 A mossy room near what looks like an exit.",
}

class GameState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_room = 1
        self.has_key = False
        self.has_treasure = False
        self.traps_hit = 0
        self.rooms_visited = set()
        self.log = []
        self.game_over = False

    def visit_room(self, room_number):
        """Process entering a room using the student's functions."""
        self.rooms_visited.add(room_number)
        self.current_room = room_number
        events = []

        # Check if student functions are implemented
        def safe_call(fn, *args):
            try:
                result = fn(*args)
                if result is None:
                    return None, True  # not implemented
                return result, False
            except Exception as e:
                return None, True

        desc = ROOM_DESCRIPTIONS.get(room_number, "An unknown room.")
        events.append(desc)

        # Key pickup
        key_result, not_impl = safe_call(pick_up_key, room_number, self.has_key)
        if not_impl:
            events.append("⚠️ pick_up_key() not done yet!")
        elif key_result and not self.has_key:
            self.has_key = True
            events.append("🔑 You found a KEY!")

        # Trap check
        trap_result, not_impl = safe_call(check_for_trap, room_number)
        if not_impl:
            events.append("⚠️ check_for_trap() not done yet!")
        elif trap_result:
            self.traps_hit += 1
            events.append("💥 TRAP! You lost some health! (-30 pts)")

        # Treasure check
        treasure_result, not_impl = safe_call(check_for_treasure, room_number, self.has_key)
        if not_impl:
            events.append("⚠️ check_for_treasure() not done yet!")
        elif treasure_result:
            self.has_treasure = True
            events.append("🏆 YOU FOUND THE TREASURE! Amazing!")
            self.game_over = True

        self.log.append("\n".join(events))

    def get_score(self):
        result, not_impl = None, True
        try:
            result = calculate_score(len(self.rooms_visited), self.has_treasure, self.traps_hit)
            if result is not None:
                not_impl = False
        except:
            pass
        if not_impl:
            return "??? (finish calculate_score!)"
        return result


# ============================================================
#  🖥️  GUI SECTION — Do not edit below this line!
# ============================================================

def build_game_gui():
    game = GameState()

    window = tk.Tk()
    window.title("🗺️ Treasure Hunt")
    window.geometry("480x560")
    window.configure(bg="#0d1117")
    window.resizable(False, False)

    # Fonts
    title_font = tkfont.Font(family="Courier", size=17, weight="bold")
    body_font  = tkfont.Font(family="Courier", size=10)
    btn_font   = tkfont.Font(family="Courier", size=10, weight="bold")
    mono_font  = tkfont.Font(family="Courier", size=9)

    # Title
    tk.Label(window, text="🗺️  TREASURE HUNT", font=title_font,
             bg="#0d1117", fg="#f0c674").pack(pady=(16, 2))
    tk.Label(window, text="Navigate rooms 1–8. Find the key. Find the treasure.",
             font=mono_font, bg="#0d1117", fg="#6e7681").pack()

    # Status bar
    status_frame = tk.Frame(window, bg="#161b22", padx=12, pady=8)
    status_frame.pack(fill="x", padx=16, pady=10)

    room_lbl   = tk.Label(status_frame, text="Room: 1", font=btn_font, bg="#161b22", fg="#79c0ff")
    key_lbl    = tk.Label(status_frame, text="Key: ✗", font=btn_font, bg="#161b22", fg="#ff7b72")
    traps_lbl  = tk.Label(status_frame, text="Traps: 0", font=btn_font, bg="#161b22", fg="#ffa657")
    score_lbl  = tk.Label(status_frame, text="Score: ?", font=btn_font, bg="#161b22", fg="#56d364")

    room_lbl.grid(row=0, column=0, padx=8)
    key_lbl.grid(row=0, column=1, padx=8)
    traps_lbl.grid(row=0, column=2, padx=8)
    score_lbl.grid(row=0, column=3, padx=8)

    # Log
    log_frame = tk.Frame(window, bg="#161b22", bd=2, relief="flat")
    log_frame.pack(padx=16, fill="both", expand=True)

    log_text = tk.Text(log_frame, font=mono_font, bg="#0d1117", fg="#c9d1d9",
                       wrap="word", relief="flat", bd=8, state="disabled", height=12)
    log_text.pack(fill="both", expand=True)

    # Room buttons
    tk.Label(window, text="Go to room:", font=mono_font,
             bg="#0d1117", fg="#6e7681").pack(pady=(10, 2))

    btn_frame = tk.Frame(window, bg="#0d1117")
    btn_frame.pack()

    def go_to_room(r):
        if game.game_over:
            return
        game.visit_room(r)
        refresh_ui()

    COLORS = ["#388bfd","#2ea043","#d29922","#f85149","#a371f7",
              "#39c5cf","#ec775c","#79c0ff"]

    for i in range(8):
        room_n = i + 1
        c = COLORS[i]
        tk.Button(
            btn_frame, text=f"R{room_n}", font=btn_font,
            bg=c, fg="#0d1117", activebackground="#fff",
            relief="flat", bd=0, width=4, height=2,
            cursor="hand2",
            command=lambda r=room_n: go_to_room(r)
        ).grid(row=0, column=i, padx=3, pady=4)

    # Reset button
    def reset_game():
        game.reset()
        refresh_ui(clear_log=True)

    tk.Button(
        window, text="↺  New Game", font=btn_font,
        bg="#21262d", fg="#c9d1d9", activebackground="#30363d",
        relief="flat", bd=0, padx=12, pady=6,
        cursor="hand2", command=reset_game
    ).pack(pady=(4, 12))

    def refresh_ui(clear_log=False):
        room_lbl.config(text=f"Room: {game.current_room}")
        key_lbl.config(
            text="Key: ✓" if game.has_key else "Key: ✗",
            fg="#56d364" if game.has_key else "#ff7b72"
        )
        traps_lbl.config(text=f"Traps: {game.traps_hit}")
        score_lbl.config(text=f"Score: {game.get_score()}")

        log_text.config(state="normal")
        if clear_log:
            log_text.delete("1.0", "end")
            log_text.insert("end", "🎮 New game started! Choose a room to explore.\n")
        elif game.log:
            entry = game.log[-1]
            log_text.insert("end", "\n" + "─"*40 + "\n" + entry + "\n")
            if game.game_over:
                log_text.insert("end", f"\n🎉 GAME OVER! Final Score: {game.get_score()}\n")
            log_text.see("end")
        log_text.config(state="disabled")

    # Initial message
    log_text.config(state="normal")
    log_text.insert("end", "🎮 Welcome! Choose a room to begin your adventure.\n")
    log_text.insert("end", "🔑 Hint: Find the key before heading to the treasure room!\n")
    log_text.config(state="disabled")

    window.mainloop()


if __name__ == "__main__":
    build_game_gui()
