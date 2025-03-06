""" Required Function from Main Menu
Function	        Purpose
start_clock_game()	Initializes the Clock Game from the main menu."""

import tkinter as tk
from ui import ClockGame


def open_main_menu(root: tk.Toplevel, main_menu_root: tk.Tk):
    """Reopen the Main Menu when returning from Clock Game."""
    print("Returning to Main Menu...")  # Replace with actual main menu function
    root.destroy()  # HACK: The actual main menu function in question
    main_menu_root.deiconify()


def start_clock_game(main_menu_root: tk.Tk):
    """Start the Clock Game UI from the Main Menu."""
    root = tk.Toplevel()
    game = ClockGame(root, return_to_main_menu_callback=lambda: open_main_menu(root, main_menu_root))
    root.mainloop()


if __name__ == "__main__":
    start_clock_game()
