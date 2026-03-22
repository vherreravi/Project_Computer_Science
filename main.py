"""
=============================================
  🚀 MAIN LAUNCHER
  Student Project Hub
=============================================

This file is the entry point for all student projects.
Run this file and choose which program to launch.

Run with:  python main.py
"""

import subprocess
import sys
import os


def clear_screen():
    """Clear the terminal screen on any OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    """Display the main menu."""
    print("=" * 45)
    print("   🎓  STUDENT PROJECT LAUNCHER")
    print("=" * 45)
    print()
    print("  Which project would you like to open?")
    print()
    print("  [1]  🧮  Calculator")
    print("  [2]  🗺️   Treasure Hunt Game")
    print("  [3]  ❌  Quit")
    print()
    print("=" * 45)


def launch_file(filename):
    """
    Launch a Python file as a separate process.
    Uses the same Python interpreter that is running this script.
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(filepath):
        print(f"\n  ⚠️  Could not find '{filename}'.")
        print(f"  Make sure it is in the same folder as main.py\n")
        return

    print(f"\n  ▶  Launching {filename} ...\n")
    subprocess.run([sys.executable, filepath])


def main():
    while True:
        clear_screen()
        print_menu()

        choice = input("  Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            launch_file("calculator_project.py")

        elif choice == "2":
            launch_file("treasure_game.py")

        elif choice == "3":
            clear_screen()
            print("\n  👋  Goodbye! Happy coding!\n")
            break

        else:
            print("\n  ❌  Invalid choice. Please enter 1, 2, or 3.")
            input("  Press Enter to try again...")


if __name__ == "__main__":
    main()
